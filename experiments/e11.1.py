def greet(message):
    new_message = message.capitalize()
    print("hey hey")
    return new_message

user_greeting = input("What greeting do you want? ")
greeting = greet(user_greeting)
print(greeting)