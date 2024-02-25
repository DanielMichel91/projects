# Define two lists
list1 = [10, 21, 45, 66, 78]
list2 = [10, 22, 46, 66, 78, 90]

# Find the symmetric difference and convert it to a sorted list
set_difference = set(list1).symmetric_difference(set(list2))
sym_difference = list(set_difference)
sym_difference.sort()

# Print the symmetric difference
print(sym_difference)

# Find the common elements and convert them to a sorted list
set_common = set(list1).intersection(set(list2))
common_value = list(set_common)
common_value.sort()

# Print the common elements
print(common_value)

# Define information about two hotels
hotel_Marrios = {
    "name": "Marrios",
    "age": 1991,
    "payment_options": ["card", "cash", "online"],
    "available_rooms": [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night": 50,
    "employees": ["carlo", "maria", "marta", "luis", "fernando"]
}

hotel_hilten = {
    "name": "hilten",
    "age": 1992,
    "payment_options": ["card", "online"],
    "available_rooms": [100, 800, 801, 805, 1000, 1001],
    "price_per_night": 70,
    "employees": ["artur", "maria", "oliver", "xenia"]
}

# Calculate the cost of staying at each hotel for five nights
nights = 5
cost_marrios = hotel_Marrios["price_per_night"] * nights
cost_hilten = hotel_hilten["price_per_night"] * nights

# Determine the cheaper hotel and calculate the price difference
if cost_marrios > cost_hilten:
    diff = cost_marrios - cost_hilten
    guenstigeres_hotel = "hotel Marrios"
else:
    diff = cost_hilten - cost_marrios
    guenstigeres_hotel = "hotel hilten"

# Print the result
print(f'{guenstigeres_hotel} ist das günstigere hotel und der Preisunterschied liegt bei: {diff}€.')
print(f'Fünf Übernachtungen kosten {cost_marrios}€ im hotel Marrios und {cost_hilten}€ im hotel Hilten. Der Preisunterschied sind {diff}€.')

# Find the intersection of available rooms in both hotels and convert it to a list
room_numbers = set(hotel_Marrios["available_rooms"]).intersection(set(hotel_hilten["available_rooms"]))
list_numbers = list(room_numbers)

# Print the available room numbers in both hotels
print(f'Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren : {list_numbers}? Danke.')

# Find the number of payment options in each hotel
print(f'Im Hotel Marrios gibt es {len(hotel_Marrios["payment_options"])} und im hotel Hilten gibt es {len(hotel_hilten["payment_options"])} Zahlungsmöglichkeiten.')

# Find the symmetric difference in payment options and convert it to a list
pay_diff = set(hotel_Marrios["payment_options"]).symmetric_difference(set(hotel_hilten["payment_options"]))
list_diff = list(pay_diff)

# Print the differences in payment options
print(f'Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten: {list_diff}.')

# Check in which hotel is "fernando" is working and decide to stay there
if "fernando" in hotel_hilten["employees"]:
    print(f'Fernando arbeitet im Hotel {hotel_hilten["name"]}, daher übernachte ich dort.')
else:
    print(f'Fernando arbeitet im Hotel {hotel_Marrios["name"]}, daher übernachte ich dort.')