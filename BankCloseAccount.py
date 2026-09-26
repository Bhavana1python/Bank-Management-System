from Bankrecords import bankrecord
import pickle
class accountclose:
    def closeacc(self):
        records = bankrecord().getrecords()
        try:
            acno = int(input("Enter Account Number to delete: "))
        except ValueError:
            print("Enter only digits --- Try again")
            return
        for record in records:
            if acno == record[0]:
                records.remove(record)
                with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "wb") as fp:
                    for rec in records:
                        pickle.dump(rec, fp)
                print("Account deleted successfully")
                return
        print("Account number does not exist")
#o = accountclose()
#o.closeacc()