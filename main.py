from auth import login, load_user
from admin import Admin
from student import Student

# User Interface
def main():
    user_id=login()
    user=load_user(user_id)
    if user is None:
        print("User not found.")
        return
    
# Admin Dashboard
    print("=====================================================================================")
    print("Hello,", user.name)
    if isinstance(user, Admin):
        while True:
            print("-------------------------------------------------------------------------------------")
            print("1. Add User\n2. Update User\n3. Delete User\n4. Analyze Data\n5. Exit")
            print("=====================================================================================")
            choice = input("Enter choice: ")
            print("=====================================================================================")
            if choice=='1':#ADD
                uid=input("User ID: ")
                name=input("Name: ")
                role=input("Role (admin/student): ")
                password=input("Password: ")
                user.add_user(uid, name, role, password)
                grades=list(map(int, input("Enter grades (Maths,Science,English,Social Studies,Computer) separated by commas[,]: ").split(',')))
                user.add_grades(uid, grades)
                activities=input("Enter ECAs (separated by semicolon[;]): ")
                user.add_eca(uid, activities)
            
            elif choice=='2':#UPDATE
                uid=input("User ID to update: ")
                new_info=input("Enter new info (name,role): ")
                user.update_user(uid,f"{uid},{new_info}")
                new_password=input("Enter new password: ")
                user.update_password(uid,f"{uid},{new_password}")
                new_grades=input("Enter new grades (Maths,Science,English,Social Studies,Computer): ")
                user.update_grades(uid,f"{uid},{new_grades}")
                new_activities=input("Enter new ECAs (separated by semicolon[;]): ")
                user.update_activities(uid,f"{uid},{new_activities}")
            
            elif choice=='3':#DELETE
                uid=input("User ID to delete: ")
                user.delete_user(uid)
            
            elif choice=='4':#ANALYZE
                user.analyze_data()
            
            elif choice=='5':
                break

# Student Dashboard   
    elif isinstance(user, Student):
        while True:
            print("-------------------------------------------------------------------------------------")
            print("1. View Profile\n2. View Grades\n3. View ECA\n4. Exit")
            print("=====================================================================================")
            choice = input("Enter choice: ")
            print("=====================================================================================")
            if choice=='1':
                print(user.viewprofile())
            elif choice=='2':
                print(user.viewgrades())
            elif choice=='3':
                print(user.vieweca())
            elif choice=='4':
                break

# Check if the main function is running directly
if __name__=="__main__":
    main()
