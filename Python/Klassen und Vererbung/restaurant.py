class Restaurant:
    """The __init__() method should generate 3 attributes: restaurant_name, cuisine, city."""
    def __init__(self, restaurant_name, cuisine, city, open):
        self.restaurant_name = restaurant_name.capitalize()
        self.cuisine = cuisine
        self.city = city
        self.open = False
    
    def describe_restaurant(self):
        """Prints all information about the restaurant in a meaningful sentence."""
        print(f'The restaurant "{self.restaurant_name}" offers {self.cuisine} cuisine in {self.city}.')

    def open_restaurant(self):
        """Open your restaurant for guests."""
        self.open = True
        print(f'{self.restaurant_name} is open.')
         
    def close_restaurant(self):
        """Close your restaurant for guests."""
        self.open = False
        print(f'{self.restaurant_name} is closed.')

class IceCreamShop(Restaurant):
    """A sample class to model an ice cream shop."""
    
    def __init__(self, restaurant_name, cuisine, city, open):
        """Initializes all attributes of the parent class. Adds one additional attribute "flavors"."""
        super().__init__(restaurant_name, cuisine, city, open)
        self.flavors = []
    
    def describe_ice_shop(self):
        """Prints all information about the ice cream shop in a meaningful sentence."""
        print(f'The ice cream shop "{self.restaurant_name}" offers {self.cuisine} cuisine in {self.city}.')
        
    def list_flavors(self):
        """List available ice cream flavors."""
        self.flavors = ["strawberry", "chocolate", "vanilla"]
        print(f'The flavors are: {self.flavors}')