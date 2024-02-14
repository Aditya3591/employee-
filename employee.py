import random
 
class Employee_wage:
 
    def __init__(self, emp_name):
        self.emp_name = emp_name
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
            self.total_hours_worked+=self.full_hour
        elif emp_status == 'halfday':
            self.total_wage += self.wage_per_hour * self.part_time
            self.total_hours_worked+=self.part_time
        

    def monthly_wage(self):
        
        while self.total_days_worked < self.month_work_days and self.total_hours_worked<self.monthly_target_hours:
            self.emplyoee_wage()
            self.total_days_worked += 1

    
    
    def __repr__(self) -> str:
        return f'Emp salary: {self.total_wage} total days worked:{self.total_days_worked} total hours worked: {self.total_hours_worked}'

    
     
class Company:

    def __init__(self, name):
        self.company_name = name
        self.employee_list={}

    def add_employee(self,emp_obj):
        self.employee_list[emp_obj.emp_name] = emp_obj

    def display(self):
        pass


if __name__ == '__main__':

    company = Company('SRM')
    while True:
        choice = int(input("choice: "))
        if choice == 0:
            break
        emp_name = input("Emp name: ")
        emp = Employee_wage(emp_name)
        emp.monthly_wage()
        company.add_employee(emp)

        print(company.employee_list)
     #print(__name__)
     #emp=Employee_wage('Aditya')
     #emp.monthly_wage()
     #print(f"Total wage is: {emp.total_wage}\ntotal hours works is : {emp.total_hours_worked}\ntotal days worked is : {emp.total_days_worked}")
     #company = Company('SRM')
     #company.add_employee(emp)
     #print(company.employee_list)



    

     