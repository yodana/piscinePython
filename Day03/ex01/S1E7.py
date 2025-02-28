from S1E9 import Character


class Baratheon(Character):
    """Character Baratheon"""
    def __init__(self, name, is_alive=True):
        """Init the Character Baratheon"""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return "Vector: " + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return "Vector: " + str((self.family_name, self.eyes, self.hairs))

    def die(self):
        """Give death of the character"""
        self.is_alive = False


class Lannister(Character):
    """ Character Lannister """
    def __init__(self, name, is_alive=True):
        """Init the Character Lannister"""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def create_lannister(name, is_alive=True):
        return Lannister(name, is_alive)

    def __str__(self):
        return "Vector: " + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return "Vector: " + str((self.family_name, self.eyes, self.hairs))

    def die(self):
        """Give death of the character"""
        self.is_alive = False
