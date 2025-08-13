# CapitalConductor Monorepo

- Backend (FastAPI): root Dockerfile, app/..., start.sh
- Frontend (Next.js): frontend/

Deploy
- Backend → Railway
  - Builder: Dockerfile
  - Root: /
  - Start Command: empty
- Frontend → Netlify
  - Base directory: frontend
  - Build command: npm run build
  - Publish directory: .next
  - Env: NEXT_PUBLIC_API_BASE=https://<your-railway-api-domain>
