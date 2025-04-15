# Initialize user information
class User:
    def __init__(self,id,name,role):
        self.id=id
        self.name=name
        self.role=role

# Display profile information in student dashboard
    def viewprofile(self):
        return f"ID: {self.id}, Name: {self.name}, Role: {self.role}"
