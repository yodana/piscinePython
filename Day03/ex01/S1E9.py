from abc import ABC, abstractmethod


class Character(ABC):

    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Init the name and is alive"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Init the Character Stark"""
        super().__init__(name, is_alive)

    def die(self):
        """Give death of the character"""
        self.is_alive = False
