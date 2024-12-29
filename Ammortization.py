#Creates a generic account object that will act as a super for more specific account types
class account:
    def __init__(self, balance, rate, term):
        self.balance = balance
        self.apy = rate
        self.term  = term
    
    def __str__(self):
        return f"Account Balance: {self.balance} with a {round(self.apy*100,2)}% APY"

#Loan specific object that is used to calculate cost/interest and perform an ammorterization
class loan(account):
    def __init__(self, balance, rate, term):
        super().__init__(balance, rate, term)
        self.calculate()
    #calculates the payment, total cost, and total interest of the loan
    def calculate(self):
        r = self.apy/12
        self.payment = self.balance*((r*(1+r)**self.term)/((1+r)**self.term-1))
        self.cost = self.payment*self.term
        self.interest = self.cost - self.balance
    #prints statement with basic facts of the loan
    def loanInfo(self):
        print(f"Your ${self.balance} loan at %{round(self.apy*100,2)} APY will have a monthly payment of ${round(self.payment,2)}. This will cost ${round(self.cost,2)} over its {round(self.term,2)} month term and you will pay ${round(self.interest,2)} in interest.")

    def ammortarization(self):
        pass   

subaru = loan(6000,0.072,60)
subaru.loanInfo()