
# Test Case 1: (29157.09)
# balance = 320000;annualInterestRate = 0.2

# Test Case 1: (90325.03)
# balance = 999999;annualInterestRate = 0.18

#Test Case 3(wrong): (290)
# balance = 3208; annualInterestRate = 0.15



def finding_the_minimum_payment(balance, annualInterestRate):
    monthlyPaymentRate = annualInterestRate/12
    temp_balance = balance
    minimum_payment = 0

    while balance > 0:
        if balance >= (minimum_payment+10)*12:
            minimum_payment += 10
        else:
            minimum_payment += 0.01
        balance = temp_balance
        for month in range(1, 13):
            unpaid_balance = balance - minimum_payment
            balance = unpaid_balance + monthlyPaymentRate * unpaid_balance
    return (minimum_payment)

minimum_payment = finding_the_minimum_payment(balance,annualInterestRate)

print ("Lowest Payment: " + str("%.2f" % minimum_payment) )
