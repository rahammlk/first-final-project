import json
import datetime

class sign_up:
    def __init__(self):
        self.username,self.password,self.email,self.birthYear,self.sequrityquestion1,self.sequrityquestion2= self.get_data()
    def load(self):
        with open('db.json') as f:
            db = json.load(f)
        return db
    def write_2_json(self):
        db = self.load()
        sign = {
            'username':self.username,
            'Password': self.password,
            'email': self.email,
            'birthYear':self.birthYear,
            'sequrityquestion1':self.sequrityquestion1,
            'sequrityquestion2' :self.sequrityquestion2

        }
        db.append(sign)
        with open('db.json','w') as file:
            json.dump(db,file,indent=4)

    def get_data(self):
        db = self.load()
        username = input("enter your username:")
        i = 0
        while i < len(db):
            if db[i]['username'] == username:
                print('username must be unique,please try again.')
                username = input("enter your username:")
                i = -1
            i += 1
        while True:
            password = input("enter your password:")
            if len(password) < 6:
                print("password is invalid,password is bigger than 6.")
            elif len(password) >= 6:
                letter = False
                number = False
                for i in password:
                    if i.isalpha():
                        letter = True
                    elif i.isdigit():
                        number = True
                if number + letter == 2:
                    print("Your password is valid.")
                    break
                else:
                    print("your password is invalid.")
            else:
                print("Password must be longer than 6 characters.")
        email = input("enter your email:")
        while not (email.endswith("@gmail.com") or email.endswith("yahoo.com")):
            print("your email is invalid.")
            email = input("enter your email:")
        i = 0
        while i < len(db):
            if db[i]['email'] == email:
                print("email must be unique , please try again.")
                email = input("enter your email:")
                i = -1
            i +=1

        while True:
            birthYear = int(input("enter your birthYear:"))
            age = datetime.datetime.now().year - birthYear
            if 18<=age<=50:
                print("Your registration was successful.")
                break
            else:
                print("Registration is not possible. Contact the company.")

        sequrityquestion1 = input('enter your favorite color:')
        sequrityquestion2 = input('enter your favorite car:')
        return username,password,email,birthYear,sequrityquestion1,sequrityquestion2

class course:
    def __init__(self,current_user):
        self.current_user = current_user
        self.name_course, self.users = self.info()
    def load_user(self):
        with open('db.json') as j:
            db = json.load(j)
        return db

    def load_course(self):
        with open('db2.json') as file:
            db2 = json.load(file)
        return db2

    def write_course(self):
        db2 = self.load_course()
        found = False
        for i in db2:
            if i['name of course'] == self.name_course:
                for j in self.users:
                    if j not in i['Registrations']:
                        i['Registrations'].append(j)
                found = True
                break
        if not found:
            course = {
                'name of course': self.name_course,
                'Registrations': self.users
            }
            db2.append(course)
        with open('db2.json', 'w') as f:
            json.dump(db2, f, indent=4)

    def info(self):
        db = self.load_user()
        training_course = ['python', 'matlab', 'javascript', 'Machine learning', 'deep learning', 'Network','Operating system']
        db2 = self.load_course()
        name_course = input("enter your  register course:")
        if name_course not in training_course:
            print("your course invalid.")
        else:
            print("your course valid")
        users = []
        regist = False
        for j in db:
            if j['username'] ==self.current_user:
                if 'course' in j:
                    if type(j['course']) == list and name_course in j['course']:
                        regist = True
                    elif j['course'] == name_course:
                        regist = True
            if 'course' in j:
                if type(j['course']) == list:
                    if name_course in j['course']:
                        users.append(j.get('username'))
                elif j['course'] == name_course:
                    users.append(j.get('username'))
        if not regist:
            print('you must register course')
            x = login()
            x.menu()
        return name_course, users

