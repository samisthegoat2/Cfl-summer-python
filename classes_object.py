class student:
    def __init__(self,name,age,ethnicity,location,interest,school,grade,friend):
        self.name = name
        self.age = age
        self.ethnicity  = ethnicity
        self.location = location
        self.interest = interest
        self.school = school
        self.grade = grade
        self.friend = friend


    def introductions(self):
        return print(f"Hi, my name is {self.name} and I am in {self.grade}")



student1 = student("Samuel", 12, "Black", "Honduras", "Soccer", "middle school", 8, "Mark")
student2 = student("Daniel", 15, "Dominican", "united states", "writing", "Food and finance", 10, "Jack")
student3 = student("Micah", 15, "Black", "Bronx", "coding", "High school", 11, "John")

print(student2.friend)

print(student1.introductions())
print(student2.introductions())
print(student3.introductions())