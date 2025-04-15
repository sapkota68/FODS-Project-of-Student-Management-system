from student import Student
from admin import Admin

# Authenticate user and password for login
def login():
    while True:
        print("=====================================================================================")
        print("                              Student Management System                              ")
        print("=====================================================================================")
        username=input("Enter username: ")
        password=input("Enter password: ")
        try:
            with open("passwords.txt", "r") as f:
                for data in f:
                    id,ps=data.strip().split(',')
                    if id==username and ps==password:
                        return username
        except Exception as e:
            print("Error during login:", e)
        print("Invalid credentials, please try again.\n")
 
# Differentiate login for admin and student
def load_user(username):
    try:
        with open("users.txt", "r") as f:
            for data in f:
                id,name,role=data.strip().split(',')
                if id==username:
                    return Admin(id,name) if role=='admin' else Student(id, name)
    except Exception as e:
        print("Error loading user data:", e)
    return None
