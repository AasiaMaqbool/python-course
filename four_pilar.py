class Family:
    def __init__(self,family_name,number_of_members,country):
        self.family_name=family_name
        self.number_of_members=number_of_members
        self.country=country
    def member_says(self):
        print(f"Hey,I am from{self.family_name} family and there are {self.number_of_members}members in family")
class Family_detailed(Family):
    def which_country(self):
        print(f"The {self.family_name} family has roots from {self.country}")
a=Family("Rodrigue",5,"pern")
b=Family_detailed("Bezos",15,"UAE")

a.member_says()
b.member_says()
b.which_country()

