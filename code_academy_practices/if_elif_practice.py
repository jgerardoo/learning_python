# ---------- PRACTICE ----------
# Little Codey is an interplanetary space boxer who is trying to win championship belts
# for various weight categories on other planets within the solar system.
# Write a program that helps Codey keep track of their target weight by:
# 1. Checking which number planet is equal to.
# 2. Computing Codey’s weight on the destination planet.

# Here is the table of conversions:
#   No.     Planet      Relative Gravity
#   1        Venus      0.91
#   2	     Mars     	0.38
#   3        Jupiter    2.34
#   4	     Saturn	    1.06
#   5        Uranus     0.92
#   6        Neptune	1.19

# Message intro
print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
weight = 185
planet = 3

# If statement
if planet == 1:
  venus_weight = weight * 0.91
  print(f"Your weight in Venus is {venus_weight} lbs")
elif planet == 2:
  mars_weight = weight * 0.38
  print(f"Your weight in Mars is {mars_weight} lbs")
elif planet == 3:
  jupiter_weight = weight * 0.91
  print(f"Your weight in Jupiter is {jupiter_weight} lbs")
elif planet == 4:
  saturn_weight = weight * 0.91
  print(f"Your weight in Saturn is {saturn_weight} lbs")
elif planet == 5:
  uranus_weight = weight * 0.91
  print(f"Your weight in Uranus is {uranus_weight} lbs")
elif planet == 6:
  neptune_weight = weight * 0.91
  print(f"Your weight in Neptune is {neptune_weight} lbs")