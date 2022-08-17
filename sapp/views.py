from calendar import c
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
import os
from app.models import crtcompony,empgroup2,Employee,create_VoucherModels,Create_attendence,pan,create_payhead,compute_information,Rounding,gratuity,units,gst,add_bank,E_found_trasfer,create_salary,bank3
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




def emp_grp(request):
    
    return render(request,'employegroup2.html')     





 

def pan2(request):
    return render(request,'pan.html')  

def attendence(request):
    data=Create_attendence.objects.all()
    return render(request,'attendence2.html',{'p':data})

def unit2(request):
    return render(request,'unit2.html')

def payroll(request):
    return render(request,'payroll.html')



    #employeegroup


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
    data2=empgroup2.objects.all()
    context={'p':data,
    'p2':data2}
    return render(request,'gredit.html',context) 

def emp_gredit2(request,pk):
    if request.method=='POST':
        datas=empgroup2.objects.get(id=pk)
        datas.groupname =request.POST.get('name')
        datas.groupalias = request.POST.get('alias')
        datas.groupunder = request.POST.get('under')
        

        datas.save()
        return redirect('emp_add2')




  





    #payheads



def payheads(request):
    data=create_payhead.objects.all()
    return render(request,'payheads2.html',{'p':data})  

def payheads2(request):
    data=Create_attendence.objects.all()
    return render(request,'payheads.html',{'p':data})   


