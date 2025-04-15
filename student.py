from user import User

class Student(User):
    def __init__(self,id,name):
        super().__init__(id, name, 'student')

# Display grades in student dashboard
    def viewgrades(self):
        subjects = ['Math', 'Science', 'English', 'Social Studies', 'Computer']
        try:
            with open("grades.txt", "r") as f:
                for data in f:
                    part = data.strip().split(',')
                    if part[0] == self.id:
                        return dict(zip(subjects, map(int, part[1:])))
        except Exception as e:
            print(f"Error reading grades: {e}")
        return {}

# Display ECA of students
    def vieweca(self):
        try:
            with open("eca.txt", "r") as f:
                for data in f:
                    if data.startswith(self.id + ','):
                        return data.strip().split(',', 1)[1]
        except Exception as e:
            print(f"Error reading ECA data: {e}")
        return "No ECA record found."
