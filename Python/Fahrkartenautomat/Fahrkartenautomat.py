import json

# Welcome message
print("Herzlichen Willkommen bei Ihrer Bahn, sie haben folgende Fahrkarten zur Auswahl:")

print()

# Read ticket data from the "tickets.json" file
with open("tickets.json", "r") as file:
    tickets = json.load(file)

    # Display the available ticket options
    for ticket_num, ticket in enumerate(tickets['tickets']):
        print(f'{ticket_num} {ticket["name"]}')

print()

# Get the user's choice of ticket
choice = int(input("Bitte geben sie die entsprechende Zahl für die gewünschte Fahrkarte ein: "))

print()

# Check if the user's choice is valid
if choice < 0 or choice >= len(tickets["tickets"]):
    print("Ungültige Auswahl. Programm wird abgebrochen.")
    exit()

# Display the selected ticket
print(f'Sie haben sich für "{tickets["tickets"][choice]["name"]}" entschieden')

print()

# Display accepted payment options
print("Dieser Automat akzeptiert folgende Münzen und Geldscheine:")

print()

for x in tickets["accepted_cash"]:
    print(f'{x} Euro')

total_paid = 0

# Handle payment until the required amount is reached
while total_paid < tickets["tickets"][choice]["price"]:
    print()
    print(
        "Bitte werfen sie eine Münze/einen Geldschein ein, es fehlen noch",
        tickets["tickets"][choice]["price"] - total_paid,
        "Euro.",
    )
    current_paid = int(input())
    if current_paid in tickets["accepted_cash"]:
        print()
        print("Danke für", current_paid, "Euro.")
        total_paid += current_paid
    else:
        print()
        print(
            "Leider akzeptieren wir die Münze/den Geldschein nicht, bitte werfen sie etwas anderes ein."
        )
print()

# Calculate and display any change
if total_paid > tickets["tickets"][choice]["price"]:
    print(
        "Ihr Restgeld beträgt",
        total_paid - tickets["tickets"][choice]["price"],
        "Euro.",
    )
print("Danke für ihren Einkauf und gute Fahrt.")