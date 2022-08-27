from timeit import default_timer
from turtle import pos
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from .models import Enterp, Investor, Forum, Comments

# Create your views here.

def index(request):
    i=0
    j=0
    EE = []
    while j!=3:        
        obj = Enterp.objects.filter(id=i).first()
        if obj is not None:
            EE.append(obj)
            j=j+1        
        i=i+1
    return render(request, 'index.html', {'ents': EE})

def signup(request):
    return render(request, 'signup1.html')

def browse(request):
    II = Investor.objects.all()
    EE = Enterp.objects.all()    
    if request.method == 'POST':
        searchx = request.POST.get("searchx")
        category = request.POST.get("filterq")
        search = searchx.lower()
        
        II1=[]
        EE1=[]

        if search == "":
            if category == 'all':
                II1 = Investor.objects.all()
                EE1 = Enterp.objects.all()
            else:
                II1 = Investor.objects.filter(invfield = category)
                EE1 = Enterp.objects.filter(field = category)
            return render(request, 'browse.html', { 'invs': II1, 'ents': EE1})
        else:
            for i in Investor.objects.all():
                name = i.firmname.lower()+i.name.lower()
                result = name.find(search)            
                if result != -1 and category == 'all':
                    II1.append(i)
                elif result != -1 and i.invfield == category:
                    II1.append(i)

            for e in Enterp.objects.all():
                name = e.companyname.lower()+e.name.lower()
                result = name.find(search)
                if result != -1 and category == 'all':
                    EE1.append(e)
                elif result != -1 and e.field == category:
                    EE1.append(e)
            return render(request, 'browse.html', {'invs': II1, 'ents':EE1})                    
    return render(request, 'browse.html', {'invs': II, 'ents': EE})

def signup_ent(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username = username).first():
            messages.info(request, 'Username Taken')
            return redirect('/signup_ent')    

        if User.objects.filter(email = email).first():
            messages.info(request, 'Email Already In Use')
            return redirect('/signup_ent')    

        user_obj=User(username = username, email=email)        
        user_obj.set_password(password)
        user_obj.save()
        i=1
        while True:
                if(Enterp.objects.filter(id=i)):
                        i=i+1
                else:
                        break
        ent_obj = Enterp.objects.create(id =i,user = user_obj, username = username, email = email, name = name,is_investor = False)
        ent_obj.save()
        return redirect('/login')
    return render(request, 'signup_ent.html')

def signup_inv(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username = username).first():
            messages.info(request, 'Username Taken')
            return redirect('/signup_inv')    

        if User.objects.filter(email = email).first():
            messages.info(request, 'Email Already In Use')
            return redirect('/signup_inv')    

        user_obj=User(username = username, email=email)
        user_obj.is_staff=True
        user_obj.set_password(password)
        user_obj.save()
        i=1
        while True:
                if(Investor.objects.filter(id=i)):
                        i=i+1
                else:
                        break
        inv_obj = Investor.objects.create(id =i, user = user_obj, username = username, email = email, name = name, is_investor = True)
        inv_obj.save()
        return redirect('/login')
    return render(request, 'signup_inv.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')                
        user_obj = Investor.objects.filter(username = username).first()
        if user_obj is None:
            user_obj2 = Enterp.objects.get(username = username)
            dj_login(request, user)
            if user_obj2.companyname == "":
                return redirect('/createprof/'+username)          
            else:
                return redirect('/')
        else:
            user_obj = Investor.objects.get(username = username)
            dj_login(request, user)
            if user_obj.details == "":
                return redirect('/createprof/' + username)
            else:
                return redirect('/')        
    return render(request, 'login.html')
       

def createprof(request, pk):
    if request.method == 'POST':                
        obj = Investor.objects.filter(username = pk).first()
        if obj is None:
            obj2 = Enterp.objects.get(username=pk)
            obj2.companyname = request.POST.get("companyname")
            obj2.bplan = request.POST.get('bplan')
            obj2.qpitch = request.POST.get('qpitch')
            obj2.cfunds = request.POST.get('cfunds')
            obj2.rfunding = request.POST.get('rfunding')
            obj2.field = request.POST.get('field')            
            obj2.save()
            return redirect('/')
        else:            
            obj.firmname = request.POST.get("firmname")        
            obj.networth = request.POST.get("networth")
            obj.comphold = request.POST.get("comphold")
            obj.invfield = request.POST.get("field")
            obj.details = request.POST.get("details")  
            obj.save()
            return redirect('/')
    return render(request, 'createprof.html')

def logoutuser(request):
    logout(request)
    messages.info(request, "Logged Out")
    return redirect('/')

def yprofile(request, pk):
    if request.method == 'POST':
        img = request.FILES.get('image')
        username = request.POST.get('username')
        obj = Investor.objects.filter(username = username).first()
        if obj is None:
            obj=Enterp.objects.filter(username = username).first()
            obj.image = img
            obj.save()
            return redirect('/yprofile/'+username)
        else:
            obj.image = img
            obj.save()
            return redirect('/yprofile/'+username)

    obj = Investor.objects.filter(username = pk).first()
    if obj is None:
        obj=Enterp.objects.filter(username = pk).first()
        return render(request, 'yourprofile.html', {'obj': obj})
    return render(request, 'yourprofile.html', {'obj': obj})

def forums(request):
    ff = Forum.objects.all()
    cc = Comments.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        posteruname = request.POST.get('username')
        image = request.FILES.get('image')        
        new_obj = Forum.objects.create( title = title, details = content, posteruname = posteruname, image = image)
        new_obj.save()
    return render(request, 'forums.html', {'forums': ff, 'comments': cc})

def deletepost(request, pk):
    Forum.objects.filter(id=pk).delete()
    return redirect('/forums')
    
def ccomment(request):    
    comment = request.POST.get('comment')
    reuname = request.POST.get('recieveruname')
    senduname = request.POST.get('senderuname')
    i=1
    while True:
            if(Comments.objects.filter(id=i)):
                    i=i+1
            else:
                    break
    new_obj = Comments.objects.create(id = i,  recieveruname = reuname, senderuname = senduname, comment = comment)
    new_obj.save()
    return redirect('/forums')

