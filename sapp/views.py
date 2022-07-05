from django.shortcuts import render,redirect
import os
from sapp.models import crtcompony,empgroup2,Employee
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request, 'base.html')

def changecompany(request):
    return render(request, 'changecompany.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Compony added successfully!")
        
        return redirect('/')

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})


#payroll

def emp_grp(request):
    
    return render(request,'employegroup2.html')     

def employee(request):
    return render(request,'employe2.html')   

def payheads(request):
    return render(request,'payheads2.html')   

def attendence(request):
    return render(request,'attendence2.html')



    #edit


def emp_grp2(request):
    data=empgroup2.objects.all()
    return render(request,'employegroup.html',{'p':data})  


def emp_add(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        
        tut=empgroup2(groupname=name,groupalias=alias,groupunder=under)
        tut.save()
        return redirect('emp_add2')
    return render(request,'employegroup2.html')   

def emp_add2(request):
    emp=empgroup2.objects.all()
    return render(request,'employegroup2.html',{'data':emp})  

def emp_gredit(request,pk):
    data=empgroup2.objects.get(id=pk)
    return render(request,'gredit.html',{'p':data}) 

def emp_gredit2(request,pk):
    if request.method=='POST':
        datas=empgroup2.objects.get(id=pk)
        datas.groupname =request.POST.get('name')
        datas.groupalias = request.POST.get('alias')
        datas.groupunder = request.POST.get('under')
        

        datas.save()
        return redirect('emp_add2')




def employee2(request):
    return render(request,'employe.html')   

def payheads2(request):
    return render(request,'payheads.html')   

def attendence2(request):
    return render(request,'attendence.html') 


def save_employee(request):

    if request.method == 'POST':

        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['underr']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        
        obj = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            emailid = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,


        )

        obj.save()
        return render(request,'load_create_employee.html')

                 



def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')