def add_payhead(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']
       

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads')


def payhead_edit2(request,pk):
    if request.method=='POST':
        data=create_payhead.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.pay_type=request.POST.get('payhead')
        data.income_type=request.POST.get('income')
        data.under=request.POST.get('under')
        data.affect_net=request.POST.get('netsalary')
        data.payslip=request.POST.get('payslip')
        data.calculation_of_gratuity=request.POST.get('caltype')
        data.cal_type=request.POST.get('ctype')
        data.calculation_period=request.POST.get('caltype')
        data.leave_withpay=request.POST.get('attendence with pay')
        data.leave_with_out_pay=request.POST.get('Attendance with out pay')
        data.production_type=request.POST.get('ptype')
        data.opening_balance=request.POST.get('balance')
        data.save()

        idd=data

        data2=compute_information.objects.get(id=pk)
        data2.compute=request.POST.get('compute')
        data2.effective_from=request.POST.get('effective_from')
        data2.amount_upto=request.POST.get('amount_upto')
        data2.slab_type=request.POST.get('slab_type')
        data2.value=request.POST.get('value')
        data2.Pay_head_id=idd

        data2.save()


        data3=Rounding.objects.get(id=pk)
        data3.Rounding_Method=request.POST.get('roundmethod')
        data3.Round_limit=request.POST.get('limit')
        data3.pay_head_id=idd
        data3.save()

        data4=gratuity.objects.get(id=pk)
        data4.days_of_months=request.POST.get('days_of_months')
        data4.number_of_months_from=request.POST.get('from')
        data4.to=request.POST.get('to')
        data4.calculation_per_year=request.POST.get('eligiibility')
        data4.pay_head_id=idd
        data4.save()
        return redirect('payheads')
    return render(request,'payhead_edit.html')
    

def payhead_edit(request,pk):
    data=create_payhead.objects.get(id=pk)
    data2=compute_information.objects.get(id=pk)
    data3=Rounding.objects.get(id=pk)
    data4=gratuity.objects.get(id=pk)
    context={'p':data,'p2':data2,
    'p3':data3,'p4':data4
    }
    return render(request,'payhead_edit.html',context) 



        
    
    #attendence 



def attendence4(request):
    return render(request,'attendence(sec).html')


def attendence2(request):
    data=Create_attendence.objects.all()
    data2=units.objects.all()

    context={'p':data,
    'p2':data2}
    return render(request,'attendence.html',context)

def attendence3(request):
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('attendence')


def attendence_edit(request,pk):
    data=Create_attendence.objects.get(id=pk)
    data2=Create_attendence.objects.all()
    context={'p':data,
    'p2':data2}
    return render(request,'attendence_edit.html',context) 

def attendence_edit2(request,pk):
    if request.method == 'POST':
        data=Create_attendence.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.under=request.POST.get('under')
        data.type=request.POST.get('type')
        data.save()
        return redirect('attendence')



    #employee

def employee(request):
    p3=Employee.objects.all()
    context={'data':p3}
    return render(request,'employe2.html',context)   

def employee2(request):
    obj=bank3.objects.all()
    data=Employee.objects.all()
    data2=empgroup2.objects.all()
    context={'std':data,
    'p':obj,'p3':data2}
    return render(request,'employe.html',context)

def addemployee(request):
    if request.method=='POST':
        
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
        #Bank
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee(

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
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            
            



        )

        std.save()
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
        return redirect('employee')




#payrolvoucher



def add_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        use_effct_date = request.POST['effect']  
        allow_zero_trans = request.POST['trans']  
        allow_naration_in_vou = request.POST['narr']  
        optional = request.POST['optical'] 
        provide_narr = request.POST['ledg']  
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        std.save()
        return redirect('add_voucher2')

    return render(request, 'payroll.html')  


def add_voucher2(request):
    emp=create_VoucherModels.objects.all()
    return render(request,'payroll2.html',{'data':emp}) 

def add_voucher3(request):
    emp=create_VoucherModels.objects.all()
    return render(request,'payroll.html',{'data':emp}) 

def add_voucher_edit(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    data2=create_VoucherModels.objects.all()
    context={'p':emp,
    'data':data2}
    return render(request,'payrolledit.html',context) 

def add_voucher_edit2(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    emp.voucher_name=request.POST.get('name')
    emp.alias=request.POST.get('alias')
    emp.voucher_type=request.POST.get('type')
    emp.abbreviation=request.POST.get('abber')
    emp.active_this_voucher_type=request.POST.get('active')
    emp.method_voucher_numbering=request.POST.get('numbering')
    emp.use_adv_conf=request.POST.get('config', False)
    emp.prvnt_duplictes=request.POST.get('prevent', False)
    emp.use_effective_date=request.POST.get('effect')
    emp.allow_zero_value_trns=request.POST.get('trans')
    emp.allow_naration_in_voucher=request.POST.get('narr')
    emp.make_optional=request.POST.get('optical')
    emp.provide_naration=request.POST.get('ledg')
    emp.print_voucher=request.POST.get('print')
    emp.save()
    return redirect('add_voucher2')


    #unit




def unit(request):
    p=units.objects.all()
    return render(request, 'unit.html',{'p2':p})

def unit2(request):
    p=units.objects.all()
    return render(request,'unit2.html',{'data':p})

def unit3(request):
    p=units.objects.all()
    return render(request,'unit3.html',{'data':p})

def add_unit(request):
    if request.method=='POST':
        type = request.POST['type']
        symbol = request.POST['symbol']
        formal_name = request.POST['formal']
        number_of_decimal_places = request.POST['decimal']
        first_unit = request.POST['ft']  
        conversion = request.POST['con'] 
        second_unit = request.POST['sec'] 

        std=units(type=type,symbol=symbol,formal_name=formal_name,number_of_decimal_places=number_of_decimal_places,first_unit=first_unit,conversion=conversion,second_unit=second_unit)
        std.save()
        return redirect('unit2')


def unit_edit(request,pk):
    data=units.objects.get(id=pk)
    return render(request,'unit_edit.html',{'p':data})

def unit_edit2(request,pk):
    std=units.objects.get(id=pk)
    std.type=request.POST.get('type')
    std.symbol=request.POST.get('symbol')  
    std.formal_name=request.POST.get('formal')
    std.number_of_decimal_places=request.POST.get('decimal') 
    std.first_unit=request.POST.get('ft')
    std.conversion=request.POST.get('con')
    std.second_unit=request.POST.get('sec')  
    std.save()
    return redirect('unit2')
    






    #pan


def panadd(request):
    if request.method == 'POST':
        tax2=request.POST['tax']
        no2=request.POST['no']

        std = pan(tax3 = tax2,
        no = no2)
        std.save()
        return redirect('pan2')
    return render(request, 'pan.html')




    #gst


def gst3(request):
    return render(request,'gst.html') 


def gst2(request):
    if request.method == 'POST':
        state=request.POST['state']
        type=request.POST['type']
        teretory = request.POST['teretory']
        uin = request.POST['uin']
        gstr1 = request.POST['gstr1']
        kerala = request.POST['kerala']
        set = request.POST['set']
        enable = request.POST['enable']
        enable2 = request.POST['enable2']
        enable3 = request.POST['enable3']
        bond = request.POST['bond']
        taxrate = request.POST['taxrate']
        basistax = request.POST['basistax']
        purchase = request.POST['purchase']
        eway = request.POST['eway']
        applicable = request.POST['applicable']
        thresholt = request.POST['thresholt']
        limit = request.POST['limit']
        infrastate = request.POST['infrastate']
        thresholt2 = request.POST['thresholt2']
        invoice = request.POST['invoice']
        einvoice = request.POST['einvoice']

        std=gst(state=state,type=type,teretory=teretory,uin=uin,gstr1=gstr1,kerala=kerala,set=set,enable=enable,
        enable2=enable2,enable3=enable3,bond=bond,taxrate=taxrate,basistax=basistax,purchase=purchase,
        eway=eway,applicable=applicable,thresholt=thresholt,limit=limit,infrastate=infrastate,thresholt2=thresholt2,
        invoice=invoice,einvoice=einvoice)

        std.save()
        return redirect('gst3')
        



#salary



def salary(request):
    p=create_payhead.objects.all()
    return render(request,'salary.html',{'pay':p}) 

def salary2(request):
    data2=empgroup2.objects.all()
    return render(request,'salary2.html',{'data':data2}) 

def salary3(request):
    pk=create_payhead.objects.all()
    if request.method=='POST':
        name2=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=create_salary(name=name2,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   payheaad_type=payhead,
                   calculation_type=calculation,
        )
        std.save()
        return redirect('salary')
    return render(request,'salary.html',{'pk':pk})






def load(request):
    did=request.GET.get("id")
    print("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})





def bank(request):
    obj=bank3.objects.all()
    return render(request,"bank.html",{"p":obj})

def add_bank3(request):
    obj=bank3.objects.all()
    if request.method=="POST":
        nam=request.POST['name']
        std=bank3(name=nam)
        std.save()
        return redirect('employee2')



                



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



