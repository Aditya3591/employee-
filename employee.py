import random
 
class Employee_wage():
 
    def __init__(self):
    
        self.wage_per_hour=20
        self.full_hour=8
        self.part_time=4
        self.total_wage = 0


    def check_attendance(self):

        attendance= random.choice(['present', 'absent','halfday'])
        return attendance
    
    def emplyoee_wage(self):
        emp_status = self.check_attendance()
        if emp_status == 'present':
            self.total_wage = self.wage_per_hour * self.full_hour
        elif emp_status == 'halfday':
            self.total_wage = self.wage_per_hour * self.part_time
        else:
            print('Employee is absent')


        
emp1=Employee_wage()

emp1.emplyoee_wage()
print(emp1.total_wage)