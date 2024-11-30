from pathlib import Path
from flask import current_app
from uuid import uuid4


class ImageHandler:

    @staticmethod
    def save_image(image):
        if not image:
            return None
        # suffix of a.png is png. suffix of h.jpeg is jpeg
        suffix = Path(image.filename).suffix
        image_name = str(uuid4()) + suffix  # create unique name
        image_path = Path(current_app.root_path) / "static/images" / image_name
        # save the image on the server side on static/images/122323-323wedwewe--32323-wewe.png
        image.save(image_path)
        return image_name  # return the name because i want to save it on db

    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / "static/images" / image_name
        if not image_path.exists():
            image_path = Path(current_app.root_path) / \
                         "static/images/no-image.png"
        return image_path

    @staticmethod
    def update_image(old_image_name, image):
        if not image.filename: return old_image_name
        image_name = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return image_name

    @staticmethod
    def delete_image(image_name):
        if not image_name: return  # do nothing
        if image_name == "no-image.png":
            return
        image_path = Path(current_app.root_path) / "static/images" / image_name
        image_path.unlink(missing_ok=True)
