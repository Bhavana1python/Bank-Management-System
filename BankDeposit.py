#BankDeposit.py
import pickle
from Bankrecords import bankrecord
class BDeposit:
    def deposit(self):
        try:
            records = bankrecord().getrecords()
            # print (records)
            acno = int(input("Enter the account number to which you want to deposit: "))
            res = False
            for record in records:
                if (acno == record[0]):
                    bankrec = record
                    res = True
            if res:
                print("Available balance before deposited is: ", bankrec[2])
                depamt = float(input("Enter the deposit amount: "))
                bal = bankrec[2] + depamt
                bankrec[2] = bal
                print("Available balance after deposited is: ", bankrec[2])
                with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "wb") as fp:
                    for record in records:
                        pickle.dump(record, fp)
                    print("Amount is credited in ur account successfully")
            else:
                print("Account number does not exist")
        except ValueError:
            print("Enter only digits--Try again")
#o=BankDeposit()
#o.deposit()
