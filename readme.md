# 📦 Scaffolder

> Buat struktur folder project otomatis dari blueprint teks — tanpa klik satu per satu.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Size](https://img.shields.io/badge/Size-1%20file-5eead4) ![License](https://img.shields.io/badge/License-MIT-green)

---

## Cara Pakai

```bash
python mkproject.py
```

Script akan menanyakan 3 hal secara berurutan:

**1. Lokasi** — di mana folder project dibuat
```
📁 Lokasi target: desktop
   Maksudnya di '/home/user/Desktop'? [Y/n]: y
```

**2. Nama project** — nama folder utamanya
```
📦 Nama project: web-app
   Buat project 'web-app' di dalam '/home/user/Desktop'? [Y/n]: y
```

**3. Blueprint** — ketik struktur yang diinginkan, lalu tekan `Ctrl+D` untuk eksekusi
```
📝 Masukkan blueprint:

app.py
requirements.txt
/templates
  index.html
/static
  style.css
```

**Hasil:**
```
web-app/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

---

## Aturan Blueprint

- Nama diawali atau diakhiri `/` → dibuat sebagai **folder**
- Selain itu → dibuat sebagai **file**
- Indent (spasi) → menandakan isi dari folder di atasnya

---

## Shortcut Lokasi

Tidak perlu ketik path lengkap:

| Ketik | Path |
|-------|------|
| `desktop`, `deks`, `dekstop` | `~/Desktop` |
| `downloads`, `dl`, `donlod` | `~/Downloads` |
| `documents`, `doc`, `dokumen` | `~/Documents` |
| `home` | `~` |

Typo umum sudah dikenali otomatis.

---

## Author

**Mr. Elixir** — [@MrElixir1945](https://github.com/MrElixir1945)
