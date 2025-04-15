from user import User
import pandas as pd
import matplotlib.pyplot as plt

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, 'admin')

# Adding user information from admin
    def add_user(self, user_id, name, role, password):
        with open("users.txt", "a") as f:
            f.write(f"{user_id},{name},{role}\n")
        with open("passwords.txt", "a") as f:
            f.write(f"{user_id},{password}\n")

    def add_grades(self, user_id, grades):
        with open("grades.txt", "a") as f:
            f.write(f"{user_id}," + ",".join(map(str, grades)) + "\n")

    def add_eca(self, user_id, activities):
        with open("eca.txt", "a") as f:
             f.write(f"{user_id},{activities}\n")

# Updating user information from admin
    def update_user(self, user_id, new_info):
        self.updatefile("users.txt", user_id, new_info)

    def update_password(self, user_id, new_password):
        self.updatefile("passwords.txt", user_id, new_password)

    def update_grades(self, user_id, new_grades):
        self.updatefile("grades.txt", user_id, new_grades)

    def update_activities(self, user_id, new_activities):
        self.updatefile("eca.txt", user_id, new_activities)

    def updatefile(self, filename, user_id, new_line):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
            with open(filename, "w") as f:
                for line in lines:
                    if line.startswith(user_id):
                        f.write(new_line + '\n')
                    else:
                        f.write(line)
        except Exception as e:
            print(f"Error updating {filename}: {e}")

# Deleting user information from admin
    def delete_user(self, user_id):
        self.deletefile("users.txt", user_id)
        self.deletefile("grades.txt", user_id)
        self.deletefile("eca.txt", user_id)
        self.deletefile("passwords.txt", user_id)

    def deletefile(self, filename, user_id):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
            with open(filename, "w") as f:
                for line in lines:
                    if not line.startswith(user_id):
                        f.write(line)
        except Exception as e:
            print(f"Error deleting from {filename}: {e}")

# Display analysis of student data
    def analyze_data(self):
        from data_analysis import analyze
        analyze()
    

