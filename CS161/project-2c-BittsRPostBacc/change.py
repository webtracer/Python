# Author: Randy Bitts
# GitHub username: BittsrPostBacc
# Date: 09/28/2022
# Description: Asks the user for an amount of change from 0-99
#               and then break it down to Q,D,N,P quantities

print("Please enter an amount in cents less than a dollar.")
amount = int(input())
quarters = int(amount / 25)
dimes = int((amount - (quarters*25)) / 10)
nickels = int(((amount - (quarters*25)) - (dimes*10)) / 5)
pennies = int(((amount - (quarters*25) - (dimes*10)) - (nickels*5)) / 1)

print("Your change will be:")
print(f"Q: {quarters}")
print(f"D: {dimes}")
print(f"N: {nickels}")
print(f"P: {pennies}")
