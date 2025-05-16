user_input = input("What's your password? >:) ")

print(user_input)

if len(user_input) < 8:
    print("Your password isn't long enough.")
else:
    print("That is a strong password.")