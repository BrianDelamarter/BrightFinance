class account:
    def __init__(self, balance, rate, term):
        self.balance = balance
        self.apy = rate
        self.term  = term
    
    def __str__(self):
        return f"Account Balance: {self.balance} with a {round(self.apy*100,2)}% APY"

class loan(account):
    def monthly(self):
        r = self.apy/12
        payment = round(self.balance*((r*(1+r)**self.term)/((1+r)**self.term-1)),2)
        print(f"Your monthly payment is ${payment}")
    
    def totalCost(self):
        

subaru = loan(6000,0.072,60)
subaru.monthly()