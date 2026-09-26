#BankViewCustomers.py
from Bankrecords import bankrecord
class BViewCustomers:
    def viewcustomer(self):
        try:
            while True:
                print("-" * 40)
                acno = int(input("Enter Account Number: "))
                records = bankrecord().getrecords()
                found = False
                for record in records:
                    if acno == record[0]:
                        print("Account Number:", record[0])
                        print("Account Name:", record[1])
                        print("Balance:", record[2])
                        print("PIN:", BViewCustomers().getpin(record[3]))
                        print("Branch Name:", record[4])
                        found = True
                        break
                if not found:
                    print("Employee number does not exist")
                ch = input("Do you want to view another customer yes/no: ")
                if ch.lower() == "no":
                    print("Thanks for using Bhavana's program")
                    break
        except ValueError:
            print("Enter only digits--Try again")

    def getpin(self,pin):

        if pin is None:
            return None

        return "*" * len(str(pin))

    def viewcustomers(self):
        records = bankrecord().getrecords()
        print("-" * 60)
        print("acno\tcname\tbalance\t\tpin\t\t\tbranch")
        print("-" * 60)
        for record in records:
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(record[0],record[1],record[2],record[3],record[4]))
        print()
#o = BankViewCustomers()
#o.viewcustomer()
#o.viewcustomers()