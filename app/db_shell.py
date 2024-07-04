from app.models import Employee

# to execute this file put below on terminal
# exec(open(r'C:\Users\shetk\Desktop\A_Python_B11\DJango_framework\first_project\app\db_shell.py').read())

# employee_data = Employee.objects.all()

# employee_data = Employee.objects.all()[1]


# read all emp
# print(employee_data)

# for emp in employee_data:
#     print(emp.__dict__)

# get single employee

# try:
#     emp = Employee.objects.get(id=3)
#     print(emp)
# except Employee.DoesNotExist:
#     print("Employee Not Exists.")

# create Employee
# 1 way

# emp = Employee(
#     name="Ravan",
#     email="ravan@gmail.com",
#     mobile_num=23434423,
#     designation="tester",
#     salary=56000,
# )

# emp.save()

# 2 nd way

# Employee.objects.create(
#     name="Laxman",
#     email="laxman@gmail.com",
#     mobile_num=2342423,
#     designation="HR",
#     salary=500000,
# )


# Update Emp

# try:
#     emp = Employee.objects.get(id=2)
#     emp.salary = 1000000
#     emp.email = "chotaBheem"
#     emp.save()

# except Employee.DoesNotExist:
#     print("Employee not Exists")


# delete Emp

# try:
#     emp = Employee.objects.get(id=3)
#     emp.delete()

# except Employee.DoesNotExist:
#     print("Employee not Exists")


# emp = Employee.objects.filter(email="sam@gmail.com")
# print(emp)

# emp = Employee.objects.filter(email="saaaaam@gmail.com")
# print(emp)

# emp = Employee.objects.get(email="saaaaam@gmail.com")
# print(emp)

# emp = Employee.objects.filter(designation__startswith="H")
# print(emp)

# emp = Employee.objects.filter(designation__endswith="R")
# print(emp)

# emp = Employee.objects.filter(salary__gte=40000)
# print(emp)

# emp = Employee.objects.order_by('salary')
# print(emp)

# emp = Employee.objects.order_by('-salary')
# print(emp)

# emp = Employee.objects.filter(email__icontains='gmail.com')
# print(emp)

# emp_count = Employee.objects.count()
# print(emp_count)


# get the AVg salary

# from django.db.models import Avg

# avg_salary = Employee.objects.aggregate(Avg("salary"))
# print(avg_salary)


# from django.db.models import Sum

# sum_salary = Employee.objects.aggregate(Sum("salary"))
# print(sum_salary)


# distinct_designations = Employee.objects.values('designation').distinct()

# print(distinct_designations)


# AND

# mid_sal_emp = Employee.objects.filter(salary__gte = 10000, salary__lte = 100000)
# print(mid_sal_emp)


# In

# role_in = Employee.objects.filter(designation__in = ['intern','HR'])
# print(role_in)


# top 2 salary

# top_2_highest_paid = Employee.objects.order_by("-salary")[:2]
# print(top_2_highest_paid)


# non HR

# non_hr = Employee.objects.filter(salary__gte = 50000).exclude(designation="HR")
# print(non_hr)


unique_design = Employee.objects.values('designation').distinct()
print(unique_design)