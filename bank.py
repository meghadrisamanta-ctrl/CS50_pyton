greeting = input("Greet the customer: ")
better = greeting.strip().lower()
if better.startswith("hello"):
    print("$0")
elif better[0] == "h" and better != "hello":
    print("$20")
else:
    print("$100")
