import pickle
from Bankrecords import bankrecord
class BWithDraw:
    def withdraw(self):
        try:
            records = bankrecord().getrecords()
            acno = int(input("Enter account number: "))
            found = False
            for record in records:
                if acno == record[0]:
                    found = True
                    print("Available balance before withdrawl:", record[2])
                    wamt = float(input("Enter amount to withdraw: "))
                    # minimum balance validation
                    if (record[2] - wamt) < 500:
                        print("Withdrawal denied")
                        print("Minimum balance of 500 must be maintained")
                    record[2] = record[2] - wamt
                    print("Available balance after withdrawl is:", record[2])
                    with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "wb") as fp:
                        for rec in records:
                            pickle.dump(rec, fp)
                    print("Amount is debited from your account successfully")
                    break
            if not found:
                print("Account number does not exist")
        except ValueError:
            print("Enter only digits--Try again")

#o = BankWithDraw()
#o.withdraw()