investment = input("Enter investment amount: ")

investment = float(investment)

interest_rate = input("Interest Rate : ")
interest_rate = float(interest_rate) * .01

for i in range(0):
    investment = investment + (investment * interest_rate)

print(f"Investment after 10 years : {investment:.2f}")
