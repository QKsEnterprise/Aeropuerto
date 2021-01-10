Francia = "Francia price:$2.000.000 passangers:5"

Francia = 2000000 * 5

# print(Francia)

DebitCard = 1000000

FinalResult = Francia - DebitCard

if DebitCard >= Francia:
    print("Transaction ¡Ok! $", FinalResult)
else:
    print("Invalid Transaction")
