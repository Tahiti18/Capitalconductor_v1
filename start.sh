
#!/usr/bin/env bash
# force rebuild
set -e
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT:-8000}"
