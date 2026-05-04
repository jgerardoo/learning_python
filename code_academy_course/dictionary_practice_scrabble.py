# letters and points lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# create a letter_to_points list
letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)
print()

# Add an element into letter_to_points for blank tiles
letter_to_points[" "] = 0
print(letter_to_points)
print()

# Create a function to calculate word points
## I've added a line to also accept lowercase letters
def score_word(word):
  word_total_points = 0
  index = 0
  for letter in word:
    letter = word[index].upper()
    index += 1
    word_total_points += letter_to_points.get(letter, 0)
  return word_total_points

# Test the function
brownie_points = score_word("BROWNIE")
shoe_points = score_word("shoe")

# BROWNIE to earn 15 points
print(f"The word 'BROWNIE' scores {brownie_points} points")
# shoe to earn 7 points
print(f"The word 'shoe' scores {shoe_points} points")
print()

# Create a dictionary to map players to words used
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)
print()

# Create an empty dictionary called player_to_points
player_to_points = {}
print(player_to_points)
print()

# Calculate player points and add each player to the player_to_points dictionary
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Print the results
print("Round 1 results:")
print(player_to_points)
print()

# Add a word to the list of words a player has played
def play_word(player, word):
  player_to_words[player].append(word)
  # player_to_words.update({player: word})

# Add one word per player
print("One more word per player:")
play_word("player1", "ZOO")
play_word("wordNerd", "EAGLE")
play_word("Lexi Con", "PHONE")
play_word("Prof Reader", "WATER")
print(player_to_words)
print()

# Create a function to call any time a word is played
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# Print Round 2 results
update_point_totals()
print("Round 2 results:")
print(player_to_points)
print()