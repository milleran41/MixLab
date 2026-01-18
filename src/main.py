import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import os
import sys
import webbrowser
import urllib.request
import threading

# === Локализация (12 языков) ===
translations = {
    'en': {
        'title': "MixLab - Color Picker & Mixer",
        'upload_image': "Upload Image",
        'take_snapshot': "Camera",
        'save_image': "Save Image",
        'select_color': "Selected Color",
        'color_recipe': "Color Recipe",
        'manual_mix': "Manual Mixing",
        'color_palette': "Color Palette",
        'parts': "parts",
        'percentage': "percent",
        'select_language': "Language",
        'click_to_upload': "Click to upload",
        'Красный': "Red",
        'Жёлтый': "Yellow",
        'Синий': "Blue",
        'Зелёный': "Green",
        'Фиолетовый': "Violet",
        'Чёрный': "Black",
        'Белый': "White",
        'camera_error': "Failed to start camera. Please check permissions.",
        'unavailable_color': "Color unavailable for mixing",
        'add_color': "Add Color",
        'result': "Result",
        'delete': "Delete",
        'zoom_in': "Zoom In",
        'zoom_out': "Zoom Out",
        'clear': "Clear",
        'no_image': "No image loaded",
        'recipe_not_available': "Select a color to view recipe",
        'magnifier_title': "Magnifier",
        'selected_pixel': "Selected pixel:",
        'zoom': "Zoom: 10x",
        'image': "Image",
        'custom_mix': "Custom Mix",
        'support_project': "Support Project"
    },
    'ru': {
        'title': "MixLab - Color Picker & Mixer",
        'upload_image': "Загрузить изображение",
        'take_snapshot': "Камера",
        'save_image': "Сохранить изображение",
        'select_color': "Выбранный цвет",
        'color_recipe': "Рецепт смешивания",
        'manual_mix': "Ручное смешивание",
        'color_palette': "Палитра цветов",
        'parts': "части",
        'percentage': "процентов",
        'select_language': "Язык",
        'click_to_upload': "Нажмите для загрузки",
        'Красный': "Красный",
        'Жёлтый': "Жёлтый",
        'Синий': "Синий",
        'Зелёный': "Зелёный",
        'Фиолетовый': "Фиолетовый",
        'Чёрный': "Чёрный",
        'Белый': "Белый",
        'camera_error': "Не удалось включить камеру. Проверьте разрешения.",
        'unavailable_color': "Цвет недоступен для смешивания",
        'add_color': "Добавить цвет",
        'result': "Результат",
        'delete': "Удалить",
        'zoom_in': "Увеличить",
        'zoom_out': "Уменьшить",
        'clear': "Очистить",
        'no_image': "Изображение не загружено",
        'recipe_not_available': "Выберите цвет для отображения рецепта",
        'magnifier_title': "Лупа",
        'selected_pixel': "Выбранный пиксель:",
        'zoom': "Увеличение: 10x",
        'image': "Изображение",
        'custom_mix': "Пользовательское смешивание",
        'support_project': "Поддержать проект"
    },
    'es': {
        'title': "MixLab - Selector y Mezclador de Colores",
        'upload_image': "Cargar imagen",
        'take_snapshot': "Cámara",
        'save_image': "Guardar imagen",
        'select_color': "Color seleccionado",
        'color_recipe': "Receta de color",
        'manual_mix': "Mezcla manual",
        'color_palette': "Paleta de colores",
        'parts': "partes",
        'percentage': "por ciento",
        'select_language': "Idioma",
        'click_to_upload': "Haga clic para cargar",
        'Красный': "Rojo",
        'Жёлтый': "Amarillo",
        'Синий': "Azul",
        'Зелёный': "Verde",
        'Фиолетовый': "Violeta",
        'Чёрный': "Negro",
        'Белый': "Blanco",
        'camera_error': "Error al iniciar la cámara. Verifique los permisos.",
        'unavailable_color': "Color no disponible para mezclar",
        'add_color': "Añadir color",
        'result': "Resultado",
        'delete': "Eliminar",
        'zoom_in': "Acercar",
        'zoom_out': "Alejar",
        'clear': "Borrar",
        'no_image': "No se ha cargado ninguna imagen",
        'recipe_not_available': "Seleccione un color para ver la receta",
        'magnifier_title': "Lupa",
        'selected_pixel': "Píxel seleccionado:",
        'zoom': "Zoom: 10x",
        'image': "Imagen",
        'custom_mix': "Mezcla personalizada",
        'support_project': "Apoyar el proyecto"
    },
    'de': {
        'title': "MixLab - Farbwähler & Mischer",
        'upload_image': "Bild hochladen",
        'take_snapshot': "Kamera",
        'save_image': "Bild speichern",
        'select_color': "Ausgewählte Farbe",
        'color_recipe': "Farb-Rezept",
        'manual_mix': "Manuelles Mischen",
        'color_palette': "Farbpalette",
        'parts': "Teile",
        'percentage': "Prozent",
        'select_language': "Sprache",
        'click_to_upload': "Zum Hochladen klicken",
        'Красный': "Rot",
        'Жёлтый': "Gelb",
        'Синий': "Blau",
        'Зелёный': "Grün",
        'Фиолетовый': "Violett",
        'Чёрный': "Schwarz",
        'Белый': "Weiß",
        'camera_error': "Kamera konnte nicht gestartet werden. Berechtigungen prüfen.",
        'unavailable_color': "Farbe nicht mischbar",
        'add_color': "Farbe hinzufügen",
        'result': "Ergebnis",
        'delete': "Löschen",
        'zoom_in': "Vergrößern",
        'zoom_out': "Verkleinern",
        'clear': "Löschen",
        'no_image': "Kein Bild geladen",
        'recipe_not_available': "Wählen Sie eine Farbe, um das Rezept zu sehen",
        'magnifier_title': "Lupe",
        'selected_pixel': "Ausgewähltes Pixel:",
        'zoom': "Vergrößerung: 10x",
        'image': "Bild",
        'custom_mix': "Benutzerdefinierte Mischung",
        'support_project': "Projekt unterstützen"
    },
    'fr': {
        'title': "MixLab - Sélecteur et Mélangeur de Couleurs",
        'upload_image': "Charger une image",
        'take_snapshot': "Appareil photo",
        'save_image': "Enregistrer l'image",
        'select_color': "Couleur sélectionnée",
        'color_recipe': "Recette de couleur",
        'manual_mix': "Mélange manuel",
        'color_palette': "Palette de couleurs",
        'parts': "parties",
        'percentage': "pour cent",
        'select_language': "Langue",
        'click_to_upload': "Cliquez pour charger",
        'Красный': "Rouge",
        'Жёлтый': "Jaune",
        'Синий': "Bleu",
        'Зелёный': "Vert",
        'Фиолетовый': "Violet",
        'Чёрный': "Noir",
        'Белый': "Blanc",
        'camera_error': "Échec du démarrage de la caméra. Vérifiez les autorisations.",
        'unavailable_color': "Couleur non disponible pour le mélange",
        'add_color': "Ajouter une couleur",
        'result': "Résultat",
        'delete': "Supprimer",
        'zoom_in': "Zoom avant",
        'zoom_out': "Zoom arrière",
        'clear': "Effacer",
        'no_image': "Aucune image chargée",
        'recipe_not_available': "Sélectionnez une couleur pour voir la recette",
        'magnifier_title': "Loupe",
        'selected_pixel': "Pixel sélectionné :",
        'zoom': "Zoom : 10x",
        'image': "Image",
        'custom_mix': "Mélange personnalisé",
        'support_project': "Soutenir le projet"
    },
    'it': {
        'title': "MixLab - Selettore e Miscelatore di Colori",
        'upload_image': "Carica immagine",
        'take_snapshot': "Fotocamera",
        'save_image': "Salva immagine",
        'select_color': "Colore selezionato",
        'color_recipe': "Ricetta colore",
        'manual_mix': "Miscelazione manuale",
        'color_palette': "Tavolozza colori",
        'parts': "parti",
        'percentage': "percento",
        'select_language': "Lingua",
        'click_to_upload': "Clicca per caricare",
        'Красный': "Rosso",
        'Жёлтый': "Giallo",
        'Синий': "Blu",
        'Зелёный': "Verde",
        'Фиолетовый': "Viola",
        'Чёрный': "Nero",
        'Белый': "Bianco",
        'camera_error': "Impossibile avviare la fotocamera. Controlla i permessi.",
        'unavailable_color': "Colore non disponibile per la miscelazione",
        'add_color': "Aggiungi colore",
        'result': "Risultato",
        'delete': "Elimina",
        'zoom_in': "Ingrandisci",
        'zoom_out': "Riduci",
        'clear': "Cancella",
        'no_image': "Nessuna immagine caricata",
        'recipe_not_available': "Seleziona un colore per vedere la ricetta",
        'magnifier_title': "Lente d'ingrandimento",
        'selected_pixel': "Pixel selezionato:",
        'zoom': "Ingrandimento: 10x",
        'image': "Immagine",
        'custom_mix': "Miscelazione personalizzata",
        'support_project': "Supporta il progetto"
    },
    'pt': {
        'title': "MixLab - Seletor e Misturador de Cores",
        'upload_image': "Carregar imagem",
        'take_snapshot': "Câmera",
        'save_image': "Salvar imagem",
        'select_color': "Cor selecionada",
        'color_recipe': "Receita de cor",
        'manual_mix': "Mistura manual",
        'color_palette': "Paleta de cores",
        'parts': "partes",
        'percentage': "por cento",
        'select_language': "Idioma",
        'click_to_upload': "Clique para carregar",
        'Красный': "Vermelho",
        'Жёлтый': "Amarelo",
        'Синий': "Azul",
        'Зелёный': "Verde",
        'Фиолетовый': "Violeta",
        'Чёрный': "Preto",
        'Белый': "Branco",
        'camera_error': "Falha ao iniciar a câmera. Verifique as permissões.",
        'unavailable_color': "Cor indisponível para mistura",
        'add_color': "Adicionar cor",
        'result': "Resultado",
        'delete': "Excluir",
        'zoom_in': "Ampliar",
        'zoom_out': "Reduzir",
        'clear': "Limpar",
        'no_image': "Nenhuma imagem carregada",
        'recipe_not_available': "Selecione uma cor para ver a receita",
        'magnifier_title': "Lupa",
        'selected_pixel': "Pixel selecionado:",
        'zoom': "Zoom: 10x",
        'image': "Imagem",
        'custom_mix': "Mistura personalizada",
        'support_project': "Apoiar o projeto"
    },
    'ar': {
        'title': "MixLab - منتقي الألوان وخلاطها",
        'upload_image': "تحميل صورة",
        'take_snapshot': "الكاميرا",
        'save_image': "حفظ الصورة",
        'select_color': "اللون المحدد",
        'color_recipe': "وصفة اللون",
        'manual_mix': "خلط يدوي",
        'color_palette': "لوحة الألوان",
        'parts': "أجزاء",
        'percentage': "بالمئة",
        'select_language': "اللغة",
        'click_to_upload': "انقر للتحميل",
        'Красный': "أحمر",
        'Жёлтый': "أصفر",
        'Синий': "أزرق",
        'Зелёный': "أخضر",
        'Фиолетовый': "بنفسجي",
        'Чёрный': "أسود",
        'Белый': "أبيض",
        'camera_error': "فشل في تشغيل الكاميرا. تحقق من الأذونات.",
        'unavailable_color': "اللون غير متاح للخلط",
        'add_color': "إضافة لون",
        'result': "النتيجة",
        'delete': "حذف",
        'zoom_in': "تكبير",
        'zoom_out': "تصغير",
        'clear': "مسح",
        'no_image': "لم يتم تحميل أي صورة",
        'recipe_not_available': "اختر لونًا لعرض الوصفة",
        'magnifier_title': "عدسة مكبرة",
        'selected_pixel': "البكسل المحدد:",
        'zoom': "التكبير: 10x",
        'image': "صورة",
        'custom_mix': "خلط مخصص",
        'support_project': "دعم المشروع"
    },
    'zh': {
        'title': "MixLab - 颜色选择器与混合器",
        'upload_image': "上传图片",
        'take_snapshot': "相机",
        'save_image': "保存图片",
        'select_color': "所选颜色",
        'color_recipe': "颜色配方",
        'manual_mix': "手动混合",
        'color_palette': "调色板",
        'parts': "份",
        'percentage': "百分比",
        'select_language': "语言",
        'click_to_upload': "点击上传",
        'Красный': "红色",
        'Жёлтый': "黄色",
        'Синий': "蓝色",
        'Зелёный': "绿色",
        'Фиолетовый': "紫色",
        'Чёрный': "黑色",
        'Белый': "白色",
        'camera_error': "无法启动相机。请检查权限。",
        'unavailable_color': "该颜色无法混合",
        'add_color': "添加颜色",
        'result': "结果",
        'delete': "删除",
        'zoom_in': "放大",
        'zoom_out': "缩小",
        'clear': "清除",
        'no_image': "未加载图片",
        'recipe_not_available': "请选择一个颜色以查看配方",
        'magnifier_title': "放大镜",
        'selected_pixel': "所选像素：",
        'zoom': "缩放：10倍",
        'image': "图片",
        'custom_mix': "自定义混合",
        'support_project': "支持项目"
    },
    'ja': {
        'title': "MixLab - カラーピッカー＆ミキサー",
        'upload_image': "画像をアップロード",
        'take_snapshot': "カメラ",
        'save_image': "画像を保存",
        'select_color': "選択された色",
        'color_recipe': "カラーレシピ",
        'manual_mix': "手動混合",
        'color_palette': "カラーパレット",
        'parts': "部品",
        'percentage': "パーセント",
        'select_language': "言語",
        'click_to_upload': "クリックしてアップロード",
        'Красный': "赤",
        'Жёлтый': "黄",
        'Синий': "青",
        'Зелёный': "緑",
        'Фиолетовый': "紫",
        'Чёрный': "黒",
        'Белый': "白",
        'camera_error': "カメラを起動できませんでした。権限を確認してください。",
        'unavailable_color': "この色は混合できません",
        'add_color': "色を追加",
        'result': "結果",
        'delete': "削除",
        'zoom_in': "拡大",
        'zoom_out': "縮小",
        'clear': "クリア",
        'no_image': "画像が読み込まれていません",
        'recipe_not_available': "レシピを表示するには色を選択してください",
        'magnifier_title': "拡大鏡",
        'selected_pixel': "選択したピクセル：",
        'zoom': "ズーム：10倍",
        'image': "画像",
        'custom_mix': "カスタム混合",
        'support_project': "プロジェクトを支援"
    },
    'pl': {
        'title': "MixLab - Selektor i Mieszacz Kolorów",
        'upload_image': "Załaduj obraz",
        'take_snapshot': "Aparat",
        'save_image': "Zapisz obraz",
        'select_color': "Wybrany kolor",
        'color_recipe': "Przepis na kolor",
        'manual_mix': "Mieszanie ręczne",
        'color_palette': "Paleta kolorów",
        'parts': "części",
        'percentage': "procent",
        'select_language': "Język",
        'click_to_upload': "Kliknij, aby załadować",
        'Красный': "Czerwony",
        'Жёлтый': "Żółty",
        'Синий': "Niebieski",
        'Зелёный': "Zielony",
        'Фиолетовый': "Fioletowy",
        'Чёрный': "Czarny",
        'Белый': "Biały",
        'camera_error': "Nie udało się uruchomić aparatu. Sprawdź uprawnienia.",
        'unavailable_color': "Kolor niedostępny do mieszania",
        'add_color': "Dodaj kolor",
        'result': "Wynik",
        'delete': "Usuń",
        'zoom_in': "Powiększ",
        'zoom_out': "Pomniejsz",
        'clear': "Wyczyść",
        'no_image': "Nie załadowano obrazu",
        'recipe_not_available': "Wybierz kolor, aby zobaczyć przepis",
        'magnifier_title': "Lupa",
        'selected_pixel': "Wybrany piksel:",
        'zoom': "Powiększenie: 10x",
        'image': "Obraz",
        'custom_mix': "Mieszanka niestandardowa",
        'support_project': "Wesprzyj projekt"
    },
    'tr': {
        'title': "MixLab - Renk Seçici ve Karıştırıcı",
        'upload_image': "Görüntü yükle",
        'take_snapshot': "Kamera",
        'save_image': "Görüntüyü kaydet",
        'select_color': "Seçilen renk",
        'color_recipe': "Renk tarifi",
        'manual_mix': "Manuel karıştırma",
        'color_palette': "Renk paleti",
        'parts': "parça",
        'percentage': "yüzde",
        'select_language': "Dil",
        'click_to_upload': "Yüklemek için tıklayın",
        'Красный': "Kırmızı",
        'Жёлтый': "Sarı",
        'Синий': "Mavi",
        'Зелёный': "Yeşil",
        'Фиолетовый': "Mor",
        'Чёрный': "Siyah",
        'Белый': "Beyaz",
        'camera_error': "Kamera başlatılamadı. İzinleri kontrol edin.",
        'unavailable_color': "Renk karıştırma için uygun değil",
        'add_color': "Renk ekle",
        'result': "Sonuç",
        'delete': "Sil",
        'zoom_in': "Yakınlaştır",
        'zoom_out': "Uzaklaştır",
        'clear': "Temizle",
        'no_image': "Görüntü yüklenmedi",
        'recipe_not_available': "Tarifi görüntülemek için bir renk seçin",
        'magnifier_title': "Büyüteç",
        'selected_pixel': "Seçilen piksel:",
        'zoom': "Yakınlaştırma: 10x",
        'image': "Görüntü",
        'custom_mix': "Özel karışım",
        'support_project': "Projeyi destekle"
    }
}

