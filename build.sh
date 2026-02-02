curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv sync

if [ -n "$DATABASE_URL" ]; then
  psql -a -d "$DATABASE_URL" -f database.sql || true
fi