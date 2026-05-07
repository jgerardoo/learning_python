# import the time module to work with times
from datetime import time

# Define a Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Create a Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Add string representation to the Franchise class
    def __repr__(self):
        return self.address

    # Add available menus method to Franchise class
    def available_menus(self, current_time):
        self.menus_available = []
        if current_time >= time(11, 00, 0) and current_time <= time(16, 00, 0):
            self.menus_available.append(brunch.name)
        if current_time >= time(15, 00, 0) and current_time <= time(18, 00, 0):
            self.menus_available.append(early_bird.name)
        if current_time >= time(17, 00, 0) and current_time <= time(23, 00, 0):
            self.menus_available.append(dinner.name)
        if current_time >= time(11, 00, 0) and current_time <= time(21, 00, 0):
            self.menus_available.append(kids.name)
        return f'Available menus at {current_time}: {self.menus_available}'

# Create the Menu class with the parameters: name, items, start_time, and end_time
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # Add a string representation to the Menu class
    def __repr__(self):
        return f'The {self.name} menu is available from {self.start_time} to {self.end_time}'

    # Add a method into the Menu class to calculate the bill
    def calculate_bill(self, purchased_items):
        purchase_total = 0
        for item in purchased_items:
            purchase_total += self.items[item]
        return purchase_total

# Create the Brunch menu
brunch_menu_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('Brunch', brunch_menu_items, time(11, 00, 0), time(16, 00, 0))

# Create the Early bird menu
early_bird_menu_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('Early bird', early_bird_menu_items, time(15, 00, 0), time(18, 00, 0))

# Create the Dinner menu
dinner_menu_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu('Dinner', dinner_menu_items,
              time(17, 00, 0), time(23, 00, 0))

# Create the Kids menu
kids_menu_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('Kids', kids_menu_items, time(11, 00, 0), time(21, 00, 0))

# Testing the Menus
# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)
# print(brunch.items)
# print(brunch.items['pancakes'])

# Calculate a breakfast order
breakfast_bill = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(f"The bill for the breakfast order was ${breakfast_bill}")

# Calculate an Early bird order
early_bird_bill = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
print(f"The bill for the early bird order was ${early_bird_bill}")
print("------------------------------")

# Create two Franchises
flagship_store = Franchise('1232 West End Road', [brunch.name, early_bird.name, dinner.name, kids.name])
new_installment = Franchise('12 East Mulberry Street', [brunch.name, early_bird.name, dinner.name, kids.name])

# Testing the Franchises
# print(flagship_store)
# print(flagship_store.menus)

# Get the menus available at 12 noon
print(flagship_store.available_menus(time(12, 00, 0)))

# Get the menus available at 5 pm
print(flagship_store.available_menus(time(17, 00, 0)))
print('------------------------------')

# Create a Business
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Arepas stuff
## Arepas menu
arepas_menu_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a' Arepa", arepas_menu_items, time(10, 00, 0), time(20, 00, 0))

## Arepas franchise
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

## Arepas business
take_arepa = Business("Take a' Arepa", [arepas_place])

# Testing the Businesses
# print(take_arepa)
# print(take_arepa.name)
# print(take_arepa.franchises)
# print(arepas_place.menus)