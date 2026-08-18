import random
print("🎯 Welcome to the Guessing Game!")

print("🤖 I'm thinking of a number between 1 and 100...")
print("💡 Can you guess it?\n")
number = random.randint(1, 100)
while True:
    guess = int(input("🔢 Enter your guess: "))

    if guess == number:
        print("\n🎉🎊 CORRECT! 🎊🎉")
        print("🏆 Congratulations! You guessed the number!")
        break
    elif guess > number:
        print("📈 Too high! Try a smaller number. 🔽\n")
    else:
        print("📉 Too low! Try a bigger number. 🔼\n")
print("✨ Thanks for playing! 🎮")