
# CapitalConductor API — GitHub + Railway Ready (Docker)

Endpoints
- GET /health
- POST /deck/unlock   {"password":"Conductor2025"}
- POST /analytics/track   {"type":"deck_open","id":"demo","email":"x@y.com"}

Deploy to Railway (via GitHub)
1) Create a new empty GitHub repo.
2) Upload **the contents** of this folder to the repo root and commit.
3) Railway → New Project → Deploy from GitHub → select your repo.
   - Builder: **Dockerfile**
   - Root directory: `/`
   - Start Command: leave **empty** (Docker CMD runs /start.sh)
4) Open `/health` on your Railway URL.

Env (Railway → Variables)
- LIVE_DECK_PASSWORD=Conductor2025
- (optional) GHL_INCOMING_WEBHOOK_URL, SHEET_ID, GOOGLE_SERVICE_ACCOUNT_JSON=/tmp/sa.json

If using Google Sheets: add a File Secret with your service account JSON mounted at `/tmp/sa.json` or write it from a base64 var in a custom Start Command.
