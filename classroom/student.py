class Student:
    def __init__(self,name,lastname,department,year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def __str__(self):
        return f'name: {self.name}, lastname: {self.lastname}, department: {self.department}, year_of_entrance: {self.year_of_entrance}'
student = Student('Albert','Penn','German',2019)
print(student)


