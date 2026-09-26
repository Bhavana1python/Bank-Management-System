#BankPinGenerateUpdate.py
from Bankrecords import bankrecord
import pickle
class BPinGenerateUpdate:
    def pingenerate(self):
        try:
            records = bankrecord().getrecords()
            # print(records)
            Acno = int(input("\tEnter Account number to generate PIN:"))
            res = False
            for record in records:
                if (record[0] == Acno):
                    bankrec = record
                    res = True
                    break
            if (res):
                if bankrec[3] is not None:
                    print("\tPIN already generated")
                    return
                pin = int(input("\tEnter 4-digit PIN: "))
                # Simple validation
                if pin < 1000 or pin > 9999:
                    print("\tPIN must be 4 digits")
                    return
                bankrec[3] = __pin
                with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "wb") as fp:
                    for record in records:
                        pickle.dump(record, fp)
                    print("pin is generated successfully")
            else:
                print("Record Not Found")
        except ValueError:
            print("Enter a valid Account number")
    def pinupdate(self):
        try:
            records = bankrecord().getrecords()
            Acno = int(input("\tEnter Account number to update PIN:"))
            res = False
            for record in records:
                if (record[0] == Acno):
                    bankrec = record
                    res = True
                    break
            if (res):
                newpin = int(input("\tEnter 4-digit PIN: "))
                # Simple validation
                if newpin < 1000 or newpin > 9999:
                    print("\tPIN must be 4 digits")
                    return
                bankrec[3] = newpin
                with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "wb") as fp:
                    for record in records:
                        pickle.dump(record, fp)
                    print("pin is updated successfully")
        except ValueError:
            print("Enter a valid Account number")
#o=BankPinGenerateUpdate()
#o.pingenerate()
#o.pinupdate()