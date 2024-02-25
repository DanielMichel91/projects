from datetime import datetime
import pytz

# Get the German timezone
german_tz = pytz.timezone("Europe/Berlin")

# Get the current time in Germany
time_in_ger = datetime.now(german_tz)

# Format the current time as "HH:MM"
current_time_in_ger = time_in_ger.strftime("%H:%M")

class Supermarket:
    """Class to represent a supermarket."""
    def __init__(self, name, street, city):
        """Initialize supermarket attributes."""
        self.name = name.title()
        self.street = street.title()
        self.city = city.title()
        self.employees = []
        self.products = []

class Employee:
    """Class to represent an employee."""
    def __init__(self, name, age, pers_id, job):
        """Initialize employee attributes."""
        self.name = name
        self.age = age
        self.pers_id = pers_id
        self.job = job

    def greet_customer(self):
        """Greet a customer and provide assistance."""
        print(f'Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {current_time_in_ger} Uhr - wie kann ich Ihnen helfen?')
    
    def celebrate_birthday(self):
        """Celebrate the employee's birthday."""
        self.age += 1
        print(f'Juhu! Heute werde ich {self.age} Jahre!')

class Product:
    """Class to represent a product in the supermarket."""
    def __init__(self, name, prod_id, category, price):
        """Initialize product attributes."""
        self.name = name.title()
        self.prod_id = prod_id
        self.category = category.lower()
        if category != "food" and category != "drinks":
            self.category = "others"
        self.price = price

    def apply_discount(self, discount):
        """Apply a discount to the product price."""
        self.discount = discount
        if discount >= 0 and discount <= 100:
            new_price = self.price * (1 - (discount / 100))
            print("The discounted price is:", round(new_price, 2), "€")
            self.price = new_price
        else:
            new_price = self.price * (1 - (5 / 100))
            print(f'Warning, the input was incorrect. You get a 5% discount, so the discounted price is: {new_price} €')
            self.price = new_price