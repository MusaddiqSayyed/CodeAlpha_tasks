prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150}
portfolio = {}


print("Available: AAPL, TSLA, GOOG")
while True:
    symbol = input("Enter stock symbol (or 'done'): ").upper()
    if symbol == 'DONE': break
    
    if symbol in prices:
        qty = int(input(f"Quantity of {symbol}: "))
        portfolio[symbol] = qty
    else:
        print("Stock not found.")


total = 0
with open("report.txt", "w") as f:
    for s, q in portfolio.items():
        subtotal = q * prices[s]
        total += subtotal
        result = f"{s}: {q} x ${prices[s]} = ${subtotal}"
        print(result)
        f.write(result + "\n")
    
    final_val = f"Total Investment: ${total}"
    print(final_val)
    f.write(final_val)