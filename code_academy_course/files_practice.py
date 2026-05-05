# Import both the csv and the json modules
import csv
import json

# Create a list of users whose passwords have been compromised
compromised_users = []

# Open the file with the data
with open("files_for_practice/passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)                                    # Pass the password_file object holder to our CSV reader for parsing
    for row in password_csv:                                                        # save each row of the CSV into a variable
        compromised_users.append(row["Username"])                                   # add each username to the list of compromised_users

# Open a new file in write mode for compromised_users
with open("files_for_practice/compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:                                                  # Iterate over each of your compromised_users
        compromised_user_file.write(user)                                           # Write each compromised_user in compromised_user_file
        compromised_user_file.write("\n")                                           # Added the jump so that each user is in a separate line

# Notifying the Boss
# Open a new JSON file in write-mode
with open("files_for_practice/boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}     # Create a Python dictionary object with key and value
    json.dump(boss_message_dict, boss_message)                                      # Write out the dictionary into the JSON file

# Scrambling the Password
slash_null_sign = """YOU 
WERE
HACKED"""                                                                           # Save the hacker signature as a multi line string
with open("files_for_practice/new_passwords.csv", "w") as new_passwords_obj:        # Create a new csv file in write-mode
    new_passwords_obj.write(slash_null_sign)                                        # Write the signature to the csv file created