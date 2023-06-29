# Acai Bowl Randomizer

This program generates a random order for an acai bowl from SweetBerry Bowls. The user can also choose to "build their own bowl" by customizing various components of the bowl.

## Getting Started

To run this program, ensure you have Python installed on your machine. Simply execute the code using a Python interpreter. You will be prompted to enter your name, and then the program will generate a randomized acai bowl order.

```python
python random_acai_bowl.py
```

## Prerequisites

This program requires the following:

- Python 3.x

## Usage

Upon running the program, it will ask for your name and then display your randomized acai bowl order. The order consists of the following components:

- Size: Junior Bowl or Regular Bowl
- Base: Pitaya Bowl, Acai Bowl, or Coconut Bowl
- Drizzle: Honey, Agave, Peanut Butter, Nutella, or Almond Butter
- Toppings: Up to four toppings randomly selected from a predefined list

The program includes the following functions:

- `size_decider(number: int) -> str`: Decides the size of the bowl based on a random number.
- `base_decider(number: int) -> str`: Decides the base of the bowl based on a random number.
- `drizzle_decider(number: int) -> str`: Decides if and what drizzle to include based on a random number.
- `topping_selector(toppings: list[str]) -> list[str]`: Selects up to four toppings randomly from a predefined list.

## TODO

The following tasks are yet to be implemented:

- Function for Immunity booster (yes/no: single or double dose)
- Function for Fruit (up to three) [Strawberry, Banana, Kiwi, Blueberry, Mango, Pineapple]
- Class or function to determine the price of the bowl

## Author

This program was developed by Carmine Anderson - Falconi.