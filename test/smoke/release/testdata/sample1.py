import csv
from selenium.webdriver import Firefox, Chrome, Ie
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def castrange():
        with open('C:/Users/Felix/Desktop/sample.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            email = []
            mobile = []
            password = []
            firstname = []
            lastname = []
            zipcode = []
            ssn = []
            for row in readCSV:
                emailVar = row[0]
                mobileVar = row[1]
                passwordVar = row[2]
                firstnameVar = row[3]
                lastnameVar = row[4]
                zipcodeVar = row[5]
                ssnVar = row[6]

                email.append(emailVar)
                mobile.append(mobileVar)
                password.append(passwordVar)
                firstname.append(firstnameVar)
                lastname.append(lastnameVar)
                zipcode.append(zipcodeVar)
                ssn.append(ssnVar)

            email.pop(0)
            mobile.pop(0)
            password.pop(0)
            firstname.pop(0)
            lastname.pop(0)
            zipcode.pop(0)
            ssn.pop(0)

            return email, mobile, password, firstname, lastname, zipcode, ssn
