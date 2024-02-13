import random
 
class Employee_wage():
 
    def __init__(self):
    
        self.wage_per_hour=20
        self.full_hour=8
        self.part_time=4
        self.total_wage = 0
        self.month_work_days=20
        self.monthly_target_hours = 100
        self.total_hours_worked = 0
        self.total_days_worked = 0


    def check_attendance(self):

        attendance= random.choice(['present', 'absent','halfday'])
        return attendance
    
    def emplyoee_wage(self):
        emp_status = self.check_attendance()
        if emp_status == 'present':
            self.total_wage += self.wage_per_hour * self.full_hour
            
        elif emp_status == 'halfday':
            self.total_wage += self.wage_per_hour * self.part_time
            
        

    def monthly_wage(self):
        
        while self.total_days_worked < self.month_work_days:
            self.emplyoee_wage()
            self.total_days_worked += 1
    
     
        
emp1=Employee_wage()

emp1.monthly_wage()
print(f"Total wage: {emp1.total_wage}")

