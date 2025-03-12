password = input("Enter new password: ")
results = {}

if len(password) >= 8:
    results["length"] = True
else:
    results["length"] = False

digit = False

for item in password:
    if item.isdigit():
        digit = True

results["digit"] = digit

uppercase = False

for item in password:
    if item.isupper():
        uppercase = True

results["upper-case"] = uppercase

print(results)
print(results.values())

if all(results.values()):
    print("Strong Password")
else:
    print("Weak Password")

