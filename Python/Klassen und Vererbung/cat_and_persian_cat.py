class Cat:
    """A sample class to model a cat."""
    def __init__(self, name, color):
        """Initialize name and color attributes."""
        self.name = name.capitalize()
        self.color = color

    def eat(self):
        """Simulate a cat eating."""
        print(f'{self.name} is eating.')

    def meow(self):
        """Simulate a cat meowing."""
        print(f'{self.name}: "MEOOOOW!')

# Create an instance of the Cat class
simba = Cat("simba", "brown")

# Access attributes and call methods
print(f'My cat is called {simba.name}.')
print(f'My cat is {simba.color}.')
simba.eat()
simba.meow()

# Create two more instances of the Cat class
malu = Cat("malu", "black")
luna = Cat("luna", "white")

# Call meow method for each cat
simba.meow()
malu.meow()
luna.meow()

class PersianCat(Cat):
    """A sample class to model a Persian cat."""

    def __init__(self, name, color):
        """
        Initializes attributes of the parent class.
        Adds two additional attributes specific for Persian cats.
        """
        super().__init__(name, color)
        self.fur_length = 10
        self.fur_brushed = False

    def brush_fur(self):
        """Brushes the fur and changes the value to True."""
        self.fur_brushed = True
        print(f'{self.name}\'s fur is now brushed.')

    # Overwriting methods from the parent class
    def meow(self):
        """Persian cats meow slightly differently."""
        print(f'{self.name}: "YOOOWL!')

# Create an instance of the PersianCat class
oliver = PersianCat("oliver", "brown")

# Access attributes and call methods specific to PersianCat
print(oliver)
oliver.eat()
print(oliver.fur_brushed)
oliver.brush_fur()
print(oliver.fur_brushed)
oliver.meow()

# Example using TextBlob and DataFrame
from textblob import TextBlob
sample_textblob = TextBlob("A sample text is better than none.")
print(dir(sample_textblob))
print(sample_textblob.words)

from pandas import DataFrame
data_dict = {'name': ["mark", "pia"], 'age': [35, 26]}
df = DataFrame(data=data_dict)
print(dir(df))