class login:
    def __init__(self):
        self.current_user=None
        self.username,self.password = self.gett_data()
        self.menu()
    def load_login(self):
        with open('db.json') as f:
            db = json.load(f)
        return db

    def menu(self):
        while True:
            question = input('enter option:\n1)Request to register for the course\n2)Participation in determining the level\n3)forgot password\n4)exit\n:')
            if question == '1':
                self.courses()
                majid = course(current_user='amir')
                majid.write_course()
            elif question == '2':
                username = input('enter your username:')
                amir = Exam(username)
                amir.write_answer()
                amir.calc_test()
            elif question == '3':
                self.forgot_pass()
                self.gett_data()
            elif question == '4':
                print('Thanks for using system.')
                amir = main()
                amir.choice()
            else:
                print('your answer invalid.')
    def gett_data(self):
        db = self.load_login()
        username = input('enter your username:')
        password = input('enter your password:')
        for i in db:
            if i['username']==username and i['Password']==password:
                self.current_user= username
                print("WELCOME TO YOUR PROFILE.")
                self.menu()
                return username,password
        print("you must register.")
        sign_up()
        return username,password
    def forgot_pass(self):
        db = self.load_login()
        found = False
        while True:
            sequrityquestion1 = input('enter your favorite color:')
            sequrityquestion2 = input('enter your favorite car:')
            for i in db:
                if i['sequrityquestion1'] == sequrityquestion1 and i['sequrityquestion2'] == sequrityquestion2:
                    found = True
                    while True:
                        password = input("enter your new password:")
                        if len(password) < 6:
                            print("password is invalid,password is bigger than 6.")
                        elif len(password) >= 6:
                            letter = False
                            number = False
                            for j in password:
                                if j.isalpha():
                                    letter = True
                                elif j.isdigit():
                                    number = True
                            if number and letter:
                                print("Your password is valid.")
                                print("your password is change")
                            else:
                                print("your password is invalid.")
                        else:
                            print("password is wrong")
                        i['Password'] = password
                        with open('db.json', 'w') as h:
                            json.dump(db, h, indent=4)
                        amir = main()
                        amir.choice()
                        return
            if not found:
                print("You answered the security questions incorrectly.")
    def courses(self):
        db = self.load_login()
        courses = ['python' , 'matlab' , 'javascript' , 'Machine learning' , 'deep learning' , 'Network' ,'Operating system']
        for i in courses:
            print(i)
        while True:
            answer =input('enter your course:')
            if answer in courses:
                print("your choice is valid.")
                print("Course registration was successful.")
                print(f"course start date:{datetime.datetime.now()}")
                date = datetime.datetime.now()
                for j in db:
                    if j['username'] == self.current_user:
                        if "course" not in j:
                            j['course'] = []
                        if "Course start date" not in j:
                            j['Course start date'] = {}
                        if answer not in j['course']:
                            j["course"].append(answer)
                            j['Course start date'][answer] = date.strftime('%Y/%m/%d - %H:%M:%S')

                                    # j['Course start date'] = date.strftime('%Y/%m/%d - %H:%M:%S')
                            break
                break
            else:
                print('your course is invalid.')
        with open('db.json','w') as file:
            json.dump(db,file,indent=4)

class Exam:
    def __init__(self,username):
        self.username=username
        (self.q1,self.q2,self.q3,self.q4,self.q5,self.a1,self.a2,self.a3,self.a4,self.a5) =self.getting_data()
    def load_test(self):
        with open('test.json') as l:
            test=json.load(l)
        return test

    def load_user(self):
        with open('db.json') as j:
            db = json.load(j)
        return db
    def write_answer(self):
        test = self.load_test()
        answer = {
            'answer 1' : self.a1,
            'answer 2' : self.a2,
            'answer 3' : self.a3,
            'answer 4' : self.a4,
            'answer 5' : self.a5
        }
        test.append(answer)
        with open('test.json' , 'w') as m:
            json.dump(test,m,indent=4)
    def getting_data(self):
        db = self.load_user()
        test = self.load_test()
        q1 = q2 = q3 =q4 = q5 =""
        a1 = a2 = a3 =a4 =a5 = ""
        for i in db:
            if i['username'] == self.username:
                if 'course' not in i:
                    print("First you must register for the course.")
                    x =login()
                    x.menu()
                    return
                elif "python" in i['course']:
                    q1 = input('What is the correct way to check if a variable x is equal to 5 in Python?a)x = 5 b)x==5 c)x.equals(5)  d) x is 5 ')
                    q2 = input('Which data type is used to store an ordered, mutable collection of items in Python? a)tuple b)set c)list d)dictionary')
                    q3 = input('What is the output of "Hello" + "World" in Python? a)"Hello World" b)"HelloWorld"  c)"Hello" + "World"  d) Error ')
                    q4 = input('Which keyword is used to define a function in Python? a)def b)function c)define d)func')
                    q5 = input('What does the len() function do in Python? a)Converts a string to lowercase b)Returns the number of items in an object c)Calculates the square root d)Checks if Answer:sts ')
                    a1 = "b"
                    a2 = "c"
                    a3 = "b"
                    a4 = "a"
                    a5 = "b"
        return q1, q2, q3, q4, q5, a1, a2, a3, a4, a5
    def calc_test(self):
        db = self.load_user()
        test = self.load_test()
        counter = 0
        username_test = input("enter your username test:")
        flag = False
        for i in db:
            if i['username'] == username_test and "python" in i['course']:
                if self.q1 == self.a1:
                    counter +=1
                if self.q2 == self.a2:
                    counter +=1
                if self.q3 == self.a3:
                    counter +=1
                if self.q4 == self.a4:
                    counter +=1
                if self.q5 == self.a5:
                    counter +=1
                flag = True
                break

        if not flag:
            print("your course invalid.")
            return
        flag2 = False
        for j in db:
            if j['username'] == username_test:
                if counter == 0:
                    j['grade'] = '0'
                    print(f"your score:0")
                if counter ==1:
                    j['grade'] = '20'
                    print(f"your score:20")
                if counter ==2:
                    j['grade'] = '40'
                    print(f"your score:40")
                if counter ==3:
                    j['grade'] = '60'
                    print(f"your score:60")
                if counter ==4:
                    j['grade'] = '80'
                    print(f"your score:80")
                if counter ==5:
                    j['grade'] = '100'
                    print(f"your score:100")
                flag2 = True
                break
        if not flag2:
            print("invalid username.")
            return
        with open('db.json' , 'w') as infile:
            json.dump(db,infile,indent=4)

class main:
    def choice(self):
        while True:
            question = input("enter option:\n1)sign up\n2)login\n:")
            if question =='1':
                print("Welcome to the registration page.")
                amir = sign_up()
                amir.write_2_json()
            elif question =='2':
                print("Welcome to the login page.")
                ali = login()
                ali.gett_data()
            else:
                print('invalid choice.')
                break
start = main()
start.choice()



























