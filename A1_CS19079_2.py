from A1_CS19079_1 import Records


class UserRecords(Records):  # This class will record the logging information of user as well as check whether the user is already sign in or not
    def __init__(self):
        self.signupUser = {}

    def saveRecords(self):  # Will save details of new user on sign up
        x = input("Email: ")
        y = input("Password: ")
        self.signupUser[x] = y
        f1 = open('UsersList.txt', 'a')
        f1.write(str(self.signupUser) + '\n')  # Saving email and password of user in dictionary form
        f1.close()
        f2 = open('Emails.txt', 'a')
        f2.write(str([x]) + '\n')  # Writing email of sign up user to file of users' email
        f2.close()

    def checkEmail(self, email):  # Will check whether the email is already sign up or not
        f = open('Emails.txt', 'r')
        f.seek(0)
        for i in f:
            i = eval(i)
            for j in i:
                if j == email:
                    return True
        else:
            pass

    def checkPass(self, email, password):  # After confirmation of email's sign up it will check whether the entered password is correct or not
        f = open('UsersList.txt', 'r')
        for i in f:
            i = eval(i)
            try:
                if i[email] == password:
                    return True
                else:
                    print('Password not match')
            except KeyError:
                pass
        f.seek(0)


# a = UserRecords()
# a.saveRecords()
# b = UserRecords()
# b.saveRecords()
# c = UserRecords()
# c.saveRecords()
# a.checkEmail("a")
# a.checkPass('c', '3')