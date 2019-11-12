from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def showData(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    email = request.POST.get("t3")
    dob = request.POST.get("t4")
    gender = request.POST.get("t5")
    designation = request.POST.get("t6")
    ts = request.POST.getlist("t7")
    edu = request.POST.getlist("t8")
    password = request.POST.get("t9")
    address = request.POST.get("t10")

    print(name)
    print(age)
    print(email)
    print(dob)
    print(gender)
    print(designation)
    print(ts)
    print(edu)
    print(password)
    print(address)
    return None