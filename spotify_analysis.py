# Proyek Portofolio: Analisis Karakteristik Lagu Populer di Spotify
# Dataset : "Spotify Tracks Dataset" (Kaggle, by maharshipandya)
# Tools   : Python (pandas, matplotlib, seaborn)
# ============================================================

# 1. IMPORT & LOAD DATA
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("charts", exist_ok=True)

df_raw = pd.read_csv("dataset.csv")
print("Ukuran data awal:", df_raw.shape)
print(df_raw.head())
print(df_raw.info())

# 2. DATA CLEANING
df = df_raw.copy()
df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")])

print("\nMissing value per kolom:\n", df.isna().sum())
df = df.dropna(subset=["artists", "album_name", "track_name"])  

df_genre = df.drop_duplicates(subset=["track_id", "track_genre"])
df = df.sort_values("popularity", ascending=False).drop_duplicates(subset="track_id")
print("\nSetelah hapus duplikat:", df.shape)

df["duration_min"] = df["duration_ms"] / 60000
df_genre = df_genre.assign(duration_min=df_genre["duration_ms"] / 60000)

before = len(df)
df = df[(df["tempo"] > 0) & (df["time_signature"] > 0)]
print(f"Baris tidak valid dihapus: {before - len(df)}")

df = df[df["duration_min"] <= 10]

df["is_hit"] = df["popularity"] >= 70
print("\nJumlah lagu hit vs non-hit:\n", df["is_hit"].value_counts())

df.to_csv("spotify_clean.csv", index=False)

# 3. STATISTIK DESKRIPTIF
audio_features = ["danceability", "energy", "valence", "acousticness",
                  "speechiness", "liveness", "loudness", "tempo", "duration_min"]
print(df[audio_features + ["popularity"]].describe().round(2))

# 4. GENRE: yang paling populer
genre_stats = (df_genre.groupby("track_genre")["popularity"]
               .agg(["mean", "count"]).query("count >= 50")
               .sort_values("mean", ascending=False))
top10 = genre_stats.head(10).reset_index()

plt.figure(figsize=(9, 5))
sns.barplot(data=top10, x="mean", y="track_genre", color="#1DB954")
plt.title("10 Genre dengan Rata-rata Popularitas Tertinggi")
plt.xlabel("Rata-rata popularity")
plt.ylabel("")
plt.tight_layout()
plt.savefig("charts/01_top_genre.png", dpi=150)
plt.show()

# 5. KORELASI: fitur audio vs popularity
corr = df[audio_features + ["popularity"]].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdYlGn", center=0)
plt.title("Korelasi Fitur Audio dengan Popularity")
plt.tight_layout()
plt.savefig("charts/02_correlation.png", dpi=150)
plt.show()

print("\nKorelasi dengan popularity:\n",
      corr["popularity"].drop("popularity").sort_values(ascending=False).round(3))

# 6. LAGU HIT vs NON-HIT
comparison = df.groupby("is_hit")[audio_features].mean().T.round(3)
comparison.columns = ["Non-hit", "Hit"]
comparison["Selisih (%)"] = ((comparison["Hit"] - comparison["Non-hit"])
                             / comparison["Non-hit"] * 100).round(1)
print(comparison)

plot_feats = ["danceability", "energy", "valence", "acousticness"]
melted = df.melt(id_vars="is_hit", value_vars=plot_feats)
plt.figure(figsize=(9, 5))
sns.barplot(data=melted, x="variable", y="value", hue="is_hit",
            palette={False: "#B3B3B3", True: "#1DB954"}, errorbar=None)
plt.title("Karakteristik Lagu Hit vs Non-hit")
plt.xlabel("")
plt.ylabel("Rata-rata nilai (0-1)")
plt.legend(title="Lagu hit?")
plt.tight_layout()
plt.savefig("charts/03_hit_vs_nonhit.png", dpi=150)
plt.show()

# 7. EXPLICIT vs NON-EXPLICIT
explicit = df.groupby("explicit")["popularity"].agg(["mean", "count"]).round(2)
print("\nPopularity berdasarkan konten explicit:\n", explicit)

plt.figure(figsize=(6, 5))
sns.boxplot(data=df, x="explicit", y="popularity", palette=["#B3B3B3", "#1DB954"])
plt.title("Distribusi Popularity: Explicit vs Non-explicit")
plt.tight_layout()
plt.savefig("charts/04_explicit.png", dpi=150)
plt.show()

# 8. DURASI LAGU vs POPULARITY
df["durasi_kategori"] = pd.cut(df["duration_min"], bins=[0, 2.5, 3.5, 4.5, 10],
                               labels=["<2.5 mnt", "2.5-3.5", "3.5-4.5", ">4.5 mnt"])
dur = df.groupby("durasi_kategori", observed=True)["popularity"].mean().reset_index()

plt.figure(figsize=(7, 5))
sns.barplot(data=dur, x="durasi_kategori", y="popularity", color="#1DB954")
plt.title("Rata-rata Popularity Berdasarkan Durasi Lagu")
plt.xlabel("Durasi")
plt.tight_layout()
plt.savefig("charts/05_durasi.png", dpi=150)
plt.show()