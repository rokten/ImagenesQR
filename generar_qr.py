import os
import qrcode

# CONFIGURACIÓN
USUARIO = "rokten"
REPO = "ImagenesQR"
RAMA = "main"

def generar():
    img_dir = "imagenes"
    qr_dir = "codigos_qr"

    os.makedirs(qr_dir, exist_ok=True)

    formatos = ('.jpg', '.jpeg', '.png', '.webp')
    fotos = [f for f in os.listdir(img_dir) if f.lower().endswith(formatos)]

    if not fotos:
        print("❌ No hay fotos en la carpeta /imagenes")
        return

    for foto in fotos:
        link = f"https://raw.githubusercontent.com/{rokten}/{ImagenesQR}/{main}/imagenes/{foto}"

        qr = qrcode.make(link)

        nombre_qr = f"qr_{os.path.splitext(foto)[0]}.png"
        qr.save(os.path.join(qr_dir, nombre_qr))

        print(f"✅ QR creado para: {foto}")

if __name__ == "__main__":
    generar()
