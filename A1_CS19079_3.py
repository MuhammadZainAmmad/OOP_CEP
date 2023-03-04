from A1_CS19079_1 import Records


class History(Records):  # Stores users shopping history as well as provide user history and delete history
    count = 0

    def __init__(self):
        self.history = []

    def saveRecords(self, email, history):
        # stores time and list of users purchased items
        # history should be two dimensional list containing purchase date and list of products
        f = open(email + '.shopHist.txt', 'a+')
        f.write(str(history) + '\n')
        f.close()

    def getHistory(self, email):  # return history of users purchase
        try:
            f = open(email + '.shopHist.txt', 'r')
            f.seek(0)
            if History.count == 0:
                for line in f:
                    line = eval(line)
                    self.history.append(line)
                History.count += 1
                return self.history
            else:
                return self.history
        except FileNotFoundError:
            return False

    def deleteHistory(self, email):  # delete history of user
        f = open(email + '.shopHist.txt', 'w')
        f.write('')
        f.close()
        self.history = []



# a = History()
# a.saveRecords('a', [2, ['a', 'b', 'c']])
#a.getHistory('a')
# a.deleteHistory('a')