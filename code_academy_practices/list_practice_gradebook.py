# Last semester grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Current grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# Add new grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

# Add extra 5 point to "Visual arts"
gradebook[5][1] = gradebook[5][1] + 5
print(gradebook)

# Remove the numeric value for "Poetry"
gradebook[2].remove(85)
print(gradebook)

# Add a "Pass/Fail" result for "Poetry"
gradebook[2].append("Pass")
print(gradebook)

# Combine your results with last semester grades
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
print()