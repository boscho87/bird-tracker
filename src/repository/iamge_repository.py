from src.tracker.entity.image import Image


class ImageRepository:


    def save_or_update_image(self, image : Image):


        return image.save()

    def delete_image(self, image: Image):
        return image.delete()