# === Список поддерживаемых языков ===
LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
    ('es', 'Español'),
    ('de', 'Deutsch'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
    ('pt', 'Português'),
    ('ar', 'العربية'),
    ('zh', '中文'),
    ('ja', '日本語'),
    ('pl', 'Polski'),
    ('tr', 'Türkçe')
]

# === Базовые цвета ===
base_colors = [
    {"name": "Красный", "hex": "#D32F2F", "rgb": [211, 47, 47]},
    {"name": "Жёлтый", "hex": "#FBC02D", "rgb": [251, 192, 45]},
    {"name": "Синий", "hex": "#1976D2", "rgb": [25, 118, 210]},
    {"name": "Зелёный", "hex": "#388E3C", "rgb": [56, 142, 60]},
    {"name": "Фиолетовый", "hex": "#7B1FA2", "rgb": [123, 31, 162]},
    {"name": "Чёрный", "hex": "#212121", "rgb": [33, 33, 33]},
    {"name": "Белый", "hex": "#FFFFFF", "rgb": [255, 255, 255]}
]

# === Глобальные переменные ===
image_path = None
original_image = None
tk_image = None
selected_color = "#000000"
current_recipe = None
language = "ru"
manual_colors = [{"color": "#FF0000", "parts": 1}, {"color": "#0000FF", "parts": 1}]
manual_result = "#800080"
zoom = 1.0

