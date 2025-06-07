import pandas as pd
import matplotlib.pyplot as plt

# Lee el CSV con rankings ATP (ajusta ruta si es necesario)
df = pd.read_csv('rankings_atp.csv').head(10)

plt.figure(figsize=(10,6))
plt.bar(df['full_name'], df['ranking_points'])
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 ATP – Ranking Points')
plt.ylabel('Points')
plt.tight_layout()

plt.savefig('top10_atp.png')
print('✓ Gráfica guardada como top10_atp.png en api_tennis')
