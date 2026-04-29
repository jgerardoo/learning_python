# Add the imports needed
from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module as cm

# Get the current date and time
now = dt.now()
print(f"The current datetime is {now}")

# Get only current date and current time
current_date = now.date()
current_time = now.time()
print(f"The current date is {current_date}")
print(f"The current time is {current_time}")

# Generate a random target date (year)
year = randint(500, 3000)
print(f"The target date is {year}")

# Create a base cost
base_cost = Decimal("500.00")
print(f"The base cost is ${base_cost}")

# Determine a cost multiplier
cost_multiplier = Decimal(abs(now.year - year))
print(f"The cost multiplier is ${cost_multiplier}")

# Calculate the final cost, ensure two decimal places
cost = base_cost + cost_multiplier
cost = cost.quantize(Decimal('0.01'))
print(f"The final cost is ${cost}")

# List of possible destinations for the time travel
destinations = ["Mexico", "USA", "France", "China"]

# Randomly select one destination from the list
destination = choice(destinations)
print(f"The destination is {destination}")
print()

# Print the message using the function imported
print(cm.generate_time_travel_message(cost, destination, year))