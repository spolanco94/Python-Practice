##### Write 2 examples that incorporate the lesson points from Chapter 5
##### Use conditionals, if statements, and looping through lists
cars = ["bmw", "acura", "mazda", "honda", "jaguar"]
shoes = ["adidas", "nike", "asics", "timberlands", "skechers"]
score = 0

print("Welcome! Guess the order of best cars from best to worst!")
for i in cars:
    print("What is your guess? ")
    guess = input()
    if i != guess.lower():
        if i == "bmw":
            print(f"{i == guess.lower()}, it was {i.upper()}!\n")
        else:
            print(f"{i == guess.lower()}, it was {i.title()}!\n")
    else:
        print(f"{i == guess.lower()}\n")
        score += 1
if score >= 4:
    print(f"Wow, you got {score} points! You are a car lover huh? Nice Job!")
elif score > 1:
    print(f"Aw, you got {score} points. Try again next time!")
else:
    print(f"You got {score} points. Don't worry, this quiz isn't everything!")
print("Hope you had fun!")

# print("How about which shoe brands were most popular?")
# for i in shoes:
#     print("What is your guess? ")
#     guess = input()
#     if i != guess.lower():
#         print(f"{i == guess.lower()}, it was {i.title}!")
#     else:
#         print(i == guess.lower())

