# MixLab — Color Picker & Mixer

![MixLab Screenshot](src/assets/screenshot.png)

**MixLab** is a free, offline color picker and mixer for **artists, designers, painters, decorators, DIY enthusiasts, and anyone who works with physical paints or color matching**.  
Perfect for choosing wall colors, mixing art supplies, or matching digital designs to real-world materials.

✅ 100% offline after first launch  
✅ No ads, no tracking, no telemetry  
✅ Open-source (MIT License)  
✅ Windows standalone executable (.exe)  
✅ 12 languages supported  
✅ **Pure pigment palette**: Only 5 artist-grade pigments (Cadmium Red, Cadmium Yellow, Ultramarine Blue, Titanium White, Ivory Black)

---

## ✨ Features

- 🎨 **RYB pigment model** — realistic mixing based on artist pigments (not RGB/CMYK)
- 🖼️ **Image loader** — open any image from your computer
- 🔍 **Eyedropper tool** — pick colors directly from images
- 🔬 **10x magnifier** — preview pixels before selection
- 🧪 **Smart mixing recipes** — see exact proportions to mix colors from base paints:
  - `#FFD800` → yellow:10 (pure cadmium yellow)
  - `#E60000` → red:10 (pure cadmium red)
  - `#0033A0` → blue:10 (pure ultramarine)
  - `#212121` → black:8 + white:2 (dark gray)
- ✏️ **HEX input** — type any HEX color code directly (e.g. `#e13509`) to instantly see the color and its mixing recipe. Supports right-click context menu (cut / copy / paste / select all)
- 🎵 **Color Harmony Tool** — opens an interactive browser page showing complementary, triadic, analogous and tetradic palettes for the selected color, with live visual demos
- ➕ **Manual mixer** — create custom blends with adjustable parts (only pure pigments allowed)
- 🌍 **12 languages**: English, Русский, Español, Deutsch, Français, Italiano, Português, العربية, 中文, 日本語, Polski, Türkçe — all UI elements including the harmony tool are fully localized
- 💙 **Developer support** — optional QR code donations via Ko-fi (downloads automatically on first launch)

---

## 📦 Download (Windows)

📥 [**Download MixLab v1.0 for Windows**](https://github.com/milleran41/MixLab/releases/latest)

> No installation required!  
> 1. Download `MixLab-v1.0-win.zip`  
> 2. Extract the archive  
> 3. Run `MixLab.exe`  
> *First launch downloads QR code (requires internet). All subsequent uses work 100% offline.*

---

## 🎵 Color Harmony Tool

Click the **Color Harmony** button (next to Clear) to open an interactive harmony viewer in your browser.  
It automatically uses the color currently selected in MixLab and opens in the app's active language.

Supported harmony types:
| Type | Description |
|------|-------------|
| Complementary | 2 colors opposite on the color wheel |
| Triadic | 3 colors evenly spaced (120°) |
| Analogous | 3 neighboring colors (±30°) |
| Tetradic | 4 colors forming a rectangle (90°) |

The tool works fully offline — no internet required after the first launch.

---

## ✏️ HEX Color Input

In the **Selected Color** panel you can type any HEX code manually:

- Type with or without `#` — both `e13509` and `#e13509` are accepted
- Color preview and mixing recipe update instantly as you type
- Right-click the field for **Cut / Copy / Paste / Select All** in your current language
- When picking a color from an image or palette, the field syncs automatically

---

## 🛠️ Build from Source

### Requirements
- Python 3.8+
- Git (optional)

### Steps
```bash
# Clone repository
git clone https://github.com/milleran41/MixLab.git
cd MixLab

# Install dependencies
pip install -r requirements.txt

# Run the application
cd src
python main.py
```

### Build executable (Windows)
```bash
cd src
pyinstaller MixLab-Windows.spec
# Output: src/dist/MixLab-Windows.exe
```

---

## 📁 Project Structure

```
MixLab/
├── src/
│   ├── main.py                  # Main application
│   ├── assets/
│   │   ├── icon.ico             # App icon
│   │   ├── harmony.html         # Color Harmony Tool (offline browser page)
│   │   ├── qr-donate.png        # Ko-fi QR code
│   │   └── screenshot.png       # Screenshot for README
│   ├── MixLab-Windows.spec      # PyInstaller build config
│   └── MixLab.spec
├── requirements.txt
└── README.md
```

---

## 📄 License

MIT License — free to use, modify and distribute.  
See [LICENSE](LICENSE) for details.
