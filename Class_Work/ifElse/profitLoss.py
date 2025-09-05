# If the cost price and selling price of an item are input
# through the keyboard, write a program to determine
# whether the seller has made a profit or incurred a loss.
# Also, determine how much profit he made or loss he
# incurred.

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

profit = (sp - cp)

if profit > 0:
    print("Profit = ", profit)
elif profit < 0:
   print("Loss = ", -profit)
else:
    print("No Profit No Loss")