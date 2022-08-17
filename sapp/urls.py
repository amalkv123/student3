from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('changecompany',views.changecompany,name='changecompany'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtecompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('emp_grp',views.emp_grp,name='emp_grp'),
    path('emp_add2',views.emp_add2,name='emp_add2'),
    path('emp_add',views.emp_add,name='emp_add'),
    path('employee',views.employee,name='employee'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('payheads',views.payheads,name='payheads'),
    path('attendence3',views.attendence3,name='attendence3'),
    path('attendence',views.attendence,name='attendence'),
    path('attendence4',views.attendence4,name='attendence4'),
    path('attendence_edit/<int:pk>',views.attendence_edit,name='attendence_edit'),
    path('attendence_edit2/<int:pk>',views.attendence_edit2,name='attendence_edit2'),
    path('emp_grp2',views.emp_grp2,name='emp_grp2'),
    path('employee2',views.employee2,name='employee2'),
    path('payheads2',views.payheads2,name='payheads2'),
    path('attendence2',views.attendence2,name='attendence2'),
    path('payroll',views.payroll,name='payroll'),
    path('emp_gredit/<int:pk>',views.emp_gredit,name='emp_gredit'),
    path('emp_gredit2/<int:pk>',views.emp_gredit2,name='emp_gredit2'),
    path('add_voucher',views.add_voucher,name='add_voucher'),
    path('add_voucher2',views.add_voucher2,name='add_voucher2'),
    path('add_voucher3',views.add_voucher3,name='add_voucher3'),
    path('add_voucher_edit/<int:pk>',views.add_voucher_edit,name='add_voucher_edit'),
    path('add_voucher_edit2/<int:pk>',views.add_voucher_edit2,name='add_voucher_edit2'),
    path('unit',views.unit,name='unit'),
    path('unit2',views.unit2,name='unit2'),
    path('unit3',views.unit3,name='unit3'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('unit_edit/<int:pk>',views.unit_edit,name='unit_edit'),
    path('unit_edit2/<int:pk>',views.unit_edit2,name='unit_edit2'),
    path('gst3',views.gst3,name='gst3'),
    path('panadd',views.panadd,name='panadd'),
    path('pan2',views.pan2,name='pan2'),
    path('gst2',views.gst2,name='gst2'),
    path('add_payhead',views.add_payhead,name='add_payhead'),
    path('payhead_edit/<int:pk>',views.payhead_edit,name='payhead_edit'),
    path('payhead_edit2/<int:pk>',views.payhead_edit2,name='payhead_edit2'),
    path('salary',views.salary,name='salary'),
    path('salary2',views.salary2,name='salary2'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    path('load',views.load,name='load'),
    path('salary3',views.salary3,name='salary3'),
    path('bank',views.bank,name='bank'),
    path('add_bank3',views.add_bank3,name='add_bank3'),
   






    
]