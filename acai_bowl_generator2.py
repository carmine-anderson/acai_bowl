"""Program using random to create a random order of acai bowl from sweetberry bowls."""
"""Once selecting the "build your own bowl"."""

from random import randint
from typing import Union

# Randomized integers
hunger_level: int = randint(0, 1)
random_base: int = randint(0, 10)
random_drizzle: int = randint(0, 10)
random_immunity: int = randint(0, 1)
double_immunity: int = randint(0, 1)
random_fruit: int = randint(0, 3)
fruit_first_random: int = randint(0, 5)

#customer_name: str = input("What is your name?")
#print(f"Hello {customer_name}, here is your randomized acai bowl order...") 
print("\n")

##### FUNCTIONS #####

# Function to decide the size of your bowl.
def size_decider(number: int) -> str:
    """Decides the size of the bowl."""
    if number == 0:
        return "Junior Bowl"
    else: 
        return "Regular Bowl"

# Function to decide the base of your bowl. 
def base_decider(number: int) -> str:
    """Function to decide the base of a bowl."""
    if number <= 3:
        return "Pitaya"
    elif number <= 7:
        return "Acai"
    elif number > 7:
        return "Coconut"

# Function to select a drizzle for your bowl.
def drizzle_decider(number: int) -> str:
    """Function to decide if and what drizzle."""
    if number % 2 != 0:
        return "No"
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

# Function to create a randomized selection of toppings for your bowl.
def topping_selector(toppings: list[str]) -> list[str]:
    """Function for selecting toppings for your bowl."""
    random_topping_int: int = randint(1, 4)
    random_topping_int2: int = randint(1, 28)
    random_topping_int3: int = randint(1, 14)
    random_topping_int4: int = randint(15,28)
    result: list[str] = []
    i: int = 0
    while i < len(toppings):
        if len(result) == 4:
            return result
        if i == len(toppings):
            return result
        elif i % random_topping_int == 1:
            if toppings[i] in result:
                ...
                # DO NOTHING
            else:
                result.append(toppings[random_topping_int + 2])
        elif toppings[i] not in result:
            if i % random_topping_int == 0:
                result.append(toppings[random_topping_int3])
            else:
                result.append(toppings[random_topping_int4 - random_topping_int3])
        i += 1 + random_topping_int
        random_topping_int += 1
        random_topping_int2 -= 1
        random_topping_int3 += 1
        random_topping_int4 -= 3

    return result

# Function for Immunity booster (yes/no: single or double dose)
def immunity(number: int, second_number: int) -> str:
    """."""
    the_immunity: str = ""
    count: str = ""
    answer: bool = False
    i: int = 0
    if answer == False:
        while i == 0:
            if number == 0:
                return "No Immunity"
            elif number == 1:
                the_immunity = "Immunity Booster"
                if second_number == 0:
                    count = "Single"
                elif second_number == 1:
                    count = "Double"
            i = 1
        answer = True
    return f"{count} {the_immunity}"

# Function for Fruit (up to three) [Strawberry, Banana, Kiwi, Blueberry, Mango, Pineapple]
def fruit_selector(fruits: list[str], number: int) -> Union[str, list[str]]:
    """Fruit Selector."""
    global fruit_first_random
    result: list[str] = []
    i: int = 1

    if number == 0:
        return "No Fruit"
    if number > 0:
        result.append(fruits[fruit_first_random])

    while len(result) < 3:
        if i * number == 2:
            result.append(fruits[i + 1])
            i += 2 - number
        elif fruits[i] not in result:
            result.append(fruits[i])
        i += 1
        
    j: int = len(result) - 1
    while j > 3:
        result.pop(-1)
    
    return result
 
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
immunity_booster: str = immunity(random_immunity, double_immunity)
fruits: list[str] = [
    "Strawberry",
    "Banana", 
    "Kiwi", 
    "Blueberry", 
    "Mango", 
    "Pineapple"
]
fruit_list: list[str] = fruit_selector(fruits, random_fruit)

# Class that constucts the bowl
class Sweetberry_Bowl:
    size: str
    base: str
    drizzle: str
    toppings: list[str]
    immunity_booster: str
    fruits: Union[str, list[str]]
    price: int 

    def __init__(self, size: str, base: str, drizzle: str, toppings: list[str], immunity_booster: str, fruits: Union[str, list[str]]):
        """Constructor of the bowl."""
        self.size = size
        self.base = base
        self.drizzle = drizzle
        self.toppings = toppings
        self.immunity_booster = immunity_booster
        self.fruits = fruits

    def price(self) -> float:
        """Method to determine the price of your bowl based on ingredients."""
        price: float = 0.0

        # Size
        if self.size == "Junior Bowl":
            price += 5.0
        else: 
            price += 7.0

        # Base
        if self.base == "Pitaya Bowl":
            price += 0.50
        elif self.base == "Acai Bowl":
            price += 1.75
        elif self.base == "Coconut Bowl":
            price += 1.00

        # Drizzle
        if self.drizzle == "No":
            price += 0.0
        elif self.drizzle == "Honey":
            price += 1.00
        else:
            if self.drizzle == "Nutella":
                price += 1.00
            else:
                price += 0.50

        # Toppings
        i: int = 0
        while i < len(self.toppings):
            price += 0.50
            i += 1

        # Immunity Booster
        j: int = 0
        if self.immunity_booster[j] == "N":
            price += 0.0
        else:
            if self.immunity_booster[j] == "S":
                price += 1.0
            else:
                if self.immunity_booster[j] == "D":
                    price += 2.0

        # Fruits
        a: int = 0
        if self.fruits == "No Fruit":
            price += 0.0
        else:
            while a < len(self.fruits):
                price += 0.50
                a += 1

        # Consumer Tax
        price *= 1.05

        self.price = price

        return self.price

my_bowl: Sweetberry_Bowl = Sweetberry_Bowl(size, base, drizzle, topping_list, immunity_booster, fruit_list)
price_of_bowl: float = my_bowl.price()

# CREATE print statement of the bowl with the customers name, ingredient, and price of the bowl
print(f"The size of your bowl will be a {size} and have a {base} base.")
print(f"There will be {drizzle} drizzle.")
print(f"Your toppings are: {topping_list}.")
print(f"You will have {immunity_booster}.")
print(f"And finally these fruits: {fruit_list}.")
print(f"The price of your bowl will be ${price_of_bowl}.")
print("\n")