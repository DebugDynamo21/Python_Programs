# While purchasing certain items, a discount of 10% is offered
# if the quantity purchased is more than 1000. If quantity and
# price per item are input through the keyboard, write a
# program to calculate the total expenses.

quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))

total_expense = quantity * price_per_item

if quantity > 1000:
    discount = total_expense * 0.10
    total_expense -= discount
    print(f"A discount of 10% has been applied. Discount amount: {discount:.2f}")
else:
    print("No discount applied.")
