changeAmt = input("What is the amount of change required?")
changeAmt = int(changeAmt)
numQtrs = changeAmt // 25 # Figure out the number of quarters

changeAmt = changeAmt - (numQtrs * 25)

numDimes = changeAmt // 10 
changeAmt -= (numDimes * 10)

numNickels = changeAmt // 5 
changeAmt -= (numNickels * 5)

numPennies = changeAmt // 1
changeAmt -= (numPennies * 1)

print("Quarters: " + str(numQtrs))
print("Dimes: " + str(numDimes))
print("Nickels: " + str(numNickels))
print("Pennies: " + str(numPennies))

print("Your change is " + str(numQtrs) + " Quarters, " + str(numDimes) + " Dimes, " + str(numNickels) + " Nickels, and " +72 str(numPennies) + " Pennies.")