# Инициализация локализации с поддержкой current_lang_name
t = translations[language].copy()
display_names = dict(LANGUAGES)
t['current_lang_name'] = display_names.get(language, language)

active_color = "#FF0000"
recipe_title = None
palette_inner = None
palette_support_frame = None
lang_button = None  # <-- важно для обновления текста

# === Вспомогательные функции ===
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def calculate_recipe(hex_color, r, g, b):
    target_rgb = [r, g, b]
    distances = []
    for color in base_colors:
        dr = r - color["rgb"][0]
        dg = g - color["rgb"][1]
        db = b - color["rgb"][2]
        distance = (dr*dr + dg*dg + db*db) ** 0.5
        distances.append({**color, "distance": distance})
    distances.sort(key=lambda x: x["distance"])
    top_colors = distances[:3]
    total_weight = sum(1 / (c["distance"] + 1) for c in top_colors)
    recipe = []
    for color in top_colors:
        weight = (1 / (color["distance"] + 1)) / total_weight
        parts = max(1, round(weight * 10))
        percentage = round(weight * 100)
        recipe.append({
            "color": color["name"],
            "parts": parts,
            "percentage": percentage
        })
    total_parts = sum(item["parts"] for item in recipe)
    scale = 10 / total_parts
    for item in recipe:
        item["parts"] = max(1, round(item["parts"] * scale))
    return [item for item in recipe if item["percentage"] > 5]

