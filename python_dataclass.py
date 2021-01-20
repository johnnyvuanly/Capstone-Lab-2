# Editing our Student class and turning it into a dataclass

from dataclasses import dataclass

@dataclass # dataclass is a decorator
# Python has generated an init method for us and also generated a string method
class Student:
    name: str
    college_id: str
    gpa: float

    def __str__(self):
        return f'Name {self.name}, GPA: {self.gpa}' 
        # With out these lines it would return the lines below. This allows to customize reponse and make cleaner
        # Student(name='Alex', college_id='abcdef')
        # Student(name='Sam', college_id='qwerty')

def main():
    alex = Student('Alex', 'abcdef', 3.07)
    print(alex.name) 
    print(alex.college_id) 
    print(alex) 

    sam = Student('Sam', 'qwerty', 4.00)
    print(sam)

# Define main before calling it 

main() # We have to call our main method in others words we have to call our funtions. Without this nothing happens
