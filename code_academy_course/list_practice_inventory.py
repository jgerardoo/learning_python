inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
print(inventory)

# how many items in the warehouse
inventory_len = len(inventory)
print(inventory_len)
print()

# Select the first element in inventory
first = inventory[0]
print(first)
print()

# Select the last element in inventory
last = inventory[-1]
print(last)
print()

# Select items from the inventory starting at index 2 and up to, but not including, index 6
inventory_2_6 = inventory[2:6]
print(inventory_2_6)
print()

# Select the first 3 items of inventory
first_3 = inventory[:3]
print(first_3)
print()

# How many "twin bed" are in inventory?
twin_beds = inventory.count("twin bed")
print(twin_beds)
print()

# Remove the 5th element in the inventory
removed_item = inventory.pop(4)
print(removed_item)
print()

# Add new item to inventory at 11th position
inventory.insert(10, "19th Century Bed Frame")
print(inventory)
print()

# Sort inventory using the .sort()
inventory.sort()
print(inventory)