import random
 
class Employee_wage():
 
    def __init__(self):
        self.attendacne=0

    def check_attendance(self):

        attendance= random.choice(['present', 'absent'])
        print(attendance)
        if attendance == 'present':
            print("employee is present")
        else:
            print("emplyoee is absent")
        
att=Employee_wage()
att.check_attendance()