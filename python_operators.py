# Arithmetic Operators: Used to perform mathematical calculations like addition, subtraction, multiplication, and division.
# Assignment Operators: Used to assign values to variables and update them with operations.
# Comparison Operators: Used to compare two values and return a Boolean result (True or False).
# Logical Operators: Used to combine multiple conditions and return a Boolean outcome.
# Bitwise Operators: Used to perform operations at the binary (bit) level on integers.
# Membership Operators: Used to test whether a value exists within a sequence such as a list or string.
# Identity Operators: Used to check whether two variables refer to the exact same object in memory

# Arithmetic Operators
# Shopping cart total calculation
item_price = 25.99
quantity = 3
tax_rate = 0.08
# Calculate subtotal using multiplication
subtotal = item_price * quantity
# Calculate tax using multiplication
tax_amount = subtotal * tax_rate
# Calculate total using addition
total = subtotal + tax_amount
# Calculate change from $100 using subtraction
payment = 100.00
change = payment - total
# Display results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax_amount:.2f}")
print(f"Total: ${total:.2f}")
print(f"Change: ${change:.2f}")
print("-----------------------------")

# Assignment Operators
# Initial account balance
account_balance = 1000.00
# Deposit money using addition assignment
deposit_amount = 250.00
account_balance += deposit_amount
print(f"After deposit: ${account_balance:.2f}")
# Withdraw money using subtraction assignment
withdrawal_amount = 75.00
account_balance -= withdrawal_amount
print(f"After withdrawal: ${account_balance:.2f}")
# Apply monthly interest using multiplication assignment
monthly_interest_rate = 1.005  # 0.5% interest
account_balance *= monthly_interest_rate
print(f"After interest: ${account_balance:.2f}")
# Calculate service fee using division assignment
service_fee_rate = 0.02  # 2% service fee
fee_amount = account_balance
fee_amount *= service_fee_rate
account_balance -= fee_amount
print(f"Final balance: ${account_balance:.2f}")
print("-----------------------------")

# Comparison Operators
# Student test scores
student_score = 87
passing_score = 60
honor_roll_score = 90
perfect_score = 100
# Check if student passed using greater than or equal
passed = student_score >= passing_score
print(f"Student passed: {passed}")
# Check if student made honor roll using greater than or equal
honor_roll = student_score >= honor_roll_score
print(f"Honor roll: {honor_roll}")
# Check if student got perfect score using equal
perfect = student_score == perfect_score
print(f"Perfect score: {perfect}")
# Check if student needs improvement using less than
needs_improvement = student_score < passing_score
print(f"Needs improvement: {needs_improvement}")
# Compare with class average
class_average = 82
above_average = student_score > class_average
print(f"Above class average: {above_average}")
print("-----------------------------")

# Logical Operators
# User credentials and permissions
user_authenticated = True
user_role = "admin"
account_active = True
maintenance_mode = False
# Check if user can access admin panel using 'and'
admin_access = user_authenticated and user_role == "admin" and account_active
print(f"Admin access granted: {admin_access}")
# Check if user can access system using 'or'
basic_access = user_authenticated and account_active or user_role == "guest"
print(f"Basic access granted: {basic_access}")
# Check if system is available using 'not'
system_available = not maintenance_mode and account_active
print(f"System available: {system_available}")
# Complex access control logic
full_access = (user_authenticated and account_active) and (user_role == "admin" or user_role == "moderator") and not maintenance_mode
print(f"Full access granted: {full_access}")
print("-----------------------------")

# Identity Operators
# Creating different types of objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
# Check if lists are the same object using 'is'
same_object = list1 is list3
print(f"list1 is list3: {same_object}")
# Check if lists are different objects using 'is'
different_objects = list1 is list2
print(f"list1 is list2: {different_objects}")
# Check if lists are not the same object using 'is not'
not_same_object = list1 is not list2
print(f"list1 is not list2: {not_same_object}")
# Common use case: checking for None
user_data = None
no_data = user_data is None
print(f"No user data: {no_data}")
# After loading data
user_data = {"name": "John", "age": 30}
has_data = user_data is not None
print(f"Has user data: {has_data}")
print("-----------------------------")

# Membership Operators
# Content filtering for a social media platform
blocked_words = ["spam", "scam", "fake", "virus"]
user_message = "This is a legitimate message about our product"
suspicious_message = "This is a spam message with fake offers"
# Check if message contains blocked words using 'in'
contains_blocked = any(word in user_message.lower() for word in blocked_words)
print(f"Message contains blocked words: {contains_blocked}")
# Check specific word using 'in'
has_spam = "spam" in suspicious_message.lower()
print(f"Message contains 'spam': {has_spam}")
# Check if word is not in blocked list using 'not in'
safe_word = "Product"
is_safe = safe_word not in blocked_words
print(f"'{safe_word}' is safe to use: {is_safe}")
# Check user permissions
allowed_users = ["admin", "moderator", "verified_user"]
current_user = "regular_user"
has_permission = current_user in allowed_users
print(f"User has permission: {has_permission}")
# Check if user is not in banned list
banned_users = ["spammer123", "troll456"]
is_banned = current_user in banned_users
print(f"User is banned: {is_banned}")
print("-----------------------------")

# Bitwise Operators
# Permission flags for a file system
READ = 4        # 100 in binary
WRITE = 2       # 010 in binary
EXECUTE = 1     # 001 in binary
# User permissions using bitwise OR to combine flags
user_permissions = READ | WRITE  # 110 in binary (6 in decimal)
print(f"User permissions: {user_permissions}")
# Check if user has read permission using bitwise AND
has_read = bool(user_permissions & READ)
print(f"Has read permission: {has_read}")
# Check if user has write permission using bitwise AND
has_write = bool(user_permissions & WRITE)
print(f"Has write permission: {has_write}")
# Check if user has execute permission using bitwise AND
has_execute = bool(user_permissions & EXECUTE)
print(f"Has execute permission: {has_execute}")
# Add execute permission using bitwise OR
user_permissions = user_permissions | EXECUTE
print(f"Updated permissions: {user_permissions}")
# Remove write permission using bitwise XOR
user_permissions = user_permissions ^ WRITE
print(f"After removing write: {user_permissions}")
# Double a number using left shift (equivalent to multiplying by 2)
number = 5
doubled = number << 1
print(f"{number} doubled using left shift: {doubled}")
print("-----------------------------")