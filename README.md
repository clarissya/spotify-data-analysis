# 🎵 Spotify Tracks Data Analysis & Insights

Proyek analisis data sederhana untuk mengidentifikasi karakteristik lagu populer di Spotify menggunakan Python.

## 📌 Business Overview & Objective
Tujuan dari analisis ini adalah untuk memahami fitur audio (*audio features*) apa saja yang membedakan lagu populer (*hit*) dari lagu non-hit, serta memberikan rekomendasi berbasis data bagi produser musik dan tim A&R (Artist & Repertoire).

## 🛠️ Tools & Libraries
- **Language:** Python 3.13
- **Libraries:** Pandas, Matplotlib, Seaborn
- **Dataset:** Spotify Tracks Dataset (Kaggle by Maharshi Pandya)

## 📊 Key Findings & Insights

### 1. Genre Paling Populer
Genre seperti **Pop, Dance/EDM, Reggaeton, dan K-Pop** mendominasi tingkat popularitas rata-rata tertinggi.
> **Reason:** Genre ini memiliki *replay value* tinggi, struktur melodi mainstream, serta dukungan kurasi *editorial playlist* Spotify global (seperti *Today's Top Hits*).

### 2. Fitur Audio vs Popularity (Korelasi)
Korelasi antara fitur audio individual (*danceability, energy, valence*, dll.) terhadap `popularity` cenderung **lemah** ($|r| < 0.2$).
> **Insight:** Popularitas suatu lagu tidak hanya ditentukan oleh satu karakteristik musik saja, melainkan gabungan dari kombinasi audio, reputasi artis, strategi pemasaran, dan tren media sosial (TikTok/Reels).

### 3. Karakteristik Lagu Hit vs Non-hit
- **Danceability:** Lagu *hit* (`popularity >= 70`) memiliki tingkat *danceability* lebih tinggi dibanding lagu non-hit.
- **Energy & Loudness:** Lagu *hit* cenderung diproduksi dengan *loudness* yang optimal dan energi yang relatif dinamis untuk menarik perhatian pendengar dalam beberapa detik pertama.
- **Acousticness:** Lagu *hit* memiliki nilai *acousticness* yang jauh lebih rendah (didominasi produksi musik modern/elektronik).

## 💡 Recommendations for A&R / Music Producers
1. **Target Durasi Ideal:** Buat lagu dengan durasi optimal **2.5 – 3.5 menit** untuk memaksimalkan *stream count* dan sesuai dengan tren perilaku pendengar modern.
2. **Audio Profiling:** Prioritaskan *danceability* di atas 0.60 dan tingkat *loudness* jernih tanpa mengalami *clipping*.
3. **Explicit Content:** Jangan ragu menggunakan label *explicit* jika sesuai target audiens, karena secara statistik tidak mengurangi potensi kerekatan popularitas di platform digital.

## ⚠️ Limitations
- **Snapshot Data:** Dataset bersifat statis pada satu titik waktu, sedangkan metrik *popularity* Spotify bersifat dinamis dan terus berubah.
- **External Factors:** Dataset tidak memperhitungkan variabel eksternal seperti anggaran iklan/pemasaran, jumlah *followers* artis, maupun fenomena viralitas di luar Spotify.