# === Функция для работы с путями ресурсов ===
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    full_path = os.path.join(base_path, relative_path)
    if os.path.exists(full_path):
        return full_path
    try:
        base_path = sys._MEIPASS
        full_path = os.path.join(base_path, relative_path)
        if os.path.exists(full_path):
            return full_path
    except Exception:
        pass
    return os.path.join(os.path.abspath("."), relative_path)

# === Функция загрузки QR-кода ===
def ensure_qr_exists():
    qr_path = resource_path("assets/qr-donate.png")
    os.makedirs(os.path.dirname(qr_path), exist_ok=True)
    if not os.path.exists(qr_path):
        try:
            urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/milleran41/linkora/main/assets/qr-donate.png",
                qr_path
            )
        except Exception as e:
            print("Failed to download QR code:", e)
    return qr_path

# === Остальные функции (без изменений) ===
def load_image():
    global image_path, original_image, tk_image, zoom
    path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if not path: return
    image_path = path
    try:
        original_image = Image.open(path).convert("RGB")
        zoom = 1.0
        display_image()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image:\n{e}")

def display_image():
    global tk_image
    if original_image is None: return
    w, h = original_image.size
    new_size = (int(w * zoom), int(h * zoom))
    resized = original_image.resize(new_size, Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized)
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.config(scrollregion=(0, 0, new_size[0], new_size[1]))

