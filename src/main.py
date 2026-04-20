import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import os
import sys
import webbrowser
import urllib.request
import threading
import math
from typing import Any, Callable, Dict, List, Optional, Tuple

# === Типы для глобальных переменных ===
root: Optional[tk.Tk] = None
canvas: Optional[tk.Canvas] = None
color_display: Optional[tk.Frame] = None
color_hex_label: Optional[ttk.Label] = None
recipe_frame: Optional[ttk.LabelFrame] = None
recipe_title: Optional[tk.Label] = None
manual_frame: Optional[ttk.Frame] = None
result_label: Optional[tk.Frame] = None
result_hex_label: Optional[ttk.Label] = None
palette_inner: Optional[ttk.Frame] = None
palette_support_frame: Optional[ttk.LabelFrame] = None
zoom_label: Optional[ttk.Label] = None
lang_button: Optional[ttk.Menubutton] = None
support_frame: Optional[ttk.Frame] = None
upload_btn: Optional[ttk.Button] = None
save_btn: Optional[ttk.Button] = None
zoom_in_btn: Optional[ttk.Button] = None
zoom_out_btn: Optional[ttk.Button] = None
clear_btn: Optional[ttk.Button] = None
left_frame: Optional[ttk.LabelFrame] = None
color_frame: Optional[ttk.LabelFrame] = None
manual_frame_outer: Optional[ttk.LabelFrame] = None
result_label_text: Optional[ttk.Label] = None
color_label: Optional[ttk.Label] = None
add_btn: Optional[ttk.Button] = None
hex_entry: Optional[tk.Entry] = None
hex_entry_var: Optional[tk.StringVar] = None
hex_hint_label: Optional[ttk.Label] = None

