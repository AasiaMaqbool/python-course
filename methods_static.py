class Teams:
    membership = 'true'

    def __init__(self, name, id, employee_workyear):
        if employee_workyear > 5:
            self.name = name
            self.id = id

    def salary(self):
        salary_increment = 2000  # Initialize the salary increment variable
        salary_increment += 2000
        print('salary_increment is equal to', salary_increment)

    @classmethod
    def cls_methods(cls, name, id):
        # Example implementation for a class method
        return f"Class method called with name: {name}, id: {id}"

    @staticmethod
    def stc_method(name, id):
        print('membership:', Teams.membership)
        print('salary_increment: 2000')  # Just an example print statement


# Example usage
team_member = Teams('John Doe', 123, 6)  # Assuming employee work year is greater than 5
team_member.salary()
print(Teams.cls_methods('Jane Doe', 456))
Teams.stc_method('Jane Doe', 456)