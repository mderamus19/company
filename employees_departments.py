# Create an Employee type that contains information about employees of a company.
# Each employee must have a name, job title, and employment start date.
# Create a Company type that employees can work for. A company should have a
# business name, address, and industry type.
# Create two companies, and 5 people who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a business name, and its employees.
class Employee:
    '''creating employee profile'''

    def __init__(self, name, job_title, emp_start_date):
        '''initializing employee profile'''
        self.name = name
        self.job_title = job_title
        self.emp_start_date = emp_start_date


class Company:
    '''create a company'''

    def __init__(self,business_name, address, industry):
        '''initialize company attributes'''
        self.business_name = business_name
        self.address = address
        self.industry = industry
        self.employees = list()

facebook = Company("Facebook", "Huntsville", "Social Media")
intuitive = Company("Intuitive", "Research Park", "Research")
misty = Employee("Misty", "Software Developer", "Nov 12, 2019")
chris = Employee("Chris", "Network Administrator", "October 21, 2019")
girtie = Employee("Girtie", "Administrator", "October 25, 2019")
hank = Employee("Hank", "Engineer", "September 21, 2019")
josh = Employee("Josh", "Systems Administrator", "November 21, 2019")

facebook.employees.append(misty)
facebook.employees.append(josh)
intuitive.employees.append(chris)
intuitive.employees.append(girtie)
intuitive.employees.append(hank)

print(f"{facebook.business_name} is in the {facebook.industry} industry and has the following employees:")
for employee in facebook.employees:
    print(f"{employee.name}")
print(f"\n{intuitive.business_name} is in the {intuitive.industry} industry and has the following employees:")
for employee in intuitive.employees:
    print(f"{employee.name}")