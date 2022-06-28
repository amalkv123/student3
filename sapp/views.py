import email
from django.shortcuts import render ,redirect
from django.contrib import messages

from sapp.models import student_details
# Create your views here.

# load register page
def student(request):
    return render(request,'student.html')

#add students data in mysql  
def add_students_data(request):
    if request.method=='POST':
        sname=request.POST['student_name']
        email=request.POST['email']
        gen=request.POST['gender']
        quli=request.POST['qulification']
        age=request.POST['Age']
        phn=request.POST['Phone_Number']
        date=request.POST['Date']
        address=request.POST['Address']

        student=student_details(student_name=sname,
                                email=email,
                                gender=gen,
                                qulification=quli,
                                age=age,
                                phone_number=phn,
                                date=date,
                                address=address)  

        student.save()
        print('heloo')
        return redirect('show')


#show students datas   

def show(request):
    datas=student_details.objects.all()
    return render(request,'showstu.html',{'datas':datas})


# edit 
def editpage(request,pk):
    datas=student_details.objects.get(id=pk)
    return render(request,'edit.html',{'datas':datas})


#edit and upadte students datas

def editstudent_data(request ,pk):
    if request.method=='POST':
        datas=student_details.objects.get(id=pk)
        datas.student_name =request.POST.get('student_name')
        datas.email = request.POST.get('email')
        datas.qulification = request.POST.get('qulification')
        datas.age = request.POST.get('Age')
        datas.phone_number = request.POST.get('Phone_Number')
        datas.address = request.POST.get('Address')

        datas.save()
        return redirect('show')
      

# load delete page
#def delete(request,pk):
 #   datas=student_details.objects.get(id=pk)
  #  return render(request,'delete.html',{'datas':datas})

#delete student data

def delete_product(request,pk):
    datas=student_details.objects.get(id=pk)
    datas.delete()
    messages.success(request,'student data sucessfully deleted')
    return redirect('show')



#student detail view 

def detailview(request,pk):
    datas=student_details.objects.get(id=pk)
    return render(request,'detailsview.html',{'datas':datas})  