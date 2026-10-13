total = 0.0

while True:
    print("1. Add an expense")
    print("2. View total")
    print("3. Quit")
    choice = input("Choose 1, 2 or 3:").strip()

    if choice == "1":
        text = input("Enter an amount:").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Type a number like 100 or 50.5")
            continue
        total = total + amount
        print ("Saved.")
    elif choice == "2":
        print (f"total spent:${total:.2f}")
    elif choice =="3":
        print(f"Total spent: ${total:.2f}")
        print("Goodbye")
        break
    else:
        print ("Please pick 1, 2 or 3.")
