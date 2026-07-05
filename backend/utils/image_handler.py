from pathlib import Path
from flask import current_app
from uuid import uuid4


class ImageHandler:

    @staticmethod
    def _get_upload_dir():
        return Path(current_app.config["UPLOAD_FOLDER"])

    @staticmethod
    def save_image(image):
        if not image:
            return None
        suffix = Path(image.filename).suffix
        image_name = str(uuid4()) + suffix
        image_path = ImageHandler._get_upload_dir() / image_name
        image_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(image_path)
        return image_name

    @staticmethod
    def get_image_path(image_name):
        image_path = ImageHandler._get_upload_dir() / image_name
        if not image_path.exists():
            image_path = ImageHandler._get_upload_dir() / "no-image.png"
        return image_path

    @staticmethod
    def update_image(old_image_name, image):
        if not image.filename:
            return old_image_name
        image_name = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return image_name

    @staticmethod
    def delete_image(image_name):
        if not image_name:
            return
        if image_name == "no-image.png":
            return
        image_path = ImageHandler._get_upload_dir() / image_name
        image_path.unlink(missing_ok=True)