def save_image():
    if original_image is None:
        messagebox.showinfo(t['title'], t['no_image'])
        return
    path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")])
    if path:
        original_image.save(path)
        messagebox.showinfo(t['title'], t['save_image'])

def zoom_in():
    global zoom
    zoom = min(3.0, zoom + 0.1)
    display_image()
    zoom_label.config(text=f"{round(zoom * 100)}%")

def zoom_out():
    global zoom
    zoom = max(0.5, zoom - 0.1)
    display_image()
    zoom_label.config(text=f"{round(zoom * 100)}%")

def clear_image():
    global image_path, original_image, tk_image, current_recipe, selected_color
    image_path = None
    original_image = None
    tk_image = None
    canvas.delete("all")
    canvas.config(scrollregion=(0, 0, 100, 100))
    selected_color = "#000000"
    color_display.config(bg=selected_color)
    color_hex_label.config(text=selected_color)
    current_recipe = None
    display_recipe()

def show_magnifier(x, y):
    if original_image is None: return
    size = 5
    left = max(0, x - size//2)
    right = min(original_image.width, x + size//2 + 1)
    top = max(0, y - size//2)
    bottom = min(original_image.height, y + size//2 + 1)
    cropped = original_image.crop((left, top, right, bottom))
    magnified = cropped.resize((50, 50), Image.NEAREST)
    win = tk.Toplevel(root)
    win.title(t['magnifier_title'])
    win.resizable(False, False)
    win.geometry("180x180+100+100")
    win.transient(root)
    win.focus_set()
    tk_img = ImageTk.PhotoImage(magnified)
    label = tk.Label(win, image=tk_img, borderwidth=2, relief="solid")
    label.pack(pady=10)
    label.image = tk_img
    info = tk.Label(win, text=f"{t['selected_pixel']} ({x}, {y})\n{t['zoom']}", font=("Arial", 9))
    info.pack()
    win.after(2000, win.destroy)

def on_canvas_click(event):
    if original_image is None: return
    x = round(event.x / zoom)
    y = round(event.y / zoom)
    if x < 0 or y < 0 or x >= original_image.width or y >= original_image.height: return
    show_magnifier(x, y)
    r, g, b = original_image.getpixel((x, y))
    hex_color = rgb_to_hex(r, g, b)
    select_color(hex_color, r, g, b)

def select_color(hex_color, r=None, g=None, b=None):
    global selected_color, current_recipe, active_color
    selected_color = hex_color
    active_color = hex_color
    color_display.config(bg=hex_color)
    color_hex_label.config(text=hex_color.upper())
    if r is None: r, g, b = hex_to_rgb(hex_color)
    recipe = calculate_recipe(hex_color, r, g, b)
    current_recipe = {"name": "custom_mix", "hex": hex_color, "rgb": f"{r}, {g}, {b}", "recipe": recipe}
    display_recipe()

def calculate_manual_mix():
    global manual_result
    total_parts = sum(c["parts"] for c in manual_colors)
    if total_parts == 0: return
    r = g = b = 0.0
    for c in manual_colors:
        cr, cg, cb = hex_to_rgb(c["color"])
        weight = c["parts"] / total_parts
        r += cr * weight
        g += cg * weight
        b += cb * weight
    manual_result = rgb_to_hex(int(round(r)), int(round(g)), int(round(b)))
    result_label.config(bg=manual_result)
    result_hex_label.config(text=manual_result.upper())

def update_manual_display():
    for widget in manual_frame.winfo_children():
        widget.destroy()
    for i, c in enumerate(manual_colors):
        cr, cg, cb = hex_to_rgb(c["color"])
        brightness = (cr * 299 + cg * 587 + cb * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        color_btn = tk.Button(manual_frame, bg=c["color"], width=3, relief="raised")
        color_btn.bind("<Button-1>", lambda e, idx=i: open_color_picker(idx))
        color_btn.grid(row=i, column=0, padx=2, pady=2)
        parts_var = tk.StringVar(value=str(c["parts"]))
        parts_var.trace_add("write", lambda *args, idx=i, var=parts_var: update_parts(idx, var))
        parts_entry = tk.Entry(manual_frame, textvariable=parts_var, width=5)
        parts_entry.grid(row=i, column=1, padx=2)
        total = sum(c["parts"] for c in manual_colors)
        percent = int((c["parts"] / total) * 100) if total > 0 else 0
        percent_label = tk.Label(manual_frame, text=f"{percent}%", width=6)
        percent_label.grid(row=i, column=2, padx=2)
        del_btn = tk.Button(manual_frame, text=t['delete'], command=lambda idx=i: delete_manual_color(idx), width=6)
        del_btn.grid(row=i, column=3, padx=2)
    calculate_manual_mix()

def update_parts(idx, var):
    try:
        value = int(var.get())
        if value < 1: value = 1
        manual_colors[idx]["parts"] = value
        calculate_manual_mix()
    except: pass

def delete_manual_color(idx):
    if len(manual_colors) > 1:
        manual_colors.pop(idx)
        update_manual_display()

def open_color_picker(idx):
    color = colorchooser.askcolor(manual_colors[idx]["color"])[1]
    if color:
        manual_colors[idx]["color"] = color
        update_manual_display()

def add_manual_color():
    manual_colors.append({"color": active_color, "parts": 1})
    update_manual_display()

def display_recipe():
    global recipe_title
    for widget in recipe_frame.winfo_children():
        if widget != recipe_title:
            widget.destroy()
    if current_recipe is None:
        if recipe_title: recipe_title.config(text=t['color_recipe'])
        tk.Label(recipe_frame, text=t['recipe_not_available'], fg="gray", font=("Arial", 10)).pack()
        return
    cname = t.get(current_recipe["name"], current_recipe["name"])
    if recipe_title: recipe_title.config(text=cname)
    tk.Label(recipe_frame, text=f"HEX: {current_recipe['hex'].upper()}").pack(anchor="w")
    tk.Label(recipe_frame, text=f"RGB: {current_recipe['rgb']}").pack(anchor="w")
    for item in current_recipe["recipe"]:
        color_name = t.get(item["color"], item["color"])
        tk.Label(recipe_frame, text=f"{color_name}: {item['parts']} {t['parts']} ({item['percentage']}%)").pack(anchor="w")

def create_palette_in_frame(parent):
    for widget in parent.winfo_children():
        widget.destroy()
    for i, color in enumerate(base_colors):
        cname = t[color["name"]]
        cr, cg, cb = color["rgb"]
        brightness = (cr * 299 + cg * 587 + cb * 114) / 1000
        text_color = "white" if brightness < 128 else "black"
        btn = tk.Button(
            parent,
            text=cname,
            bg=color["hex"],
            fg=text_color,
            width=12,
            relief="raised",
            font=("Arial", 9),
            command=lambda c=color: select_color(c["hex"], *c["rgb"])
        )
        btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="ew")
    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(1, weight=1)

# === Изменённая функция смены языка ===
def change_language(lang):
    global language, t
    language = lang
    t = translations[lang].copy()  # всегда работаем с копией
    display_names = dict(LANGUAGES)
    t['current_lang_name'] = display_names.get(lang, lang)
    update_ui_texts()

def update_ui_texts():
    global recipe_title, lang_button, palette_support_frame
    root.title(t['title'])
    upload_btn.config(text=t['upload_image'])
    save_btn.config(text=t['save_image'])
    zoom_in_btn.config(text=t['zoom_in'])
    zoom_out_btn.config(text=t['zoom_out'])
    clear_btn.config(text=t['clear'])
    color_label.config(text=f"{t['select_color']}:")
    color_frame.config(text=t['select_color'])
    add_btn.config(text=t['add_color'])
    result_label_text.config(text=t['result'])
    left_frame.config(text=t['image'])
    recipe_frame.config(text=t['color_recipe'])
    manual_frame_outer.config(text=t['manual_mix'])
    palette_support_frame.config(text=t['color_palette'])
    if recipe_title: recipe_title.config(text=t['color_recipe'])
    create_palette_in_frame(palette_inner)
    display_recipe()
    update_manual_display()
    calculate_manual_mix()
    # Обновляем текст кнопки выбора языка
    lang_button.config(text=t['current_lang_name'])
    # Обновляем кнопку поддержки
    for child in support_frame.winfo_children():
        if isinstance(child, ttk.Button):
            child.config(text=t['support_project'])

def on_background_click(event):
    calculate_manual_mix()

# === GUI ===
root = tk.Tk()
root.title("MixLab - Color Picker & Mixer")
root.geometry("1600x900")
root.minsize(1200, 700)

style = ttk.Style()
style.configure("Bold.TLabelframe.Label", font=("Arial", 10, "bold"))

try:
    icon_path = resource_path("assets/icon.ico")
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
except Exception as e:
    print("Icon not loaded:", e)

root.bind("<Button-1>", on_background_click)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=6)
main_frame.grid_columnconfigure(1, weight=4)
main_frame.grid_rowconfigure(1, weight=1)

# === Верхняя панель ===
top_frame = ttk.Frame(main_frame)
top_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)

# >>> КНОПКА ЯЗЫКА — ТОЧНО НА МЕСТЕ <<<
lang_button = ttk.Menubutton(top_frame, text="Русский", direction="below")
lang_menu_dropdown = tk.Menu(lang_button, tearoff=0)
for code, name in LANGUAGES:
    lang_menu_dropdown.add_command(label=name, command=lambda c=code: change_language(c))
lang_button["menu"] = lang_menu_dropdown
lang_button.pack(side="right", padx=2)

upload_btn = ttk.Button(top_frame, text=t['upload_image'], command=load_image)
upload_btn.pack(side="left", padx=2)
save_btn = ttk.Button(top_frame, text=t['save_image'], command=save_image)
save_btn.pack(side="left", padx=2)
zoom_out_btn = ttk.Button(top_frame, text=t['zoom_out'], command=zoom_out)
zoom_out_btn.pack(side="left", padx=2)
zoom_in_btn = ttk.Button(top_frame, text=t['zoom_in'], command=zoom_in)
zoom_in_btn.pack(side="left", padx=2)
zoom_label = ttk.Label(top_frame, text="100%")
zoom_label.pack(side="left", padx=5)
clear_btn = ttk.Button(top_frame, text=t['clear'], command=clear_image)
clear_btn.pack(side="right", padx=2)

# Левая часть — изображение
left_frame = ttk.LabelFrame(main_frame, text=t['image'], padding="5", style="Bold.TLabelframe")
left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 5), pady=(0, 5))
left_frame.grid_rowconfigure(0, weight=1)
left_frame.grid_columnconfigure(0, weight=1)

