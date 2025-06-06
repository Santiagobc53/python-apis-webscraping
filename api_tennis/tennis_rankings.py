import os, requests, csv
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("API_HOST")            # tennis-live-data.p.rapidapi.com
KEY  = os.getenv("API_KEY")
HEADERS = {
    "X-RapidAPI-Key": KEY,
    "X-RapidAPI-Host": HOST
}

def get_rankings(tour="ATP"):
    """Descarga rankings ATP o WTA."""
    url = f"https://{HOST}/rankings/{tour}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()["results"]["rankings"]   # <── ajuste clave

def save_csv(rows, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"✓ Guardado {filename} ({len(rows)} filas)")

if __name__ == "__main__":
    save_csv(get_rankings("ATP"), "rankings_atp.csv")
    save_csv(get_rankings("WTA"), "rankings_wta.csv")