# === Локализация (12 языков) ===
translations = {
'en': {
'title': "MixLab - Color Picker & Mixer",
'upload_image': "Upload Image",
'save_image': "Save Image",
'select_color': "Selected Color",
'color_recipe': "Color Recipe",
'manual_mix': "Manual Mixing",
'color_palette': "Color Palette",
'parts': "parts",
'percentage': "percent",
'click_to_upload': "Click to upload an image",
'red': "Red",
'yellow': "Yellow",
'blue': "Blue",
'green': "Green",
'violet': "Violet",
'black': "Black",
'white': "White",
'add_color': "Add Color",
'result': "Result",
'delete': "Delete",
'zoom_in': "Zoom In",
'zoom_out': "Zoom Out",
'clear': "Clear",
'no_image': "No image loaded",
'recipe_not_available': "Select a color to see the mixing recipe",
'magnifier_title': "Magnifier",
'selected_pixel': "Pixel:",
'zoom': "Zoom: 10x",
'image': "Image",
'custom_mix': "Custom Mix",
'support_project': "Support Project",
'color_harmony': "Color Harmony",
'enter_hex': "Enter HEX color",
'cut': "Cut",
'copy': "Copy",
'paste': "Paste",
'select_all': "Select All",
'current_lang_name': "English"
},
'ru': {
'title': "MixLab - Пипетка и смешивание цветов",
'upload_image': "Загрузить изображение",
'save_image': "Сохранить изображение",
'select_color': "Выбранный цвет",
'color_recipe': "Рецепт смешивания",
'manual_mix': "Ручное смешивание",
'color_palette': "Палитра цветов",
'parts': "части",
'percentage': "процентов",
'click_to_upload': "Нажмите, чтобы загрузить изображение",
'red': "Красный",
'yellow': "Жёлтый",
'blue': "Синий",
'green': "Зелёный",
'violet': "Фиолетовый",
'black': "Чёрный",
'white': "Белый",
'add_color': "Добавить цвет",
'result': "Результат",
'delete': "Удалить",
'zoom_in': "Увеличить",
'zoom_out': "Уменьшить",
'clear': "Очистить",
'no_image': "Изображение не загружено",
'recipe_not_available': "Выберите цвет, чтобы увидеть рецепт смешивания",
'magnifier_title': "Лупа",
'selected_pixel': "Пиксель:",
'zoom': "Увеличение: 10x",
'image': "Изображение",
'custom_mix': "Пользовательское смешивание",
'support_project': "Поддержать проект",
'color_harmony': "Гармония цветов",
'enter_hex': "Введите HEX цвет",
'cut': "Вырезать",
'copy': "Копировать",
'paste': "Вставить",
'select_all': "Выделить всё",
'current_lang_name': "Русский"
},
'es': {
'title': "MixLab - Selector y Mezclador de Colores",
'upload_image': "Cargar Imagen",
'save_image': "Guardar Imagen",
'select_color': "Color Seleccionado",
'color_recipe': "Receta de Color",
'manual_mix': "Mezcla Manual",
'color_palette': "Paleta de Colores",
'parts': "partes",
'percentage': "por ciento",
'click_to_upload': "Haga clic para cargar una imagen",
'red': "Rojo",
'yellow': "Amarillo",
'blue': "Azul",
'green': "Verde",
'violet': "Violeta",
'black': "Negro",
'white': "Blanco",
'add_color': "Añadir Color",
'result': "Resultado",
'delete': "Eliminar",
'zoom_in': "Acercar",
'zoom_out': "Alejar",
'clear': "Limpiar",
'no_image': "No hay imagen cargada",
'recipe_not_available': "Seleccione un color para ver la receta de mezcla",
'magnifier_title': "Lupa",
'selected_pixel': "Píxel:",
'zoom': "Zoom: 10x",
'image': "Imagen",
'custom_mix': "Mezcla Personalizada",
'support_project': "Apoyar el Proyecto",
'color_harmony': "Armonía de Colores",
'enter_hex': "Ingrese color HEX",
'cut': "Cortar",
'copy': "Copiar",
'paste': "Pegar",
'select_all': "Seleccionar todo",
'current_lang_name': "Español"
},
'de': {
'title': "MixLab - Farbpipette & Mischer",
'upload_image': "Bild hochladen",
'save_image': "Bild speichern",
'select_color': "Ausgewählte Farbe",
'color_recipe': "Farb-Rezept",
'manual_mix': "Manuelles Mischen",
'color_palette': "Farbpalette",
'parts': "Teile",
'percentage': "Prozent",
'click_to_upload': "Klicken Sie, um ein Bild hochzuladen",
'red': "Rot",
'yellow': "Gelb",
'blue': "Blau",
'green': "Grün",
'violet': "Violett",
'black': "Schwarz",
'white': "Weiß",
'add_color': "Farbe hinzufügen",
'result': "Ergebnis",
'delete': "Löschen",
'zoom_in': "Vergrößern",
'zoom_out': "Verkleinern",
'clear': "Löschen",
'no_image': "Kein Bild geladen",
'recipe_not_available': "Wählen Sie eine Farbe, um das Rezept zu sehen",
'magnifier_title': "Lupe",
'selected_pixel': "Pixel:",
'zoom': "Vergrößerung: 10x",
'image': "Bild",
'custom_mix': "Benutzerdefinierte Mischung",
'support_project': "Projekt unterstützen",
'color_harmony': "Farbharmonie",
'enter_hex': "HEX-Farbe eingeben",
'cut': "Ausschneiden",
'copy': "Kopieren",
'paste': "Einfügen",
'select_all': "Alles auswählen",
'current_lang_name': "Deutsch"
},
'fr': {
'title': "MixLab - Pipette et Mélangeur de Couleurs",
'upload_image': "Charger une Image",
'save_image': "Enregistrer l'Image",
'select_color': "Couleur Sélectionnée",
'color_recipe': "Recette de Couleur",
'manual_mix': "Mélange Manuel",
'color_palette': "Palette de Couleurs",
'parts': "parties",
'percentage': "pour cent",
'click_to_upload': "Cliquez pour charger une image",
'red': "Rouge",
'yellow': "Jaune",
'blue': "Bleu",
'green': "Vert",
'violet': "Violet",
'black': "Noir",
'white': "Blanc",
'add_color': "Ajouter une Couleur",
'result': "Résultat",
'delete': "Supprimer",
'zoom_in': "Zoom Avant",
'zoom_out': "Zoom Arrière",
'clear': "Effacer",
'no_image': "Aucune image chargée",
'recipe_not_available': "Sélectionnez une couleur pour voir la recette de mélange",
'magnifier_title': "Loupe",
'selected_pixel': "Pixel:",
'zoom': "Zoom: 10x",
'image': "Image",
'custom_mix': "Mélange Personnalisé",
'support_project': "Soutenir le Projet",
'color_harmony': "Harmonie des Couleurs",
'enter_hex': "Entrez la couleur HEX",
'cut': "Couper",
'copy': "Copier",
'paste': "Coller",
'select_all': "Tout sélectionner",
'current_lang_name': "Français"
},
'it': {
'title': "MixLab - Selettore e Miscelatore di Colori",
'upload_image': "Carica Immagine",
'save_image': "Salva Immagine",
'select_color': "Colore Selezionato",
'color_recipe': "Ricetta del Colore",
'manual_mix': "Miscelazione Manuale",
'color_palette': "Tavolozza dei Colori",
'parts': "parti",
'percentage': "percento",
'click_to_upload': "Fai clic per caricare un'immagine",
'red': "Rosso",
'yellow': "Giallo",
'blue': "Blu",
'green': "Verde",
'violet': "Viola",
'black': "Nero",
'white': "Bianco",
'add_color': "Aggiungi Colore",
'result': "Risultato",
'delete': "Elimina",
'zoom_in': "Ingrandisci",
'zoom_out': "Rimpicciolisci",
'clear': "Pulisci",
'no_image': "Nessuna immagine caricata",
'recipe_not_available': "Seleziona un colore per vedere la ricetta di miscelazione",
'magnifier_title': "Lente d'ingrandimento",
'selected_pixel': "Pixel:",
'zoom': "Zoom: 10x",
'image': "Immagine",
'custom_mix': "Miscelazione Personalizzata",
'support_project': "Supporta il Progetto",
'color_harmony': "Armonia dei Colori",
'enter_hex': "Inserisci colore HEX",
'cut': "Taglia",
'copy': "Copia",
'paste': "Incolla",
'select_all': "Seleziona tutto",
'current_lang_name': "Italiano"
},
'pt': {
'title': "MixLab - Seletor e Misturador de Cores",
'upload_image': "Carregar Imagem",
'save_image': "Salvar Imagem",
'select_color': "Cor Selecionada",
'color_recipe': "Receita de Cor",
'manual_mix': "Mistura Manual",
'color_palette': "Paleta de Cores",
'parts': "partes",
'percentage': "por cento",
'click_to_upload': "Clique para carregar uma imagem",
'red': "Vermelho",
'yellow': "Amarelo",
'blue': "Azul",
'green': "Verde",
'violet': "Violeta",
'black': "Preto",
'white': "Branco",
'add_color': "Adicionar Cor",
'result': "Resultado",
'delete': "Excluir",
'zoom_in': "Ampliar",
'zoom_out': "Reduzir",
'clear': "Limpar",
'no_image': "Nenhuma imagem carregada",
'recipe_not_available': "Selecione uma cor para ver a receita de mistura",
'magnifier_title': "Lupa",
'selected_pixel': "Pixel:",
'zoom': "Zoom: 10x",
'image': "Imagem",
'custom_mix': "Mistura Personalizada",
'support_project': "Apoiar o Projeto",
'color_harmony': "Harmonia de Cores",
'enter_hex': "Digite a cor HEX",
'cut': "Recortar",
'copy': "Copiar",
'paste': "Colar",
'select_all': "Selecionar tudo",
'current_lang_name': "Português"
},
'ar': {
'title': "MixLab - قارئ الألوان وخلاطها",
'upload_image': "تحميل الصورة",
'save_image': "حفظ الصورة",
'select_color': "اللون المحدد",
'color_recipe': "وصفة اللون",
'manual_mix': "الخلط اليدوي",
'color_palette': "لوحة الألوан",
'parts': "أجزاء",
'percentage': "بالمئة",
'click_to_upload': "انقر لتحميل صورة",
'red': "أحمر",
'yellow': "أصفر",
'blue': "أزرق",
'green': "أخضر",
'violet': "بنفسجي",
'black': "أسود",
'white': "أبيض",
'add_color': "إضافة لون",
'result': "النتيجة",
'delete': "حذف",
'zoom_in': "تكبير",
'zoom_out': "تصغير",
'clear': "مسح",
'no_image': "لم يتم تحميل صورة",
'recipe_not_available': "اختر لونًا لرؤية وصفة الخلط",
'magnifier_title': "عدسة مكبرة",
'selected_pixel': "بكسل:",
'zoom': "التكبير: 10x",
'image': "صورة",
'custom_mix': "خلط مخصص",
'support_project': "دعم المشروع",
'color_harmony': "تناسق الألوان",
'enter_hex': "أدخل لون HEX",
'cut': "قص",
'copy': "نسخ",
'paste': "لصق",
'select_all': "تحديد الكل",
'current_lang_name': "العربية"
},
'zh': {
'title': "MixLab - 颜色选择器与混合器",
'upload_image': "上传图片",
'save_image': "保存图片",
'select_color': "选定颜色",
'color_recipe': "颜色配方",
'manual_mix': "手动混合",
'color_palette': "调色板",
'parts': "部分",
'percentage': "百分比",
'click_to_upload': "点击上传图片",
'red': "红色",
'yellow': "黄色",
'blue': "蓝色",
'green': "绿色",
'violet': "紫色",
'black': "黑色",
'white': "白色",
'add_color': "添加颜色",
'result': "结果",
'delete': "删除",
'zoom_in': "放大",
'zoom_out': "缩小",
'clear': "清除",
'no_image': "未加载图片",
'recipe_not_available': "选择颜色以查看混合配方",
'magnifier_title': "放大镜",
'selected_pixel': "像素:",
'zoom': "缩放: 10x",
'image': "图片",
'custom_mix': "自定义混合",
'support_project': "支持项目",
'color_harmony': "色彩和谐",
'enter_hex': "输入HEX颜色",
'cut': "剪切",
'copy': "复制",
'paste': "粘贴",
'select_all': "全选",
'current_lang_name': "中文"
},
'ja': {
'title': "MixLab - カラーピッカーとミキサー",
'upload_image': "画像をアップロード",
'save_image': "画像を保存",
'select_color': "選択した色",
'color_recipe': "カラーレシピ",
'manual_mix': "手動混合",
'color_palette': "カラーパレット",
'parts': "部",
'percentage': "パーセント",
'click_to_upload': "画像をアップロードするにはクリック",
'red': "赤",
'yellow': "黄",
'blue': "青",
'green': "緑",
'violet': "紫",
'black': "黒",
'white': "白",
'add_color': "色を追加",
'result': "結果",
'delete': "削除",
'zoom_in': "拡大",
'zoom_out': "縮小",
'clear': "クリア",
'no_image': "画像が読み込まれていません",
'recipe_not_available': "混合レシピを見るには色を選択してください",
'magnifier_title': "拡大鏡",
'selected_pixel': "ピクセル:",
'zoom': "ズーム: 10x",
'image': "画像",
'custom_mix': "カスタム混合",
'support_project': "プロジェクトをサポート",
'color_harmony': "カラーハーモニー",
'enter_hex': "HEXカラーを入力",
'cut': "切り取り",
'copy': "コピー",
'paste': "貼り付け",
'select_all': "すべて選択",
'current_lang_name': "日本語"
},
'pl': {
'title': "MixLab - Pipeta i Mieszacz Kolorów",
'upload_image': "Załaduj Obraz",
'save_image': "Zapisz Obraz",
'select_color': "Wybrany Kolor",
'color_recipe': "Przepis na Kolor",
'manual_mix': "Mieszanie Ręczne",
'color_palette': "Paleta Kolorów",
'parts': "części",
'percentage': "procent",
'click_to_upload': "Kliknij, aby załadować obraz",
'red': "Czerwony",
'yellow': "Żółty",
'blue': "Niebieski",
'green': "Zielony",
'violet': "Fioletowy",
'black': "Czarny",
'white': "Biały",
'add_color': "Dodaj Kolor",
'result': "Wynik",
'delete': "Usuń",
'zoom_in': "Powiększ",
'zoom_out': "Pomniejsz",
'clear': "Wyczyść",
'no_image': "Nie załadowano obrazu",
'recipe_not_available': "Wybierz kolor, aby zobaczyć przepis na mieszankę",
'magnifier_title': "Lupa",
'selected_pixel': "Piksel:",
'zoom': "Powiększenie: 10x",
'image': "Obraz",
'custom_mix': "Mieszanka Niestandardowa",
'support_project': "Wesprzyj Projekt",
'color_harmony': "Harmonia Kolorów",
'enter_hex': "Wpisz kolor HEX",
'cut': "Wytnij",
'copy': "Kopiuj",
'paste': "Wklej",
'select_all': "Zaznacz wszystko",
'current_lang_name': "Polski"
},
'tr': {
'title': "MixLab - Renk Seçici ve Karıştırıcı",
'upload_image': "Resim Yükle",
'save_image': "Resmi Kaydet",
'select_color': "Seçilen Renk",
'color_recipe': "Renk Tarifi",
'manual_mix': "Manuel Karıştırma",
'color_palette': "Renk Paleti",
'parts': "kısım",
'percentage': "yüzde",
'click_to_upload': "Resim yüklemek için tıklayın",
'red': "Kırmızı",
'yellow': "Sarı",
'blue': "Mavi",
'green': "Yeşil",
'violet': "Menekşe",
'black': "Siyah",
'white': "Beyaz",
'add_color': "Renk Ekle",
'result': "Sonuç",
'delete': "Sil",
'zoom_in': "Yakınlaştır",
'zoom_out': "Uzaklaştır",
'clear': "Temizle",
'no_image': "Resim yüklenmedi",
'recipe_not_available': "Karışım tarifini görmek için bir renk seçin",
'magnifier_title': "Büyüteç",
'selected_pixel': "Piksel:",
'zoom': "Yakınlaştırma: 10x",
'image': "Resim",
'custom_mix': "Özel Karışım",
'support_project': "Projeyi Destekleyin",
'color_harmony': "Renk Uyumu",
'enter_hex': "HEX renk girin",
'cut': "Kes",
'copy': "Kopyala",
'paste': "Yapıştır",
'select_all': "Tümünü seç",
'current_lang_name': "Türkçe"
}
}

