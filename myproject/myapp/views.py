# myapp/views.py

from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
import csv
from django.contrib.auth import authenticate, login, logout
import subprocess



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username=="A" and password=="123"):
            return redirect('/myapp/A')
        if (username=="B" and password=="123"):
            return redirect('/myapp/B')
        if (username=="C" and password=="123"):
            return redirect('/myapp/C')
        if (username=="D" and password=="123"):
            return redirect('/myapp/D')
    return render(request, 'login.html')


def csv_to_list(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


def csv_view(request):
    response = HttpResponse()
    response['X-Frame-Options'] = 'SAMEORIGIN'
    csv_file_path = 'C:\\Users\\Ashwin\\Desktop\\Django\\Django\\myproject\\log.csv'
    data = csv_to_list(csv_file_path)
    return render(request, 'csv.html', {'data': data})


def my_view(request):
    if request.method == 'POST':
        current_datetime = datetime.now()
        now = current_datetime.strftime("%H:%M:%S")
        file = open("log.csv", 'a')
        check1 = request.POST.get('myCheckbox')
        check2 = request.POST.get('myCheckbox1')
        check3 = request.POST.get('myCheckbox2')
        check4 = request.POST.get('hp')
        option1= request.POST.get('myComboBox')
        option2= request.POST.get('myComboBox1')
        option3= request.POST.get('myComboBox2')
        dis_location=request.POST.get('dis_loc')
        destination= "12"
        req_type=""
        passnode=""
        if(check4=="highp"):
            hp="High"
        else:
            hp="None"
        if(str(check1)!="None"):
            req_type=str(check1)
            passnode=option1
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(destination)+',Raised'+',,,'+hp+'\n')
        if(str(check2)!="None"):
            req_type=str(check2)
            passnode=option2
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(dis_location)+',Raised'+',,,'+hp+'\n')
        if(str(check3)!="None"):
            req_type=str(check3)
            passnode=option3
            file.write(','+str(now)+','+req_type+','+destination+','+str(passnode)+',Raised'+',,,'+hp+'\n')
        file.close()
        
        if hp=="High":
            subprocess.run(["python", "C:\\Users\\Ashwin\\Desktop\\Django\\Django\\myproject\\priority.py"])

        # Do something with the name and email values
        return HttpResponse('Thanks for submitting the form!')
    else:
        return render(request, 'A_site.html')

def my_view2(request):
    if request.method == 'POST':
        current_datetime = datetime.now()
        now = current_datetime.strftime("%H:%M:%S")
        file = open("log.csv", 'a')
        check1 = request.POST.get('myCheckbox')
        check2 = request.POST.get('myCheckbox1')
        check3 = request.POST.get('myCheckbox2')
        option1= request.POST.get('myComboBox')
        option2= request.POST.get('myComboBox1')
        option3= request.POST.get('myComboBox2')
        dis_location=request.POST.get('dis_loc')
        destination= "22"
        req_type=""
        passnode=""
        if(str(check1)!="None"):
            req_type=str(check1)
            passnode=option1
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(destination)+',Raised'+',,\n')
        if(str(check2)!="None"):
            req_type=str(check2)
            passnode=option2
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(dis_location)+',Raised'+',,\n')
        if(str(check3)!="None"):
            req_type=str(check3)
            passnode=option3
            file.write(','+str(now)+','+req_type+','+destination+','+str(passnode)+',Raised'+',,\n')

        file.close()
        # Do something with the name and email values
        return HttpResponse('Thanks for submitting the form!')
    else:
        return render(request, 'B_site.html')
    
def my_view3(request):
    if request.method == 'POST':
        current_datetime = datetime.now()
        now = current_datetime.strftime("%H:%M:%S")
        file = open("log.csv", 'a')
        check1 = request.POST.get('myCheckbox')
        check2 = request.POST.get('myCheckbox1')
        check3 = request.POST.get('myCheckbox2')
        option1= request.POST.get('myComboBox')
        option2= request.POST.get('myComboBox1')
        option3= request.POST.get('myComboBox2')
        dis_location=request.POST.get('dis_loc')
        destination= "32"
        req_type=""
        passnode=""
        if(str(check1)!="None"):
            req_type=str(check1)
            passnode=option1
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(destination)+',Raised'+',,\n')
        if(str(check2)!="None"):
            req_type=str(check2)
            passnode=option2
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(dis_location)+',Raised'+',,\n')
        if(str(check3)!="None"):
            req_type=str(check3)
            passnode=option3
            file.write(','+str(now)+','+req_type+','+destination+','+str(passnode)+',Raised'+',,\n')

        file.close()
        # Do something with the name and email values
        return HttpResponse('Thanks for submitting the form!')
    else:
        return render(request, 'C_site.html')

def my_view4(request):
    if request.method == 'POST':
        current_datetime = datetime.now()
        now = current_datetime.strftime("%H:%M:%S")
        file = open("log.csv", 'a')
        check1 = request.POST.get('myCheckbox')
        check2 = request.POST.get('myCheckbox1')
        check3 = request.POST.get('myCheckbox2')
        option1= request.POST.get('myComboBox')
        option2= request.POST.get('myComboBox1')
        option3= request.POST.get('myComboBox2')
        dis_location=request.POST.get('dis_loc')
        destination= "15"
        req_type=""
        passnode=""
        if(str(check1)!="None"):
            req_type=str(check1)
            passnode=option1
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(destination)+',Raised'+',,\n')
        if(str(check2)!="None"):
            req_type=str(check2)
            passnode=option2
            file.write(','+str(now)+','+req_type+','+str(passnode)+','+str(dis_location)+',Raised'+',,\n')
        if(str(check3)!="None"):
            req_type=str(check3)
            passnode=option3
            file.write(','+str(now)+','+req_type+','+destination+','+str(passnode)+',Raised'+',,\n')

        file.close()
        # Do something with the name and email values
        return HttpResponse('Thanks for submitting the form!')
    else:
        return render(request, 'D_site.html')