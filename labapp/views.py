from django.shortcuts import render,redirect
from django.http import HttpResponse
from labapp.models import  Patient
from labapp.models import  Tests
from labapp.models import Testname
from labapp.models import Bill
from django.db.models import Q

# Create your views here.   
def main(request):
    #patient_id=request.Patient.id
    #print(patient_id)
    if request.method=="POST":
        pname=request.POST['pname']
        number=request.POST['number']
        email=request.POST['email']
        pdesc=request.POST['pdesc']
        dname=request.POST['dname']
        pid=request.POST['pid']        
        test_name=request.POST.getlist('test')
        

        p1=Patient.objects.create(pname=pname,number=number,email=email,pdesc=pdesc,dname=dname,is_deleted="N",pid=pid)
        p1.save()
          
        x={}
        for x in test_name:
            
            if x=='C':
                p=1600
            elif x=='H':
                p=638
            elif x=='P':
                p=810
            elif x=='E':
                p=81
            elif x=='B':
                p=110
            tn=Testname.objects.create(test_name=x,tid=pid,price=p)
                        
            tn.save()               
        
        
        if request.method=="POST":
            ts=Tests.objects.create( patient_id=pid, test_id=pid)
            ts.save()

        return redirect('/main')
    else:
        #records=Patient.objects.all()      
        records=Patient.objects.filter(is_deleted="N" )  
       #print(records)      
        content={}
        content['data']=records         
        return render(request,'main.html',content)

def delete(request,rid):
    #x=Patient.objects.get(id=rid) //hard Delete
    #x.delete()
    #Soft delete
    x=Patient.objects.filter(id=rid)
    x.update(is_deleted="Y")

    return redirect('/main')

def edit(request,rid):
    if request.method=="POST":
        upname=request.POST['pname']
        unumber=request.POST['number']
        uemail=request.POST['email']
        updesc=request.POST['pdesc']
        udname=request.POST['dname']
        
        x=Patient.objects.filter(id=rid)
        x.update(pname=upname,number=unumber,email=uemail,pdesc=updesc,dname=udname,)
        return redirect('/main')
    else:
        rec=Patient.objects.get(id=rid)
        content={}
        content['data']=rec
        return render(request,'edit_main.html',content)
def bill(request,rid):
    if request.method=="POST":
        print(rid) 
        x=rid
        tests=[]
        j=Patient.objects.get(id=rid).pid
        print(j)
        name=Patient.objects.get(id=rid).pname
        number=Patient.objects.get(id=rid).number
        email=Patient.objects.get(id=rid).email
        dname=Patient.objects.get(id=rid).dname
        print(name)
        for i in Testname.objects.filter(tid=j):
            y=i.id
            result=Testname.objects.get(id=y).test_name
            tid=Testname.objects.get(id=y).tid
            price=Testname.objects.get(id=y).price
            b1=Bill.objects.create(pname=name,number=number,tid=tid,price=price,dname=dname,email=email,test_name=result,pid=j,test_id=5)
            b1.save()

            tests.append(result)
        print(tests)
        
        #b1=Bill.objects.create(pname=name,test_name=tests,pid=j,test_id=2)
        #b1.save()
        return redirect('/bill/22')
        
    else:      
        x=Patient.objects.get(id=rid).pid
        i=Patient.objects.get(id=rid)
        testlist=[]
        g=Bill.objects.all()
        for j in Bill.objects.filter(pid=x):
            z=j.id
            w=Bill.objects.get(id=z)
            print(w)
            testlist.append(w) 
       
        testlist.append(i) 
        #print(x)
        a=Testname.objects.all()       
        for b in a:
            tid=b.tid            
            #print(tid)
            if(tid==x):
                for rec in Testname.objects.filter(tid=x):
                    y=rec.id
                    #print(y)
                    result=Testname.objects.get(id=y)                 
                    #print(result) 
                    testlist.append(result)
                break
                


        
        print(testlist)

        content={} 
        content['data']=testlist
        
        return render(request,'bill.html',content)

def fbill(request,rid):
    if request.method=="POST":
        pass
    else:   
        pass


                                  



    




    
    
