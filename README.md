# MixLab — Color Picker & Mixer

![MixLab Screenshot](assets/screenshot.png)

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
- ➕ **Manual mixer** — create custom blends with adjustable parts (only pure pigments allowed)
- 🌍 **12 languages**: English, Русский, Español, Deutsch, Français, Italiano, Português, العربية, 中文, 日本語, Polski, Türkçe
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
python main.py