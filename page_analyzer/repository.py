import psycopg2
from psycopg2.extras import RealDictCursor


class UrlsRepository:

    def __init__(self, db_url):
        self.db_url = db_url

    def get_connection(self):
        return psycopg2.connect(self.db_url)

    def get_urls(self):
        conn = self.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT * FROM urls")
                return cur.fetchall()
        finally:
            conn.close()

    def find(self, id):
        conn = self.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""SELECT * FROM urls WHERE id = %s""", (id,))
                return cur.fetchone()
        finally:
            conn.close()

    def find_by_name(self, normalized_url):
        conn = self.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""SELECT * FROM urls where name = %s""", (normalized_url,))  # noqa: E501
                return cur.fetchone()
        finally:
            conn.close()

    def save(self, normalized_url):
        conn = self.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO urls (name) VALUES (%s) RETURNING id""", (normalized_url,))  # noqa: E501
                saved_id = cur.fetchone()[0]
                conn.commit()
            return saved_id
        finally:
            conn.close()

    def get_url_with_checks(self):
        conn = self.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT
                            u.id,
                            u.name,
                            uc.created_at,
                            uc.status_code
                        FROM urls u
                        LEFT JOIN url_checks uc ON u.id=uc.url_id
                        AND uc.id = (SELECT MAX(id) FROM url_checks
                        WHERE url_id = u.id)
                        ORDER BY u.id DESC"""
                )
                return cur.fetchall()
        finally:
            conn.close()


class ChecksRepository:

    def __init__(self, db_url):
        self.db_url = db_url

    def get_connection(self):
        return psycopg2.connect(self.db_url)

    def create_check(self, url_id, check_data):
        conn = self.get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO url_checks
                        (url_id, status_code, h1, title, description)
                        VALUES (%s, %s, %s, %s, %s) RETURNING id""",
                    (
                        url_id,
                        check_data.get("status_code"),
                        check_data.get("h1", ""),
                        check_data.get("title", ""),
                        check_data.get("description", ""),
                    ),
                )
                check_id = cur.fetchone()[0]
                conn.commit()
            return check_id
        except psycopg2.errors.DatabaseError as e:
            print(f"Ошибка при создании проверки:{e}")
        finally:
            conn.close()

    def get_checks_by_url_id(self, url_id):
        conn = self.get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM url_checks
                        WHERE url_id = %s
                        ORDER BY id DESC""",
                    (url_id,),
                )
                return cur.fetchall()
        finally:
            conn.close()
