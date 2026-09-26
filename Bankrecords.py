import pickle
class bankrecord:
    def getrecords(self):
        records = []
        try:
            with open("F:\\Bhavananotes\\RealTimeprojects\\Banking.pick", "rb") as fp:
                while True:
                    try:
                        record = pickle.load(fp)
                        records.append(record)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")
        return records
    def isunique(self, acno):
        records = self.getrecords()
        found = True
        for record in records:
            if acno == record[0]:
                found = False
                print("Customer already exists")
        return found


