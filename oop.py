import random

class Character:
    hair_colors = ["Blonde", "Ginger", "Black", "Teal"]
    sizes = ["Tiny", "Medium", "Large"]
    height = ["Small", "Avarage", "Tall"]
    hair_type = ["Straight", "Wavy", 'Curly']
    gender = ["Male", "Female"]

    #Constructor
    def __init__(self):
        self.generate_character()

    def generate_character():
        self.hair_colors = random.choice(Character.hair_colors)
        self.sizes = random.choice(Character.sizes)
        self.height = random.choice(Character.height)
        self.hair_type = random.choice(Character.hair_type)
        self.gender = random.choice(Character.gender)
        self.description = (
            f"Your character had {self.hair_colors} with {self.hair_type} hair, "
            f"is {self.sizes} in size, "
            f"is {self.height} in height,"
            f"and is a {self.gender}."
        )
    
    def __str__(self):
        return self.description


char1 = Character()
char2 = Character()

print(char1)
print(char2)