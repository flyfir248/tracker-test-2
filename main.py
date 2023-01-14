import sqlite3

conn = sqlite3.connect("expense.db")
cur = conn.cursor()

print("Hi")

while True:
    print("Select an option : ")
    print("1. enter a new expense")
    print("2. View expenses")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of the expense (YY-MM-DD) : ")
        desc = input("Enter the desc of the expense : ")

        cur.execute("SELECT DISTINCT category FROM expense")

        categories = cur.fetchall()
        print(" Select a category by number : ")

        for idx, category in enumerate(categories):
            print(f"{idx + 1}.{category[0]}")
        print(f"{len(categories) + 1}.Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")

        else:
            category = categories[category_choice - 1][0]

        price = float(input("Enter the price of the expense: "))
        cur.execute("INSERT INTO expense (date, desc, category,price) VALUES (?,?,?,?)", (date, desc, category, price))

        conn.commit()

    elif choice == 2:
        print("Select an option :")
        print("1. View all expenses")
        print("2. View all monthly expenses by category")
        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expense")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)

        elif view_choice == 2:
            month = input("Enter the month (MM) :")
            year = input("Enter the year (YYYY) :")
            cur.execute("""SELECT category, SUM(price) FROM expense 
                        WHERE strftime('%m', date) = ? AND strftime('%Y',date) = ? 
                        GROUP by category
                        """, (month, year))

            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category : {expense[0]}, Total : {expense[1]}")

    else:
        break

    repeat = input(" Would you like to do something else (y,n) ?\n")
    if repeat.lower() != "y":
        break

conn.close()

print('hi')
"""
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/flyfir248/tracker-test-2.git
git push -u origin main

"""