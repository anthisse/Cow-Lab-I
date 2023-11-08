"""Specification for Dragon object"""

from cow import Cow


class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        Dragon.set_image(self, image)

    @staticmethod
    def can_breathe_fire():
        return True
