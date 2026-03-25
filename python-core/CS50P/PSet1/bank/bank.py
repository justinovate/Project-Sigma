greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"):
    amount = 0
elif greeting.startswith("h"):
    amount = 20
else:
    amount = 100

print(f"${amount}")
