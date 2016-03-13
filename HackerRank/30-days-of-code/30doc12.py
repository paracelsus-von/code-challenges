class Grade(Student):
    def __init__(self,firstName,lastName,phone,score):
        Student.firstName=firstName
        Student.lastName=lastName
        Student.phone=phone
        self.score = score
            
    def calculate(self):
        if score < 40:
            self.grade = 'D'
        elif score < 60:
            self.grade = 'B'
        elif score < 75:
            self.grade = 'A'
        elif score < 90:
            self.grade = 'E'
        else:
            self.grade = 'O'
        return self.grade