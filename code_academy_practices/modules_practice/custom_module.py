# Define a function named generate_time_travel_message.
# This function should accept three parameters: year, destination, and cost.
# The function should return a formatted string that incorporates the provided year, destination, and cost
# to create a message about the time travel experience.

def generate_time_travel_message(cost, destination, year):
  message = f"Pack your bags! You're traveling to {destination} in the year {year}. The cost of this trip will be ${cost}."
  return message