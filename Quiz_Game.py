print("Welcome to this comouter quiz game:) ")
user_input = str(input("Do you wnat to play this game. "))

if user_input.lower() != "yes":
   quit()

print("Okay, Then Let's Play:)")
score = 0
print("You will get 5 questions in this quiz:")

# This is 1 questions.
answer = input("Q1 What does CPU stand for? ")
if answer.lower() == "Central Processing Unit".lower():
   print("Correct")
   score = score + 1
else:
   print("Worng")

# This is 2 questions.
answer = input("Q2 Which computer device is primarily used for inputting data by typing? ")
if answer.lower() == "Keyboard".lower():
   print("Correct")
   score = score + 1
else:
   print("Worng")

   # This is 3 questions.
answer = input("Q3 What does GUI stand for? ")
if answer.lower() == "Graphical User Interface".lower():
   print("Correct")
   score = score + 1
else:
   print("Worng")

   # This is 4 questions.
answer = input("Q4 What does URL stand for? ")
if answer.lower() == "Uniform Resource Locator".lower():
   print("Correct")
   score = score + 1
else:
   print("Worng")

   # This is 5 questions.
answer = input("Q5 Which operating system is developed by Microsoft? ")
if answer.lower() == "Windows".lower():
   print("Correct")
   score = score + 1
else:
   print("Worng")

print("You got " + str(score) + " Question Correct")
print("You got " + str((score/5) * 100) + "%")

  

  














