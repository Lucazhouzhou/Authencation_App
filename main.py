import sys
import bcrypt
import csv
while True:
    A = input("Log in, Register or Quit?")
    if A =="Log in":
        while True:
            UN=input("username?")
            PW=input("password?")
            with open ("source.csv") as database:
                reader=csv.reader(database)
                for row in reader:
                    if UN == row[0] and PW == row [1]:
                        break
                break
        q2=input("Change password or Quit?")
        if q2 =="Change password":
            PW=input(" new password?")
            if int(len(PW)) < 4 :
                PW=input("new password?")
            with open ("source.csv","a") as databa:
                writer=csv.writer(databa)
                writer.writerow([UN,PW])
        else:
            sys.exit()
        break
    elif A == "Register":
        while True:
            UN=input("username?")
            PW=input("password?")
            with open ("source.csv") as database:
                reader=csv.reader(database)
                for row in reader:
                    if UN == row[0] and PW == row [1]:
                        break
            salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"
            with open ("plain_text.txt","a") as plain:
                plain.write(f"{UN},{PW}")
            with open ("plain_text.txt") as text:
                for line in text:
                    U,P=line.split(",")
                        if U == UN:
                            HPW = bcrypt.hashpw(password=P, salt=salt)
            with open ("source.csv","a") as databa:
                writer=csv.writer(databa)
                writer.writerow([UN,HPW])
        break
    elif A == "Quit":
        sys.exist
        break
    else:
        continue