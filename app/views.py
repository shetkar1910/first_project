from django.shortcuts import render, redirect

from .models import Employee

# Create your views here.


def get_employees(request):
    # all_emps = Employee.objects.all()
    all_emps = Employee.objects.filter(is_deleted=False)

    return render(
        request=request, template_name="get_employees.html", context={"emps": all_emps}
    )


def create_employee(request):
    if request.method == "POST":
        # print(request.POST)
        ename = request.POST.get("nm")
        eemail = request.POST.get("em")
        enum = request.POST.get("mn")
        edesn = request.POST.get("edesn")
        esal = request.POST.get("sal")
        
        if not request.POST.get("id"):
            Employee.objects.create(
                name=ename,
                email=eemail,
                mobile_num=enum,
                designation=edesn,
                salary=esal,
            )
        else:
            emp = Employee.objects.get(id=request.POST.get("id"))
            emp.name = ename
            emp.email = eemail
            emp.mobile_num = enum
            emp.designation = edesn
            emp.salary = esal
            emp.save()

        return redirect("get_emps")
    elif request.method == "GET":
        return render(request=request, template_name="create_employee.html")


def get_employee(request, eid):
    emp = Employee.objects.get(id=eid)
    return render(
        request=request,
        template_name="create_employee.html",
        context={"single_emp": emp},
    )


def update_employee(request):
    pass


def delete_employee(request, eid):
    # emp = get_object_or_404(Employee, id=eid)
    emp = Employee.objects.get(id=eid)
    emp.is_deleted = True
    emp.save()

    return redirect('get_emps')
