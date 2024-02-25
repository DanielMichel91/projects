from restaurant import *

# Create an instance of the Restaurant class
da_Bippo = Restaurant("da Bippo", "Italian", "Frankfurt", "open")

# Use the methods of the Restaurant class
da_Bippo.describe_restaurant()
da_Bippo.open_restaurant()
da_Bippo.close_restaurant()

# Create an instance of the IceCreamShop class
the_ice_shop = IceCreamShop("the Ice Shop", "Italian", "Verona", "open")

# Use the methods of the IceCreamShop class
the_ice_shop.describe_ice_shop()
the_ice_shop.describe_restaurant()
the_ice_shop.list_flavors()