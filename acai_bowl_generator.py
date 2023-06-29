"""Program using random to create a random order of acai bowl from sweetberry bowls."""
"""Once selecting the "build your own bowl"."""

from random import randint
hunger_level: int = randint(0, 1)
random_base: int = randint(0, 10)
random_drizzle: int = randint(0, 10)

name: str = input("What is your name?")
print(f"Hello {name}, here is your randomized acai bowl order...") 
print("\n")

# Functions to configure and choose the outcomes of the different parts of the bowl. 
def size_decider(number: int) -> str:
    """Decides the size of the bowl."""
    if number == 0:
        return "Junior Bowl"
    else: 
        return "Regular Bowl"

def base_decider(number: int) -> str:
    """Function to decide the base of a bowl."""
    if number <= 3:
        return "Pitaya Bowl"
    elif number <= 7:
        return "Acai Bowl"
    elif number > 7:
        return "Coconut Bowl"

def drizzle_decider(number: int) -> str:
    """Function to decide if and what drizzle."""
    if number % 2 != 0:
        ...
    else:
        if number <= 2:
            return "Honey"
        elif number <= 4:
            return "Agave"
        elif number <= 6:
            return "Peanut Butter" 
        elif number <= 8:
            return "Nutella"
        elif number > 8:
            return "Almond Butter"
    
def topping_selector(toppings: list[str]) -> list[str]:
    """Function for selecting toppings for your bowl."""
    random_topping_int: int = randint(1, 4)
    result: list[str] = []
    i: int = 0
    while i < len(toppings):
        if len(result) == 4 or i == len(toppings):
            return result
        elif i % random_topping_int == 2:
            result.append(toppings[i])
        i += 1 

#TODO function for Immunity booster (yes/no: single or double dose)

#TODO Function for Fruit (up to three) [Strawberry, Banana, Kiwi, Blueberry, Mango, Pineapple]

#TODO Class or function to decide price

# Global variables that will be pulled and brought into the bowl constructor.
size: str = size_decider(hunger_level)
base: str = base_decider(random_base)
drizzle: str = drizzle_decider(random_drizzle)
toppings: list[str] = [
    "Craisins", "Almonds", "Granola",
    "Whey Choc Protein", "Kale", "Whey Vanilla Protein",
    "Pumpkin Seeds", "Walnuts", "Spirulina",
    "Spinach", "Flax Oil", "Coconut Flakes",
    "Goji Berries", "Bee Pollen", "Hemp Seeds",
    "Chia Seeds", "Cocao Nibs", "Nutella",
    "Peanut Butter", "Agave", "Honey",
    "Pineapple", "Mango", "Blueberry",
    "Kiwi", "Banana", "Strawberry",
    "Glutten Free Granola"
]
topping_list: list[str] = topping_selector(toppings)

# Class that constucts the bowl
class Bowl:
    number: int = random_base
    base: str

    def __init__(self, number: int, base: str):
        """Constructor of the bowl."""
        #self.base = base_decider(number)




# Need a class to determine the price

print(topping_list)