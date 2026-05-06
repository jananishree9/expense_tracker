# expense_tracker.py

expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Breakdown")
    print("5. Exit")

    choice = input("\nEnter choice (1/2/3/4/5): ")

    if choice == "1":
        category = input("Category (Food/Transport/Shopping/Other): ")
        amount = input("Amount spent (Rs): ")
        expense = {
            "category": category,
            "amount": float(amount)
        }
        expenses.append(expense)
        print("✅ Expense saved!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            print("\n--- Your Expenses ---")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. {expense['category']} - Rs.{expense['amount']}")

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
        print(f"\nTotal spending: Rs.{round(total, 2)}")

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            breakdown = {}
            for expense in expenses:
                cat = expense["category"]
                amt = expense["amount"]
                if cat in breakdown:
                    breakdown[cat] = breakdown[cat] + amt
                else:
                    breakdown[cat] = amt

            print("\n--- Category Breakdown ---")
            for cat, amt in breakdown.items():
                print(f"{cat}: Rs.{round(amt, 2)}")

    elif choice == "5":
        print("Bye! Spend wisely! 💰")
        break

    else:
        print("❌ Invalid choice!")
