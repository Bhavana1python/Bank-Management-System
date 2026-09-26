#BankSearchCustomer.py
from Bankrecords import bankrecord
class BSearchCustomer:
    def search(self):
        try:
            records = bankrecord().getrecords()
            acno = int(input("Enter Account Number: "))
            res = False
            for record in records:
                if acno == record[0]:
                    res = True
                    print("Valid customer")
                    break
            if not res:
                print("Invalid customer")
        except ValueError:
            print("Enter only digits --- Try again")
#o = BankSearchCustomer()
#o.search()