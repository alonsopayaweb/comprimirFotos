from PIL import Image # python3 -m pip install Pillow
import pillow_avif 
import os

carpetaFotos = os.getcwd()

if __name__ == "__main__":
    for filename in os.listdir(carpetaFotos):
        name, extension = os.path.splitext(carpetaFotos + filename)

        if extension in [".jpg"]:
            picture = Image.open(carpetaFotos + filename)
            if picture.mode in ("RGBA", "P"): picture = picture.convert("RGB")
            picture.save(carpetaFotos + "compr_"+filename, optimize=True, quality=30)
            print(f'{filename}, procesado!')