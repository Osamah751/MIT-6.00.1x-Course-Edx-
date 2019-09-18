# Test Case 1: (29157.09)
# balance = 320000;annualInterestRate = 0.2

# Test Case 1: (90325.03)
# balance = 999999;annualInterestRate = 0.18

#Test Case 3: (285.97)
balance = 3208; annualInterestRate = 0.15

# setting the variables 
monthlyPaymentRate = annualInterestRate/12
temp_balance = balance
unpaid_balance = balance
min =balance / 12
max = (balance * (1 + monthlyPaymentRate)**12 ) /12
minimum_payment = (min+max) /2



while True:

    # testing the monthly payment rate in a year
    for month in range(1, 13):
        unpaid_balance = balance - minimum_payment
        balance = unpaid_balance + monthlyPaymentRate * unpaid_balance

    # if the monthly payment rate is correct print it
    if abs(balance) < 0.1:
        print ("Lowest Payment: " + str("%.2f" % minimum_payment) )
        break
    # otherwise use binary search to look for a new monthly payment rate to test
    else:
        if balance < 0:
            max = minimum_payment
        elif balance > 0:
            min = minimum_payment

        # reset the used variables 
        minimum_payment = (min + max) / 2
        balance = temp_balance
