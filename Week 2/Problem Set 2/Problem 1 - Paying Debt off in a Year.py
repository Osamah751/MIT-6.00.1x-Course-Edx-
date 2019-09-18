'''
Problem 1 - Paying Debt off in a Year
10/10 points (graded)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

# # Test Case 1:
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# # Test Case 2:
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

for i in range (1,13):
    minimum_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    interest = 0.18/0.12 * unpaid_balance
    balance = unpaid_balance + (annualInterestRate/12 * unpaid_balance)

    ## to check the balance for each month
    # print ("Month " + str(i) + " Remaining balance: " + str("%.2f" % balance) )

print ("Remaining balance: " + str("%.2f" % balance) )