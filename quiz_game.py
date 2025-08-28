print("Welcome to the General Knowledge Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What is the capital of France? ").strip().lower()
if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("How many continents are there on Earth? ").strip().lower()
if answer == "7" or answer == "seven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What is the largest planet in our Solar System? ").strip().lower()
if answer == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Who wrote 'Romeo and Juliet'? ").strip().lower()
if answer == "william shakespeare" or answer == "shakespeare":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("What is the chemical symbol for water? ").strip().lower()
if answer == "h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 6
answer = input("How many players are there in a soccer team on the field? ").strip().lower()
if answer == "11" or answer == "eleven":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 7
answer = input("In which country are the Pyramids of Giza located? ").strip().lower()
if answer == "egypt":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 8
answer = input("What gas do humans need to breathe to survive? ").strip().lower()
if answer == "oxygen":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 9
answer = input("Who painted the Mona Lisa? ").strip().lower()
if answer == "leonardo da vinci" or answer == "da vinci":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 10
answer = input("What is the smallest prime number? ").strip().lower()
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 11
answer = input("Which ocean is the largest? ").strip().lower()
if answer == "pacific" or answer == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 12
answer = input("What is the hardest natural substance on Earth? ").strip().lower()
if answer == "diamond":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 13
answer = input("What is the capital of Japan? ").strip().lower()
if answer == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 14
answer = input("Who developed the theory of relativity? ").strip().lower()
if answer == "albert einstein" or answer == "einstein":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 15
answer = input("Which planet is known as the Red Planet? ").strip().lower()
if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 16
answer = input("How many sides does a hexagon have? ").strip().lower()
if answer == "6" or answer == "six":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 17
answer = input("What is the freezing point of water in Celsius? ").strip().lower()
if answer == "0" or answer == "zero":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 18
answer = input("Which country is known as the Land of the Rising Sun? ").strip().lower()
if answer == "japan":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 19
answer = input("Who was the first man to walk on the Moon? ").strip().lower()
if answer == "neil armstrong" or answer == "armstrong":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 20
answer = input("What is the largest mammal in the world? ").strip().lower()
if answer == "blue whale" or answer == "whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} out of 20 questions correct!")
print(f"Your score: {(score / 20) * 100}%")

   


