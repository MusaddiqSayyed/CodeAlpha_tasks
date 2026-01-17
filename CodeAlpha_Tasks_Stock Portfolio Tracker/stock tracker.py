prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

print("Stock List")
for name in prices:
    print(name, "-", prices[name])

user_portfolio = {}
choice = "yes"

while choice == "yes":
    stock = input("Enter stock name: ").upper()

    if stock not in prices:
        print("Stock not found")
    else:
        try:
            qty = int(input("Enter quantity: "))
            if qty > 0:
                user_portfolio[stock] = user_portfolio.get(stock, 0) + qty
            else:
                print("Quantity must be positive")
        except:
            print("Enter numeric value")

    choice = input("Add more stocks yes or no: ").lower()

print("Final Portfolio")

total_value = 0

for item in user_portfolio:
    amount = prices[item] * user_portfolio[item]
    total_value += amount
    print(item, user_portfolio[item], prices[item], amount)

print("Total Portfolio Value:", total_value)

store = input("Do you want to save data yes or no: ").lower()

if store == "yes":
    save_as = input("Save as txt or csv: ").lower()

    if save_as == "txt":
        f = open("portfolio.txt", "w")
        f.write("Portfolio Details\n")
        for item in user_portfolio:
            f.write(item + " " + str(user_portfolio[item]) + "\n")
        f.write("Total " + str(total_value))
        f.close()

    elif save_as == "csv":
        f = open("portfolio.csv", "w")
        f.write("Stock,Qty,Total\n")
        for item in user_portfolio:
            f.write(item + "," + str(user_portfolio[item]) + "," + str(prices[item] * user_portfolio[item]) + "\n")
        f.write("Total,," + str(total_value))
        f.close()

print("Execution Completed")