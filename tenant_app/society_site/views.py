from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from.models import tenant,personaldata,MeterRecord,Submeter,Tanker

# Create your views here.

def index(request):
    return render(request,"index.html")

# <---ADDTENANT--->
def addtenant(request):
    return render(request,"tenantadd.html")

# <---DEMO--->
def demo(request):
    return render(request,"demo.html")

# <---LOGINN--->
def login(request):
    return render(request,"login.html")

# <---REGISTER--->
def register(request):
    return render(request,"register.html")

# <---ADDINGTENANTS--->
def addingtenants(request):
    if request.method=='POST':
        room=request.POST['roomno']
        tn=request.POST['tenantname']
        ad=request.POST['address']
        adhar=request.POST['aadhar']
        r=request.POST['Rent']
        m=request.POST['mobileno']
    
    t=tenant(roomno=room,name=tn,address=ad,adharno=adhar,rent=r,mobile=m)
    t.save()
    messages.success(request, "Tenant added successfully!")
    return redirect("/tenantdata")

# <---TENANTDATA--->
def tenantdata(request):
    data = tenant.objects.all().order_by('id')  # Ascending order by default
    return render(request, "tenantdata.html", {'data': data})

# <---DELETETENANT--->
def deletetenant(request):
    roomno= request.GET['roomno'] 
    tenant.objects.filter(roomno=roomno).delete() 
    messages.success(request, "Tenant deleted successfully!") 
    return redirect("/tenantdata") 

# <---PROFILEUPDATE--->
def profileupdate(request):
    roomno=request.GET['roomno']
    
    data=tenant.objects.all().filter(roomno=roomno)
    
    return render(request,"updateform.html",{'data':data})

# <---TENANTEDIT--->
def edit(request):
    if request.method == "POST":
        roomno=request.POST['roomno']
        tn=request.POST['tenantname']
        ad=request.POST['address']
        adhar=request.POST['aadhar']
        r=request.POST['Rent']
        m=request.POST['mobileno']
        
        tenant.objects.all().filter(roomno=roomno).update(name=tn,address=ad,adharno=adhar,rent=r,mobile=m)
        return redirect("/tenantdata")
    
# <---REGISTERED--->
def registered(request):
    if request.method=='POST':
        nm=request.POST['name']
        em=request.POST['email']
        ps=request.POST['password']
        
        p=personaldata(name=nm,email=em,password=ps)
        p.save()
        
        return render(request,"login.html")
    
# <---LOGIN--->    
def logined(request):
     if request.method=='POST':
        em=request.POST["email"]
        ps=request.POST["password"]
    
        data=personaldata.objects.all().filter(email=em,password=ps)
        
        if data:
            request.session["username"]=em  
            messages.success(request,"Login successfully completed") 
        
            return redirect('/index')
        else:
             return redirect('/')    
         
# <---SEARCH--->             
def search(request):
    search_query = request.GET.get('searchQuery', '')  # Get search query from the URL
    if search_query:
        # If there's a search query, filter tenants by room number
        data = tenant.objects.filter(roomno__icontains=search_query).order_by('id')
    else:
        # If no search query, show all tenants
        data = tenant.objects.all().order_by('id')

    return render(request, "tenantdata.html", {'data': data})

# <---MAINMETER--->    
def mainmeter(request):
    return render(request,"mainmeter.html")

# <---MAINMETERENTRY--->
def mainmeterentry(request):
    if request.method=='POST':
        m=request.POST["meter"]
        mo=request.POST["month"]
        y=request.POST["year"]
        u=request.POST["units"]
        a=request.POST["amount"]
        
        m=MeterRecord( meter_no=m,month=mo,year=y,units_consumed=u,amount=a)
        m.save()
        return redirect('/index') 
    
# <---SUBMETER--->    
def submeter(request):
    return render(request,"submeter.html")

# <---SUBMETERENTRY--->    
def submeterentry(request):
    if request.method=='POST':
        roomno=request.POST["roomnoo"]
        p=request.POST["previousreading"]
        c=request.POST["currentreading"]
        m=request.POST["month"]
        y=request.POST["year"]
        
        s=Submeter( roomno=roomno,p=p,c=c,month=m,year=y)
        s.save()
        return redirect('/index')
    
# <---TANKER--->
def tanker(request):
    return render(request,"tanker.html") 

# <---ADDTANKER---> 
def addtanker(request):
    if request.method=='POST':
        month=request.POST["month"]
        year=request.POST["year"]
        t=request.POST["totaltanker"]
        a=request.POST["amount"]
        ma=request.POST["mamount"]
        tenant=request.POST["tenantno"]
        
        t=Tanker( month=month,year=year,totaltanker=t,amounttanker=a,maintenance=ma,tenantno=tenant)
        t.save()
        return redirect('/index')
    
    
# <---GALLARY---> 
def gallary(request):
    return render(request,"gallary.html")

# <---LOGOUT--->
def logout(request):
    del request.session["username"]
    messages.success(request,"logout succesfully")
    return redirect("/")


# <---ADDCOOKIE--->
def addcookie(request):
    res=HttpResponse ("cookie set succesfully")
    
    res.set_cookie("studentname","baliram")
    res.set_cookie("studentaddrss","jalna")
    
    return res
