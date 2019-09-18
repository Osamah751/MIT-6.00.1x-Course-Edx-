
#Test Case 1: (70)
# balance = 757;annualInterestRate = 0.25

# Test Case 2(correct): (10)
# balance = 84; annualInterestRate = 0.25
#
#Test Case 3(wrong): (290)
balance = 3208; annualInterestRate = 0.15



def finding_the_minimum_payment(balance, annualInterestRate):
    # annualInterestRate = 0.2
    monthlyPaymentRate = annualInterestRate/12
    temp_balance = balance
    minimum_payment = 0
    unpaid_balance = balance

    while balance >= 0:
        balance = temp_balance
        minimum_payment += 10
        for month in range(1, 13):
            unpaid_balance = balance - minimum_payment
            balance = unpaid_balance + monthlyPaymentRate * unpaid_balance



    return (minimum_payment)

minimum_payment = finding_the_minimum_payment(balance,annualInterestRate)

print ("Lowest Payment: " + str(minimum_payment) )