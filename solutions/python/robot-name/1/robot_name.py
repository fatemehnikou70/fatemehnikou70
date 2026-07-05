import random
import string

used_names = set()

class Robot:
    def __init__(self):
        self.name = self._generate_name()

    def _generate_name(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = f"{random.randint(0, 999):03}"
            name = letters + numbers

            if name not in used_names:
                used_names.add(name)
                return name

    def reset(self):
        self.name = self._generate_name()