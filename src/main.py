import os
from pathlib import Path
from PIL import Image


def convert_images_to_webp(folder: Path):
    if not folder.exists():
        print(f"❌ Folder not found: {folder}")
        return

    print(f"📂 Processing: {folder}")
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                img_path = Path(root) / file
                try:
                    with Image.open(img_path) as im:
                        if im.mode in ("RGBA", "LA") or "transparency" in im.info:
                            im = im.convert("RGBA")
                        else:
                            im = im.convert("RGB")

                        webp_path = img_path.with_suffix(".webp")
                        im.save(webp_path, "WEBP", quality=100)
                        print(f"✅ {img_path} -> {webp_path}")

                    img_path.unlink()
                    print(f"🗑️ Deleted original: {img_path}")

                except Exception as e:
                    print(f"⚠️ Failed {img_path}: {e}")


if __name__ == "__main__":
    base = Path(__file__).resolve().parent.parent
    convert_images_to_webp(base / "assets-dark")
    convert_images_to_webp(base / "assets-light")
