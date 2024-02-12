import random
 
class Employee_wage():
 
    def __init__(self):
    
        self.wage_per_hour=20
        self.full_hour=8
       
        self.total_wage = 0


    def check_attendance(self):

        attendance= random.choice(['present', 'absent'])
        return attendance
    
    def emplyoee_wage(self):
        emp_status = self.check_attendance()
        if emp_status == 'present':
            self.total_wage = self.wage_per_hour * self.full_hour
        
        else:
            print('Employee is absent')


        
att=Employee_wage()
# att.check_attendance()
# worked_hour=int(input("enter the hours worked:"))
att.emplyoee_wage()
print(att.total_wage)