canvas_frame = ttk.Frame(left_frame)
canvas_frame.grid(row=0, column=0, sticky="nsew")
canvas = tk.Canvas(canvas_frame, bg="lightgray", cursor="crosshair")
canvas.pack(side="left", fill="both", expand=True)
canvas.bind("<Button-1>", on_canvas_click)
v_scroll = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
v_scroll.pack(side="right", fill="y")
canvas.configure(yscrollcommand=v_scroll.set)
h_scroll = ttk.Scrollbar(left_frame, orient="horizontal", command=canvas.xview)
h_scroll.grid(row=1, column=0, sticky="ew")
canvas.configure(xscrollcommand=h_scroll.set)

# Правая часть
right_frame = ttk.Frame(main_frame)
right_frame.grid(row=1, column=1, sticky="nsew", padx=(5, 0))
right_frame.grid_rowconfigure(1, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

# Выбранный цвет
color_frame = ttk.LabelFrame(right_frame, text=t['select_color'], padding="5", style="Bold.TLabelframe")
color_frame.grid(row=0, column=0, sticky="ew", pady=(0, 5))
color_frame.grid_columnconfigure(1, weight=1)
color_label = ttk.Label(color_frame, text=f"{t['select_color']}:", font=("Arial", 10))
color_label.grid(row=0, column=0, sticky="w")
color_display = tk.Frame(color_frame, bg=selected_color, width=50, height=50, relief="solid", bd=1)
color_display.grid(row=0, column=1, padx=5)
color_hex_label = ttk.Label(color_frame, text=selected_color.upper(), font=("monospace", 10))
color_hex_label.grid(row=0, column=2, padx=5)

# Рецепт
recipe_frame = ttk.LabelFrame(right_frame, text=t['color_recipe'], padding="5", style="Bold.TLabelframe")
recipe_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
recipe_frame.grid_columnconfigure(0, weight=1)
recipe_title = tk.Label(recipe_frame, text=t['color_recipe'], font=("bold", 11))
recipe_title.pack(anchor="w", pady=2)
display_recipe()

# Ручное смешивание
manual_frame_outer = ttk.LabelFrame(right_frame, text=t['manual_mix'], padding="5", style="Bold.TLabelframe")
manual_frame_outer.grid(row=2, column=0, sticky="ew", pady=(0, 5))
manual_frame = ttk.Frame(manual_frame_outer)
manual_frame.pack(fill="x", pady=(0, 5))
add_btn = ttk.Button(manual_frame_outer, text=t['add_color'], command=add_manual_color)
add_btn.pack(fill="x", pady=(0, 5))
result_frame = ttk.Frame(manual_frame_outer)
result_frame.pack(fill="x")
result_label_text = ttk.Label(result_frame, text=f"{t['result']}:", font=("Arial", 10, "bold"))
result_label_text.pack(side="left")
result_label = tk.Frame(result_frame, bg=manual_result, width=50, height=50, relief="solid", bd=1)
result_label.pack(side="left", padx=5)
result_hex_label = ttk.Label(result_frame, text=manual_result.upper(), font=("monospace", 10))
result_hex_label.pack(side="left", padx=5)

# === Палитра + Поддержка ===
palette_support_frame = ttk.LabelFrame(right_frame, text=t['color_palette'], padding="5", style="Bold.TLabelframe")
palette_support_frame.grid(row=3, column=0, sticky="ew", pady=(0, 5))
palette_support_frame.grid_columnconfigure(0, weight=3)
palette_support_frame.grid_columnconfigure(1, weight=1)

palette_inner = ttk.Frame(palette_support_frame)
palette_inner.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
create_palette_in_frame(palette_inner)

support_frame = ttk.Frame(palette_support_frame)
support_frame.grid(row=0, column=1, sticky="nsew")

def load_qr_and_show():
    qr_path = ensure_qr_exists()
    if os.path.exists(qr_path):
        try:
            img = Image.open(qr_path)
            img = img.resize((120, 120), Image.Resampling.LANCZOS)
            qr_photo = ImageTk.PhotoImage(img)
            qr_label = tk.Label(support_frame, image=qr_photo)
            qr_label.image = qr_photo
            qr_label.pack(pady=(0, 10))
        except Exception as e:
            print("QR load error:", e)

threading.Thread(target=load_qr_and_show, daemon=True).start()

support_btn = ttk.Button(support_frame, text=t['support_project'], command=lambda: webbrowser.open("https://ko-fi.com/linkora"))
support_btn.pack(fill="x")

# Инициализация
update_ui_texts()

root.mainloop()