# === Глобальные переменные ===
image_path: Optional[str] = None
original_image: Optional[Image.Image] = None
tk_image: Optional[ImageTk.PhotoImage] = None
selected_color: str = "#000000"
current_recipe: Optional[Dict] = None
language: str = "en"
manual_colors: List[Dict] = [{"color": "#FF0000", "parts": 1}, {"color": "#0000FF", "parts": 1}]
manual_result: str = "#800080"
zoom: float = 1.0
t: Dict = translations[language]
active_color: str = "#FF0000"

# === Вспомогательные функции ===
def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r: float, g: float, b: float) -> str:
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """RGB to HSV with h in [0, 360), s in [0, 1], v in [0, 1]. Safe for grayscale."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val
    
    # Hue calculation (0-360 degrees) — ЗАЩИТА ОТ ДЕЛЕНИЯ НА НОЛЬ
    if delta == 0:
        h = 0.0
    elif max_val == r:
        h = 60 * (((g - b) / delta) % 6)
    elif max_val == g:
        h = 60 * (((b - r) / delta) + 2)
    else:  # max_val == b
        h = 60 * (((r - g) / delta) + 4)
    
    h = h % 360  # Нормализация в диапазон 0-360
    
    # Saturation
    s = 0.0 if max_val == 0 else delta / max_val
    
    # Value
    v = max_val
    
    return h, s, v


def calculate_recipe(hex_color: str, r: int, g: int, b: int) -> List[Dict]:
    """
    RYB mixing with STRICT pigment priorities (fixes #0033A0, #FFD800, #E60000)
    Order: 1) Pure pigments → 2) Neutrals → 3) Super dark/light → 4) Sectors
    """
    h, s, v = rgb_to_hsv(r, g, b)
    
    # === 1. ЧИСТЫЕ ПИГМЕНТЫ (ПРИОРИТЕТ ПЕРВЫЙ! СТРОГИЕ ПОРОГИ) ===
    # ЖЁЛТЫЙ: кадмий-жёлтый (#FFD800, #FFFF00, #FFFF31)
    if 35 <= h <= 105 and s > 0.7 and min(r, g) > 210:
        return [{"color": "yellow", "parts": 10, "percentage": 100}]
    
    # КРАСНЫЙ: кадмий-красный (#E60000, #FF0000)
    if ((0 <= h <= 25) or (335 <= h <= 360)) and s > 0.8 and r > 200:
        return [{"color": "red", "parts": 10, "percentage": 100}]
    
    # СИНИЙ: ультрамарин (#0033A0) и кобальт (#0000FF)
    if 210 <= h <= 260 and s > 0.8 and b > 140:
        return [{"color": "blue", "parts": 10, "percentage": 100}]
    
    # === 2. АБСОЛЮТНО ЧЁРНЫЙ/БЕЛЫЙ ===
    if max(r, g, b) <= 20:
        return [{"color": "black", "parts": 10, "percentage": 100}]
    if min(r, g, b) >= 240:
        return [{"color": "white", "parts": 10, "percentage": 100}]
    
    # === 3. НЕЙТРАЛЬНЫЕ (серые тона) — ИСПРАВЛЕНО ДЛЯ #212121 ===
    if s < 0.15:
        # Для тёмно-серого (#212121 ≈ 13% яркости) — 8 частей чёрного + 2 белого
        if v < 0.2:  # Очень тёмные серые (<50)
            black_parts = 8
            white_parts = 2
        else:
            black_parts = max(1, min(9, round((1 - v) * 10)))
            white_parts = 10 - black_parts
        return [
            {"color": "white", "parts": white_parts, "percentage": round(white_parts * 10)},
            {"color": "black", "parts": black_parts, "percentage": round(black_parts * 10)}
        ]
    
    # === 4. СВЕРХТЁМНЫЕ (но не чёрные) ===
    if max(r, g, b) <= 40:
        return [
            {"color": "black", "parts": 8, "percentage": 80},
            {"color": "white", "parts": 2, "percentage": 20}
        ]
    
    # === 5. РЕАЛИСТИЧНОЕ СМЕШИВАНИЕ ПО СЕКТОРАМ ===
    red = yellow = blue = white = black = 0.0
    
    if 0 <= h < 25:      # Красный
        red = 0.95
        yellow = 0.05
    elif 25 <= h < 45:   # Красно-оранжевый
        pos = (h - 25) / 20
        red = 0.85 - pos * 0.35
        yellow = 0.15 + pos * 0.35
    elif 45 <= h < 75:   # Жёлто-оранжевый
        pos = (h - 45) / 30
        red = 0.5 - pos * 0.3
        yellow = 0.5 + pos * 0.3
    elif 75 <= h < 105:  # Жёлтый
        yellow = 0.95
        red = 0.05
    elif 105 <= h < 135: # Жёлто-зелёный
        pos = (h - 105) / 30
        yellow = 0.7 - pos * 0.3
        blue = 0.3 + pos * 0.3
    elif 135 <= h < 175: # Зелёный (землистый!)
        yellow = 0.4
        blue = 0.6
    elif 175 <= h < 215: # Бирюзовый
        blue = 0.85
        yellow = 0.15
    elif 215 <= h < 245: # Сине-бирюзовый
        pos = (h - 215) / 30
        blue = 0.8 - pos * 0.2
        red = 0.2 + pos * 0.1
    elif 245 <= h < 295: # Синий
        blue = 0.95
        red = 0.05
    elif 295 <= h < 335: # Фиолетовый
        pos = (h - 295) / 40
        blue = 0.6 - pos * 0.25
        red = 0.4 + pos * 0.25
    else:  # 335-360: Красно-фиолетовый
        pos = (h - 335) / 25
        red = 0.85 + pos * 0.15
        blue = 0.15 - pos * 0.1
    
    # === 6. ДОБАВЛЕНИЕ БЕЛОГО/ЧЁРНОГО (ТОЛЬКО ПО ПРАВИЛАМ) ===
    # Белый ТОЛЬКО для пастелей (низкая насыщенность + высокая яркость)
    if v > 0.85 and s < 0.7:
        white = (v - 0.75) * 1.5
    
    # Чёрный для тёмных тонов
    elif v < 0.35 and s > 0.2:
        black = (0.45 - v) * 2.0
    
    # === 7. НОРМАЛИЗАЦИЯ ДО 10 ЧАСТЕЙ ===
    color_sum = red + yellow + blue
    if color_sum > 0:
        red /= color_sum
        yellow /= color_sum
        blue /= color_sum
    
    total = red + yellow + blue + white + black
    if total == 0:
        total = 1.0
    
    # Расчёт процентов
    r_pct = (red / total) * 100
    y_pct = (yellow / total) * 100
    b_pct = (blue / total) * 100
    w_pct = (white / total) * 100
    k_pct = (black / total) * 100
    
    # Формирование компонентов (>4%)
    components = []
    if y_pct > 4: components.append({"color": "yellow", "percentage": y_pct, "parts": 0})
    if r_pct > 4: components.append({"color": "red", "percentage": r_pct, "parts": 0})
    if b_pct > 4: components.append({"color": "blue", "percentage": b_pct, "parts": 0})
    if w_pct > 4: components.append({"color": "white", "percentage": w_pct, "parts": 0})
    if k_pct > 4: components.append({"color": "black", "percentage": k_pct, "parts": 0})
    
    # Сортировка по убыванию
    components.sort(key=lambda x: x["percentage"], reverse=True)
    
    # Максимум 3 компонента
    if len(components) > 3:
        components = components[:3]
        total_pct = sum(c["percentage"] for c in components)
        for c in components:
            c["percentage"] = (c["percentage"] / total_pct) * 100
    
    # Распределение 10 частей
    if components:
        total_pct = sum(c["percentage"] for c in components)
        for c in components:
            c["parts"] = max(1, round((c["percentage"] / total_pct) * 10))
        
        # Коррекция суммы до 10
        sum_parts = sum(c["parts"] for c in components)
        diff = 10 - sum_parts
        if diff != 0:
            components[0]["parts"] = max(1, components[0]["parts"] + diff)
        
        # Финальные проценты
        sum_parts = sum(c["parts"] for c in components)
        for c in components:
            c["percentage"] = round((c["parts"] / sum_parts) * 100)
    
    return components

# === Функция для работы с путями ресурсов ===
def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    full_path = os.path.join(base_path, relative_path)
    if os.path.exists(full_path):
        return full_path
    # Fallback для режима разработки
    dev_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    if os.path.exists(dev_path):
        return dev_path
    return relative_path

# === Функция загрузки QR-кода ===
def ensure_qr_exists() -> str:
    qr_path = resource_path("assets/qr-donate.png")
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    if not os.path.exists(qr_path):
        try:
            urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/milleran41/MixLab/main/assets/qr-donate.png",
                qr_path
            )
        except Exception as e:
            print(f"Failed to download QR code: {e}")
            # Создаём заглушку
            try:
                from PIL import Image, ImageDraw
                img = Image.new('RGB', (120, 120), color='white')
                draw = ImageDraw.Draw(img)
                draw.text((10, 50), "QR not available", fill='black')
                img.save(qr_path)
            except:
                pass
    return qr_path

# === Функции интерфейса ===
def load_image() -> None:
    global image_path, original_image, tk_image, zoom
    
    # Сбрасываем зум
    zoom = 1.0
    zoom_label.config(text="100%")  # Обновляем метку напрямую
    
    # Выбираем файл
    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")]
    )
    if not path:
        return
    
    image_path = path
    try:
        original_image = Image.open(path).convert("RGB")
        display_image()
    except Exception as e:
        messagebox.showerror(t['title'], f"Failed to load image:\n{str(e)}")

def display_image() -> None:
    global tk_image
    if original_image is None:
        canvas.delete("all")
        canvas.config(scrollregion=(0, 0, 400, 300))
        canvas.create_text(200, 150, text=t['click_to_upload'], fill="gray", font=("Arial", 14))
        return
    w, h = original_image.size
    new_size = (int(w * zoom), int(h * zoom))
    resized = original_image.resize(new_size, Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.config(scrollregion=(0, 0, new_size[0], new_size[1]))

def save_image() -> None:
    if original_image is None:
        messagebox.showinfo(t['title'], t['no_image'])
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")]
    )
    if path:
        try:
            original_image.save(path)
            messagebox.showinfo(t['title'], "Image saved successfully!")
        except Exception as e:
            messagebox.showerror(t['title'], f"Failed to save image:\n{str(e)}")

def zoom_in() -> None:
    global zoom
    zoom = min(5.0, zoom * 1.2)
    display_image()
    zoom_label.config(text=f"{round(zoom * 100)}%")  # Прямое обновление метки

def zoom_out() -> None:
    global zoom
    zoom = max(0.2, zoom / 1.2)
    display_image()
    zoom_label.config(text=f"{round(zoom * 100)}%")  # Прямое обновление метки

def clear_image() -> None:
    global image_path, original_image, tk_image, current_recipe, selected_color, zoom
    image_path = None
    original_image = None
    tk_image = None
    zoom = 1.0  # Сбрасываем зум
    zoom_label.config(text="100%")  # Обновляем метку
    
    # Очищаем холст
    canvas.delete("all")
    canvas.config(scrollregion=(0, 0, 400, 300))
    canvas.create_text(200, 150, text=t['click_to_upload'], fill="gray", font=("Arial", 14))
    
    # Сбрасываем цвет и рецепт
    selected_color = "#000000"
    color_display.config(bg=selected_color)
    color_hex_label.config(text=selected_color.upper())
    current_recipe = None
    display_recipe()

# === Гармония цветов ===
def open_harmony() -> None:
    """Открывает инструмент гармонии цветов в браузере"""
    html_path = resource_path("assets/harmony.html")
    # Передаём язык и цвет через hash — работает с file:/// на всех браузерах
    color_param = selected_color.lstrip('#')
    url = f"file:///{html_path.replace(os.sep, '/')}#lang={language}&color={color_param}"
    webbrowser.open(url)

# === Пипетка + Лупа ===
def show_magnifier(x: int, y: int) -> None:
    if original_image is None:
        return
    # Обеспечиваем, что координаты в пределах изображения
    x = max(0, min(x, original_image.width - 1))
    y = max(0, min(y, original_image.height - 1))
    size = 7
    left = max(0, x - size//2)
    right = min(original_image.width, x + size//2 + 1)
    top = max(0, y - size//2)
    bottom = min(original_image.height, y + size//2 + 1)
    cropped = original_image.crop((left, top, right, bottom))
    magnified = cropped.resize((70, 70), Image.Resampling.NEAREST)
    # Создаём окно лупы
    win = tk.Toplevel(root)
    win.title(t['magnifier_title'])
    win.resizable(False, False)
    win.overrideredirect(True)  # Убираем рамку окна
    # Позиционируем рядом с курсором
    screen_x = root.winfo_pointerx() + 20
    screen_y = root.winfo_pointery() + 20
    win.geometry(f"+{screen_x}+{screen_y}")
    # Контент лупы
    frame = ttk.Frame(win, padding=5)
    frame.pack()
    tk_img = ImageTk.PhotoImage(magnified)
    label = tk.Label(frame, image=tk_img, borderwidth=2, relief="solid")
    label.pack(pady=5)
    label.image = tk_img
    # Цветной индикатор выбранного пикселя
    r, g, b = original_image.getpixel((x, y))
    color_indicator = tk.Frame(frame, bg=rgb_to_hex(r, g, b), width=40, height=20, relief="solid", bd=1)
    color_indicator.pack(pady=5)
    # Автозакрытие через 1.5 секунды
    win.after(1500, win.destroy)

def on_canvas_click(event: tk.Event) -> None:
    if original_image is None:
        return
    # Корректное преобразование координат с учётом скролла и зума
    canvas_x = canvas.canvasx(event.x)
    canvas_y = canvas.canvasy(event.y)
    x = int(round(canvas_x / zoom))
    y = int(round(canvas_y / zoom))
    # Проверка границ
    if x < 0 or y < 0 or x >= original_image.width or y >= original_image.height:
        return
    # Показываем лупу
    show_magnifier(x, y)
    # Получаем цвет
    r, g, b = original_image.getpixel((x, y))
    hex_color = rgb_to_hex(r, g, b)
    # Обновляем интерфейс
    select_color(hex_color, r, g, b)

def select_color(hex_color: str, r: Optional[int] = None, g: Optional[int] = None, b: Optional[int] = None) -> None:
    global selected_color, current_recipe, active_color
    selected_color = hex_color
    active_color = hex_color
    # Обновляем отображение выбранного цвета
    color_display.config(bg=hex_color)
    color_hex_label.config(text=hex_color.upper())
    # Синхронизируем поле ввода (без рекурсии)
    if hex_entry_var and hex_entry_var.get().strip().lstrip('#').upper() != hex_color.lstrip('#').upper():
        hex_entry_var.trace_remove("write", hex_entry_var.trace_info()[0][1])
        hex_entry_var.set(hex_color)
        hex_entry.config(foreground='black')
        hex_entry_var.trace_add("write", on_hex_input)
    # Получаем RGB если не переданы
    if r is None:
        r, g, b = hex_to_rgb(hex_color)
    # Рассчитываем рецепт
    recipe = calculate_recipe(hex_color, r, g, b)
    # Сохраняем текущий рецепт
    current_recipe = {
        "name": "custom_mix",
        "hex": hex_color,
        "rgb": f"{r}, {g}, {b}",
        "recipe": recipe
    }
    display_recipe()

# === Ручное смешивание ===
def on_hex_input(*args: Any) -> None:
    """Обрабатывает ввод HEX-кода пользователем"""
    global hex_entry_var
    raw = hex_entry_var.get().strip()
    # Нормализуем: добавляем # если нет
    if raw and not raw.startswith('#'):
        raw = '#' + raw
    # Валидируем: ровно 7 символов (#rrggbb)
    if len(raw) == 7 and all(c in '0123456789abcdefABCDEF' for c in raw[1:]):
        hex_entry.config(foreground='black')
        r, g, b = hex_to_rgb(raw)
        select_color(raw, r, g, b)
    else:
        # Неполный ввод — подсвечиваем серым, не обновляем
        hex_entry.config(foreground='gray')

def calculate_manual_mix() -> None:
    global manual_result
    total_parts = sum(c["parts"] for c in manual_colors)
    if total_parts == 0:
        return
    r = g = b = 0.0
    for c in manual_colors:
        cr, cg, cb = hex_to_rgb(c["color"])
        weight = c["parts"] / total_parts
        r += cr * weight
        g += cg * weight
        b += cb * weight
    manual_result = rgb_to_hex(r, g, b)
    result_label.config(bg=manual_result)
    result_hex_label.config(text=manual_result.upper())

def update_manual_display() -> None:
    # Очищаем фрейм
    for widget in manual_frame.winfo_children():
        widget.destroy()
    # Отображаем каждый цвет в смеси
    for i, c in enumerate(manual_colors):
        # Определяем цвет текста для читаемости
        cr, cg, cb = hex_to_rgb(c["color"])
        brightness = (cr * 299 + cg * 587 + cb * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        # Кнопка выбора цвета
        color_btn = tk.Button(
            manual_frame,
            bg=c["color"],
            width=3,
            height=1,
            relief="raised",
            cursor="hand2"
        )
        color_btn.bind("<Button-1>", lambda e, idx=i: open_pigment_picker(idx))
        color_btn.grid(row=i, column=0, padx=2, pady=2, sticky="ns")
        # Поле ввода частей
        parts_var = tk.StringVar(value=str(c["parts"]))
        def make_callback(idx: int, var: tk.StringVar) -> Callable[[str, str, str], None]:
            def callback(*args: Any) -> None:
                try:
                    value = int(var.get())
                    if value < 1:
                        value = 1
                    var.set(str(value))
                    manual_colors[idx]["parts"] = value
                    calculate_manual_mix()
                except:
                    pass
            return callback
        parts_var.trace_add("write", make_callback(i, parts_var))
        parts_entry = tk.Entry(manual_frame, textvariable=parts_var, width=4, justify="center")
        parts_entry.grid(row=i, column=1, padx=2, pady=2)
        # Проценты
        total = sum(c["parts"] for c in manual_colors)
        percent = int((c["parts"] / total) * 100) if total > 0 else 0
        percent_label = tk.Label(manual_frame, text=f"{percent}%", width=5, font=("Arial", 9))
        percent_label.grid(row=i, column=2, padx=2, pady=2)
        # Кнопка удаления
        del_btn = ttk.Button(
            manual_frame,
            text="✕",
            width=3,
            command=lambda idx=i: delete_manual_color(idx)
        )
        del_btn.grid(row=i, column=3, padx=2, pady=2)
    # Обновляем результат
    calculate_manual_mix()

def delete_manual_color(idx: int) -> None:
    if len(manual_colors) > 1:
        manual_colors.pop(idx)
        update_manual_display()

def open_pigment_picker(idx: int) -> None:
    """Выбор ТОЛЬКО из 5 чистых пигментов (без системного пикера!)"""
    picker = tk.Toplevel(root)
    picker.title(t['color_palette'])
    picker.resizable(False, False)
    picker.transient(root)
    picker.grab_set()
    
    # Центрируем
    root.update_idletasks()
    x = root.winfo_x() + root.winfo_width()//2 - 150
    y = root.winfo_y() + root.winfo_height()//2 - 120
    picker.geometry(f"+{x}+{y}")
    
    pigments = [
        {"name": "red", "hex": "#E60000"},
        {"name": "yellow", "hex": "#FFD800"},
        {"name": "blue", "hex": "#0033A0"},
        {"name": "white", "hex": "#FFFFFF"},
        {"name": "black", "hex": "#000000"}
    ]
    
    ttk.Label(picker, text=t['select_color'], font=("Arial", 11, "bold"), pady=10).pack()
    
    grid_frame = ttk.Frame(picker)
    grid_frame.pack(padx=15, pady=10)
    
    for i, pigment in enumerate(pigments):
        r, g, b = hex_to_rgb(pigment["hex"])
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        
        btn = tk.Button(
            grid_frame,
            text=t[pigment["name"]],
            bg=pigment["hex"],
            fg=text_color,
            width=12,
            height=2,
            font=("Arial", 9, "bold"),
            relief="raised",
            command=lambda p=pigment, idx=idx: [
                setattr(manual_colors[idx], 'color', p["hex"]),
                update_manual_display(),
                picker.destroy()
            ]
        )
        if pigment["name"] == "white":
            btn.config(highlightbackground="gray", highlightthickness=1)
        btn.grid(row=i//2, column=i%2, padx=5, pady=5)
    
    ttk.Button(picker, text=t.get('cancel', "Cancel"), command=picker.destroy).pack(pady=(10, 10))

def add_manual_color() -> None:
    manual_colors.append({"color": active_color, "parts": 1})
    update_manual_display()

# === Отображение рецепта ===
def display_recipe() -> None:
    global recipe_title
    # Очищаем фрейм рецепта (кроме заголовка)
    for widget in recipe_frame.winfo_children():
        if widget != recipe_title:
            widget.destroy()
    # Если нет рецепта - показываем подсказку
    if current_recipe is None or not current_recipe.get("recipe"):
        hint = tk.Label(
            recipe_frame,
            text=t['recipe_not_available'],
            fg="gray",
            font=("Arial", 10, "italic"),
            pady=10
        )
        hint.pack()
        return
    # Отображаем информацию о цвете
    info_frame = ttk.Frame(recipe_frame)
    info_frame.pack(anchor="w", pady=(0, 8))
    tk.Label(info_frame, text=f"HEX: {current_recipe['hex'].upper()}", font=("Courier", 10)).pack(anchor="w")
    tk.Label(info_frame, text=f"RGB: {current_recipe['rgb']}", font=("Courier", 10)).pack(anchor="w")
    # Отображаем компоненты рецепта
    for item in current_recipe["recipe"]:
        color_name = t.get(item["color"], item["color"].capitalize())
        color_hex = {
            "red": "#D32F2F",
            "yellow": "#FBC02D",
            "blue": "#1976D2",
            "green": "#388E3C",
            "violet": "#7B1FA2",
            "black": "#212121",
            "white": "#FFFFFF"
        }.get(item["color"], "#666666")
        # Создаём компонент рецепта с цветной полосой
        comp_frame = ttk.Frame(recipe_frame)
        comp_frame.pack(fill="x", pady=3)
        # Цветная индикация (с белым контуром для белого цвета)
        color_bar = tk.Frame(comp_frame, bg=color_hex, width=18, height=18, relief="flat")
        if item["color"] == "white":
            color_bar.config(highlightbackground="gray", highlightthickness=1)
        color_bar.pack(side="left", padx=(0, 8))
        color_bar.pack_propagate(False)
        # Текст
        label = tk.Label(
            comp_frame,
            text=f"{color_name}: {item['parts']} {t['parts']} ({item['percentage']}%)",
            font=("Arial", 10)
        )
        label.pack(side="left")

# === Создание палитры в заданном фрейме ===
def create_palette_in_frame(parent: ttk.Frame) -> None:
    """Палитра ТОЛЬКО с 5 чистыми пигментами (как на реальной художественной палитре)"""
    for widget in parent.winfo_children():
        widget.destroy()
    
    # 5 ЧИСТЫХ ПИГМЕНТОВ
    palette_colors = [
        {"name": "red", "hex": "#E60000"},      # Кадмий-красный
        {"name": "yellow", "hex": "#FFD800"},   # Кадмий-жёлтый
        {"name": "blue", "hex": "#0033A0"},     # Ультрамарин
        {"name": "white", "hex": "#FFFFFF"},    # Белила
        {"name": "black", "hex": "#000000"}     # Чёрная кость
    ]
    
    for i, color in enumerate(palette_colors):
        cname = t[color["name"]]
        r, g, b = hex_to_rgb(color["hex"])
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        
        btn = tk.Button(
            parent,
            text=cname,
            bg=color["hex"],
            fg=text_color,
            width=10,
            height=1,
            relief="raised",
            font=("Arial", 9, "bold"),
            cursor="hand2",
            command=lambda c=color: select_color(c["hex"], *hex_to_rgb(c["hex"]))
        )
        if color["name"] == "white":
            btn.config(highlightbackground="gray", highlightthickness=1)
        btn.grid(row=i//2, column=i%2, padx=4, pady=4, sticky="ew")
    
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(1, weight=1)

# === Языки ===
def change_language(lang: str) -> None:
    global language, t
    language = lang
    t = translations[lang]
    update_ui_texts()

def update_ui_texts() -> None:
    global lang_button
    # Обновляем заголовок окна
    root.title(t['title'])
    # Обновляем кнопки верхней панели
    upload_btn.config(text=t['upload_image'])
    save_btn.config(text=t['save_image'])
    zoom_in_btn.config(text=t['zoom_in'])
    zoom_out_btn.config(text=t['zoom_out'])
    clear_btn.config(text=t['clear'])
    if harmony_btn:
        harmony_btn.config(text=t['color_harmony'])
    if hex_hint_label:
        hex_hint_label.config(text=t['enter_hex'])
    # Обновляем фреймы
    left_frame.config(text=t['image'])
    color_frame.config(text=t['select_color'])
    recipe_frame.config(text=t['color_recipe'])
    manual_frame_outer.config(text=t['manual_mix'])
    palette_support_frame.config(text=t['color_palette'])
    # Обновляем метки
    if color_label:
        color_label.config(text=f"{t['select_color']}:")
    if result_label_text:
        result_label_text.config(text=t['result'])
    zoom_label.config(text=f"{round(zoom * 100)}%")
    if add_btn:
        add_btn.config(text=t['add_color'])
    # Обновляем палитру
    create_palette_in_frame(palette_inner)
    # Обновляем рецепт
    display_recipe()
    # Обновляем ручное смешивание
    update_manual_display()
    # Обновляем кнопку языка
    lang_button.config(text=t['current_lang_name'])
    # Обновляем кнопку поддержки
    for child in support_frame.winfo_children():
        if isinstance(child, ttk.Button):
            child.config(text=t['support_project'])
    # Обновляем отображение изображения (для текста-заглушки)
    if original_image is None:
        display_image()

# === GUI (главное окно) ===
def create_ui() -> tk.Tk:
    global root, canvas, color_display, color_hex_label, recipe_frame, recipe_title
    global manual_frame, result_label, result_hex_label, palette_inner
    global palette_support_frame, zoom_label, lang_button, support_frame
    global upload_btn, save_btn, zoom_in_btn, zoom_out_btn, clear_btn, harmony_btn
    global left_frame, color_frame, manual_frame_outer, result_label_text, color_label, add_btn
    global image_on_canvas, current_image, zoom_level, zoom_center
    global hex_entry, hex_entry_var, hex_hint_label
    
    root = tk.Tk()
    root.title(t['title'])
    root.geometry("1200x800")
    root.minsize(1000, 700)
    
    # Иконка приложения
    try:
        icon_path = resource_path("assets/icon.ico")
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Icon not loaded: {e}")
    
    # Стили
    style = ttk.Style()
    style.configure("Bold.TLabelframe.Label", font=("Arial", 10, "bold"))
    
    # Главный фрейм
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Настройка колонок: 60% изображение, 40% панель инструментов
    main_frame.grid_columnconfigure(0, weight=3)
    main_frame.grid_columnconfigure(1, weight=2)
    main_frame.grid_rowconfigure(1, weight=1)
    
    # === Верхняя панель ===
    top_frame = ttk.Frame(main_frame)
    top_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 8))
    
    # Кнопки управления изображением
    upload_btn = ttk.Button(top_frame, text=t['upload_image'], command=load_image)
    upload_btn.pack(side="left", padx=2)
    
    save_btn = ttk.Button(top_frame, text=t['save_image'], command=save_image)
    save_btn.pack(side="left", padx=2)
    
    zoom_out_btn = ttk.Button(top_frame, text=t['zoom_out'], command=zoom_out)
    zoom_out_btn.pack(side="left", padx=2)
    
    zoom_in_btn = ttk.Button(top_frame, text=t['zoom_in'], command=zoom_in)
    zoom_in_btn.pack(side="left", padx=2)
    
    zoom_label = ttk.Label(top_frame, text="100%", width=5, anchor="center")
    zoom_label.pack(side="left", padx=5)
    
    harmony_btn = ttk.Button(top_frame, text=t['color_harmony'], command=open_harmony)
    harmony_btn.pack(side="left", padx=2)

    clear_btn = ttk.Button(top_frame, text=t['clear'], command=clear_image)
    clear_btn.pack(side="left", padx=2)
    
    # Кнопка выбора языка (справа)
    lang_button = ttk.Menubutton(top_frame, text=t['current_lang_name'], direction="below")
    lang_menu = tk.Menu(lang_button, tearoff=0)
    for lang_code in ['en', 'ru', 'es', 'de', 'fr', 'it', 'pt', 'ar', 'zh', 'ja', 'pl', 'tr']:
        lang_menu.add_command(
            label=translations[lang_code]['current_lang_name'],
            command=lambda l=lang_code: change_language(l)
        )
    lang_button["menu"] = lang_menu
    lang_button.pack(side="right", padx=2)
    
    # === Левая панель: изображение ===
    left_frame = ttk.LabelFrame(main_frame, text=t['image'], padding="5", style="Bold.TLabelframe")
    left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 8))
    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)
    
    # Холст для изображения
    canvas_frame = ttk.Frame(left_frame)
    canvas_frame.grid(row=0, column=0, sticky="nsew")
    
    canvas = tk.Canvas(canvas_frame, bg="#f0f0f0", cursor="crosshair")
    canvas.pack(side="left", fill="both", expand=True)
    
    # Скроллбары
    v_scroll = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    v_scroll.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=v_scroll.set)
    
    h_scroll = ttk.Scrollbar(left_frame, orient="horizontal", command=canvas.xview)
    h_scroll.grid(row=1, column=0, sticky="ew")
    canvas.configure(xscrollcommand=h_scroll.set)
    
    # Привязка клика (только если функция существует, иначе временно отключаем)
    try:
        canvas.bind("<Button-1>", on_canvas_click)
    except NameError:
        # Функция on_canvas_click не определена — временно отключаем пипетку
        pass

    # Изначально показываем подсказку
    canvas.delete("all")  # Очищаем холст перед добавлением подсказки
    canvas.create_text(200, 150, text=t['click_to_upload'], fill="gray", font=("Arial", 14))
    canvas.config(scrollregion=(0, 0, 400, 300))
    
    # Инициализация глобальных переменных изображения
    global current_image, image_on_canvas, zoom_level, zoom_center
    image_on_canvas = None
    current_image = None
    zoom_level = 1.0
    zoom_center = (0, 0)
    
    # === Правая панель: инструменты ===
    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=1, column=1, sticky="nsew")
    right_frame.grid_rowconfigure(0, weight=0)  # Выбранный цвет
    right_frame.grid_rowconfigure(1, weight=1)  # Рецепт (растягивается)
    right_frame.grid_rowconfigure(2, weight=0)  # Ручное смешивание
    right_frame.grid_rowconfigure(3, weight=0)  # Палитра + поддержка
    right_frame.grid_columnconfigure(0, weight=1)
    
    # --- Выбранный цвет ---
    color_frame = ttk.LabelFrame(right_frame, text=t['select_color'], padding="8", style="Bold.TLabelframe")
    color_frame.grid(row=0, column=0, sticky="ew", pady=(0, 8))
    color_frame.grid_columnconfigure(1, weight=1)
    
    color_label = ttk.Label(color_frame, text=f"{t['select_color']}:", font=("Arial", 10, "bold"))
    color_label.grid(row=0, column=0, sticky="w", padx=(0, 10))
    
    color_display = tk.Frame(color_frame, bg=selected_color, width=40, height=40, relief="solid", bd=1)
    color_display.grid(row=0, column=1, padx=5)
    color_display.pack_propagate(False)
    
    color_hex_label = ttk.Label(color_frame, text=selected_color.upper(), font=("Courier", 11, "bold"))
    color_hex_label.grid(row=0, column=2, padx=5)
    
    # Поле ввода HEX (вторая строка)
    hex_entry_var = tk.StringVar(value=selected_color)
    hex_entry_var.trace_add("write", on_hex_input)
    hex_entry = tk.Entry(color_frame, textvariable=hex_entry_var, width=10, font=("Courier", 10), justify="center")
    hex_entry.grid(row=1, column=1, columnspan=2, pady=(8, 0), sticky="w")
    
    # Контекстное меню: копировать / вставить / выделить всё
    hex_context_menu = tk.Menu(hex_entry, tearoff=0)
    hex_context_menu.add_command(label="✂ " + t['cut'],   command=lambda: hex_entry.event_generate("<<Cut>>"))
    hex_context_menu.add_command(label="⎘ " + t['copy'],  command=lambda: hex_entry.event_generate("<<Copy>>"))
    hex_context_menu.add_command(label="⎗ " + t['paste'], command=lambda: hex_entry.event_generate("<<Paste>>"))
    hex_context_menu.add_separator()
    hex_context_menu.add_command(label=t['select_all'],    command=lambda: hex_entry.select_range(0, "end"))

    def show_hex_context_menu(event: tk.Event) -> None:
        # Обновляем метки под текущий язык перед показом
        hex_context_menu.entryconfig(0, label="✂ " + t['cut'])
        hex_context_menu.entryconfig(1, label="⎘ " + t['copy'])
        hex_context_menu.entryconfig(2, label="⎗ " + t['paste'])
        hex_context_menu.entryconfig(4, label=t['select_all'])
        hex_context_menu.tk_popup(event.x_root, event.y_root)

    hex_entry.bind("<Button-3>", show_hex_context_menu)
    
    hex_hint = ttk.Label(color_frame, text=t['enter_hex'], font=("Arial", 8), foreground="gray")
    hex_hint.grid(row=1, column=0, pady=(8, 0), sticky="w")
    hex_hint_label = hex_hint
    
    # --- Рецепт смешивания ---
    recipe_frame = ttk.LabelFrame(right_frame, text=t['color_recipe'], padding="8", style="Bold.TLabelframe")
    recipe_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 8))
    recipe_frame.grid_columnconfigure(0, weight=1)
    recipe_frame.grid_rowconfigure(0, weight=1)
    
    recipe_title = tk.Label(recipe_frame, text=t['color_recipe'], font=("Arial", 11, "bold"), anchor="w")
    recipe_title.pack(anchor="w", pady=(0, 8))
    
    # Изначально показываем подсказку
    hint = tk.Label(
        recipe_frame,
        text=t['recipe_not_available'],
        fg="gray",
        font=("Arial", 10, "italic"),
        pady=20
    )
    hint.pack()
    
    # --- Ручное смешивание ---
    manual_frame_outer = ttk.LabelFrame(right_frame, text=t['manual_mix'], padding="8", style="Bold.TLabelframe")
    manual_frame_outer.grid(row=2, column=0, sticky="ew", pady=(0, 8))
    
    # Кнопка добавления цвета
    add_btn = ttk.Button(manual_frame_outer, text=t['add_color'], command=add_manual_color)
    add_btn.pack(anchor="w", pady=(0, 8))
    
    # Фрейм для списка цветов
    manual_frame = ttk.Frame(manual_frame_outer)
    manual_frame.pack(fill="x", pady=(0, 8))
    
    # Результат смешивания
    result_frame = ttk.Frame(manual_frame_outer)
    result_frame.pack(fill="x", pady=(8, 0))
    
    result_label_text = ttk.Label(result_frame, text=f"{t['result']}:", font=("Arial", 10, "bold"))
    result_label_text.pack(side="left")
    
    result_label = tk.Frame(result_frame, bg=manual_result, width=40, height=30, relief="solid", bd=1)
    result_label.pack(side="left", padx=8)
    result_label.pack_propagate(False)
    
    result_hex_label = ttk.Label(result_frame, text=manual_result.upper(), font=("Courier", 10))
    result_hex_label.pack(side="left")
    
    # Инициализация ручного смешивания
    update_manual_display()
    
    # --- Палитра и поддержка ---
    palette_support_frame = ttk.LabelFrame(right_frame, text=t['color_palette'], padding="8", style="Bold.TLabelframe")
    palette_support_frame.grid(row=3, column=0, sticky="ew")
    palette_support_frame.grid_columnconfigure(0, weight=3)
    palette_support_frame.grid_columnconfigure(1, weight=1)
    
    # Палитра цветов
    palette_inner = ttk.Frame(palette_support_frame)
    palette_inner.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
    
    # Фрейм поддержки
    support_frame = ttk.Frame(palette_support_frame)
    support_frame.grid(row=0, column=1, sticky="nsew")
    def on_closing():
        root.quit()  # Корректно завершает mainloop
        root.destroy()  # Уничтожает все дочерние окна
        sys.exit(0)

    root.protocol("WM_DELETE_WINDOW", on_closing)    
    
    # Загрузка QR-кода в отдельном потоке
    def load_qr():
        qr_path = ensure_qr_exists()
        if os.path.exists(qr_path):
            try:
                img = Image.open(qr_path)
                img = img.resize((110, 110), Image.Resampling.LANCZOS)
                qr_photo = ImageTk.PhotoImage(img)
                # Обновление в основном потоке
                def update_ui():
                    qr_label = tk.Label(support_frame, image=qr_photo, bg="white", relief="solid", bd=1)
                    qr_label.image = qr_photo  # Сохраняем ссылку
                    qr_label.pack(pady=(0, 10))
                root.after(0, update_ui)
            except Exception as e:
                print(f"QR load error: {e}")
    
    threading.Thread(target=load_qr, daemon=True).start()
    
    # Кнопка поддержки проекта
    support_btn = ttk.Button(
        support_frame,
        text=t['support_project'],
        command=lambda: webbrowser.open("https://ko-fi.com/linkora")
    )
    support_btn.pack(fill="x", pady=(5, 0))
    
    # Создаём палитру
    create_palette_in_frame(palette_inner)
    
    return root

# === ВАЛИДАЦИЯ АЛГОРИТМА И ЗАПУСК ПРИЛОЖЕНИЯ ===
if __name__ == "__main__":
    print("🎨 Тест чистых пигментов:")
    tests = [
        ("#FFD800", 255, 216, 0, "Кадмий-жёлтый"),
        ("#E60000", 230, 0, 0, "Кадмий-красный"),
        ("#0033A0", 0, 51, 160, "Ультрамарин"),
        ("#0000FF", 0, 0, 255, "Кобальт-синий"),
        ("#212121", 33, 33, 33, "Тёмно-серый"),
    ]
    for hexc, r, g, b, name in tests:
        recipe = calculate_recipe(hexc, r, g, b)
        comps = [f"{c['color']}:{c['parts']}" for c in recipe]
        result = " + ".join(comps)
        status = "✅" if (len(recipe) == 1 and recipe[0]['parts'] == 10) else "⚠️"
        print(f"{status} {name:20} {hexc} → {result}")
    
    # ✅ ЕДИНСТВЕННЫЙ ЗАПУСК ПРИЛОЖЕНИЯ
    root = create_ui()
    root.mainloop()
    
    # Запуск графического интерфейса
    print("\nЗапуск графического интерфейса MixLab...")
    root = create_ui()
    root.mainloop()
    
    # Запуск основного интерфейса
    root = create_ui()
    root.mainloop()