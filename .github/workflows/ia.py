import random
from PIL import Image, ImageDraw
from moviepy.editor import ImageClip, concatenate_videoclips

# ======================
# IA CONVERSATION FR
# ======================

reponses = {
    "bonjour": [
        "Bonjour 🙂 Comment puis-je t’aider ?",
        "Salut ! Ravi de te parler.",
    ],
    "ça va": [
        "Oui, ça va très bien, merci ! Et toi ?",
        "Toujours en forme 😄",
    ],
    "qui es tu": [
        "Je suis une intelligence artificielle locale, sans Internet.",
        "Une IA simple, mais efficace 😌",
    ],
    "default": [
        "Explique-moi un peu plus.",
        "C’est intéressant, continue.",
        "Je comprends.",
    ]
}

def parler(message):
    msg = message.lower()
    for cle in reponses:
        if cle in msg:
            return random.choice(reponses[cle])
    return random.choice(reponses["default"])

# ======================
# IA ÉCRITURE FR
# ======================

def bien_ecrire(texte):
    texte = texte.strip().capitalize()
    if not texte.endswith("."):
        texte += "."
    return texte

# ======================
# GÉNÉRATION IMAGE
# ======================

def creer_image(texte):
    img = Image.new("RGB", (512, 512), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    draw.text((20, 240), texte, fill=(255, 255, 255))
    img.save("image.png")
    return "image.png"

# ======================
# GÉNÉRATION VIDÉO
# ======================

def creer_video():
    images = []
    for i in range(3):
        img = Image.new("RGB", (512, 512), color=(50*i, 80, 120))
        draw = ImageDraw.Draw(img)
        draw.text((200, 240), f"Frame {i+1}", fill=(255, 255, 255))
        nom = f"frame{i}.png"
        img.save(nom)
        images.append(nom)

    clips = [ImageClip(img).set_duration(2) for img in images]
    video = concatenate_videoclips(clips)
    video.write_videofile("video.mp4", fps=24)
    return "video.mp4"

# ======================
# MENU PRINCIPAL
# ======================

print("🤖 IA LOCALE - BLACKVIEW TAB 90")

while True:
    print("\n1 - Parler avec l’IA")
    print("2 - Bien écrire un texte")
    print("3 - Créer une image")
    print("4 - Créer une vidéo")
    print("5 - Quitter")

    choix = input("Choix : ")

    if choix == "1":
        msg = input("Toi : ")
        print("IA :", parler(msg))

    elif choix == "2":
        txt = input("Texte : ")
        print("Corrigé :", bien_ecrire(txt))

    elif choix == "3":
        t = input("Texte image : ")
        print("Image créée :", creer_image(t))

    elif choix == "4":
        print("Création vidéo...")
        print("Vidéo :", creer_video())

    elif choix == "5":
        break