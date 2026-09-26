#BankAccountOpen.py
import pickle
from Bankrecords import bankrecord
class AccountOpen:
    def openaccount(self):
        try:
            while (True):
                with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "ab") as fp:
                    print("-------------------------------------")
                    acno = int(input("Enter Customer account number:"))
                    if (bankrecord().isunique(acno)):
                        self.cname = input("Enter customer name:")
                        self.bal = float(input("Enter Balance:"))
                        self.pin = None
                        self.bname = input("Enter Customer Branch Name:")
                        record = [acno, self.cname, self.bal, self.pin, self.bname]
                        pickle.dump(record, fp)
                        ch = input("Do yot want to open another account yes/No:")
                        if (ch.lower() == 'no'):
                            print("Thanks for using Bhavana's program")
                            break
                    else:
                        break
        except ValueError:
            print("Please enter correctly")

#o=BankAccountOpen()
#o.openaccount()
