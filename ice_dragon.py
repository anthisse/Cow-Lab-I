"""Specification for the IceDragon object"""
from dragon import Dragon


class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image)
        IceDragon.set_image(self, image)

    @staticmethod
    def can_breathe_fire():
        return False
