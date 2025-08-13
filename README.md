
# CapitalConductor API — Production-lite

## What you get
- Password gate: `POST /deck/unlock`
- Analytics tracking: `POST /analytics/track` → persists to Postgres
- Export: `GET /events/export.csv`
- Signed invites: `/invites/sign?email=&project_id=`, `/invites/verify?token=`
- CORS allowlist, rate limiting, Sentry (optional)

## Railway setup
1) Add a **Postgres** database in Railway → note the `DATABASE_URL`.
2) New service → Deploy this repo → Builder: Dockerfile → Root: `/` → Start Command: empty.
3) Variables:
```
LIVE_DECK_PASSWORD=conductor2025
DATABASE_URL=postgresql://...
ALLOWED_ORIGINS=https://YOUR-NETLIFY-SITE.netlify.app
JWT_SECRET=some-long-random
```
4) Deploy → `/health` should return ok.

