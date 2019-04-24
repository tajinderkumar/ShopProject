from django.shortcuts import render, redirect
from manager.models import UserInfoTable
from django.core.files.storage import FileSystemStorage
from manager.forms import UserInfoTableForm,roletableForm
import random
from django.contrib.auth.hashers import make_password,check_password
from  misc import emailsendingfile as ef
from misc import authrize as au


# Create your views here.
def home_view(request):
    return render(request, "buyerindex.html")
    """auth = au.authriseuser(request.session["authenticated"], request.session["roleid"], 3)
    if auth == True:
        return render(request, "buyerindex.html")
    else:
        at, message = auth
        if message == "not authorised":
            return redirect("/notauthorised/")
        elif message == "not logged in":
            return redirect("/notlogin/")
    return render(request, "buyerindex.html")"""

def buyredashboard_view(request):
    return render(request, "buyerdashboard.html")

def login_view(request):
    if(request.method=="POST"):
            pwd=""
            try:
                ue = request.POST["logintxtemail"]

                getUser = UserInfoTable.objects.get(tbuseremail=ue)
                #return render(request, "okkkk.html")
                is_verified = getUser.tbisverified
                pwd = request.POST['logintxtpassword']
                dbpwd = getUser.tbuserpassword

                if pwd == dbpwd:
                    result = True
                else:
                    result = False
                    return render(request, 'login.html', {'wrongpassword': True})
            except:
                return render(request, 'login.html', {'wronguname': True})
           # if is_verified:
            if result:
                  #return render(request, "okkkk.html")
                  request.session['authenticated'] = True
                  request.session['roleid'] = getUser.tbuserroleid_id
                  request.session['useremail'] = getUser.tbuseremail
                  request.session['username']= getUser.tbusername
                  if request.session['roleid'] == 1:
                    return redirect('/manager/')
                  if request.session['roleid'] == 2:
                    return redirect('/shopkeeper/')
                  if request.session['roleid'] == 3:
                    return redirect('/buyer/')

    return render(request, "login.html")

def signup_view(request):
    if request.method == 'POST':
        obj = UserInfoTableForm(request.POST)
        if obj.is_valid():
            f = obj.save(commit=False)
            user_image = ""
            adhar_image = ""
            pan_image = ""
            adhar_number = ""
            pan_number = ""
            otp =""
            otptime = ""

            dropdownvalue=request.POST["dropdown"]
            if(dropdownvalue=="1" or dropdownvalue=="2"):
                #return render(request,"abcd1.html")
                if request.FILES:
                        myfile = request.FILES['userimage']
                        fs = FileSystemStorage()
                        filename = fs.save(myfile.name, myfile)
                        fs.url(filename)
                        user_image = myfile.name

            if(dropdownvalue=="2"):
                adhar_number = request.POST["txtadhar"]
                pan_number = request.POST["txtpan"]
                if request.FILES:
                        adharfile = request.FILES['adharimage']
                        fs = FileSystemStorage()
                        filename = fs.save(adharfile.name, adharfile)
                        fs.url(filename)
                        adhar_image = adharfile.name
                        panfile = request.FILES['panimage']
                        fs = FileSystemStorage()
                        filename = fs.save(panfile.name, panfile)
                        fs.url(filename)
                        pan_image = panfile.name
            if dropdownvalue == "1":
                    f.tbuserroleid_id = 3

            elif dropdownvalue == "2":
                    f.tbuserroleid_id = 2
            else:
                    f.tbuserroleid_id = 2


            f.tbusername = request.POST['txtname']
            f.tbuseremail= request.POST['txtemail']
            f.tbusermob = request.POST['txtphone']
            f.tbuseraltmob = request.POST['txtaltphone']
            f.tbuseraddress= request.POST['txtaddress']
            f.tbuserimage = user_image
            f.tbuserpincode = request.POST['txtpincode']
            f.tbuserpassword = request.POST['txtpassword']
            f.tbuseradharimage = adhar_image
            f.tbuserpan = pan_number
            f.tbuseradhar = adhar_number
            f.tbuserpanimage = pan_image
            f.tbotp = otp
            f.tbotptime = otptime
            rn = random.randint(100000,1000000)
            mb = request.POST['txtphone']
            em = request.POST['txtemail']

            token = em[0:7]+str(rn)+mb[5:10]
            entoken = make_password(token)
            f.tbauthtoken = entoken
            link = "http://127.0.0.1:8000/activate/?email="+em+"&token="+entoken
            ef.emailverification(em, link, "link")
            f.save()
            return render(request, "signup.html")
    return render(request, "signup.html")

def logout_view(request):
    request.session["authenticated"] = False
    return  redirect("/")

def activateuser(request):
    em = request.GET["email"]
    tk = request.GET["token"]
    getuser = UserInfoTable.objects.get(tbuseremail=em)
    dbtoken = getuser.tbauthtoken
    if tk == dbtoken:
        update = UserInfoTable(tbuseremail=em, tbisverified=True)
        update.save(update_fields=["tbisverified"])
        return True
    else:
        return False, "You need to verified first"


def notauthorized(request):
    return render(request,"notauthorised.html")


def notlogin(request):
    return render(request,"notlogin.html")