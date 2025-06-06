# Tennis Live Data API – Rankings (ATP & WTA)

Este sub-proyecto consume la **Tennis Live Data API (sportcontentapi)** para descargar los rankings
actuales de la ATP y la WTA y guardarlos en CSV.

## Cómo ejecutar

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install requests python-dotenv

# Crear .env (NO subirlo)
API_HOST=tennis-live-data.p.rapidapi.com
API_KEY=TU_CLAVE

python tennis_rankings.py
