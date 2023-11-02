"""Cow class passed to cowsay.py"""


class Cow:
    def __init__(self, name):
        self.name = name
        self.image = None

    # Get the name
    def get_name(self):
        return self.name

    # Get the image
    def get_image(self):
        return self.image

    # Set the image
    def set_image(self, image):
        self.image = image
