from django.shortcuts import render,redirect
from manager.models import UserInfoTable,ProductType,ProductSize,ProductCategory,ProductDetails,ProductBrand
from manager.forms import UserInfoTableForm,ProductBrandForm,ProductCategoryForm,ProductDetailsForm,\
    ProductSizeForm, ProductTypeForm,roletableForm
from misc import authrize as au

def manager_view(request):
    auth = au.authriseuser(request.session["authenticated"], request.session["roleid"], 1)
    if auth==True:
        return render(request, "managerindex.html")
    else:
        at, message = auth
        if (message == "not authorised"):
            return redirect("/notauthorised/")
        elif (message == "not logged in"):
            return redirect("/notlogin/")

    #return render(request, "managerindex.html")

def change_password_view(request):
    if request.method == "POST":
        opswd = request.POST['oldtxtpassword']
        npswd = request.POST['newtxtpassword']
        useremail = request.session['useremail']
        getuser = UserInfoTable.objects.get(tbuseremail=useremail)
        roleid = getuser.tbuserroleid
        oldpass = getuser.tbuserpassword

        if opswd == oldpass:
           # getuser.tbuserpassword = npswd
            #getuser.save()
            update = UserInfoTable(tbuseremail=useremail, tbuserpassword=npswd)
            update.save(update_fields=["tbuserpassword"])
            if roleid == 1:
               return render(request, "managerindex.html")
            elif roleid == 2:
               return render(request, "shopkeeperindex.html")
            elif roleid == 3:
               return render(request, "buyerindex.html")
    return render(request, "changepassword.html")


def producttype_view(request):
    if request.method == "POST":
        try:
            ptype = request.POST['txtproducttype']
            useremail = request.session['useremail']
            getuser = UserInfoTable.objects.get(tbuseremail=useremail)
            roleid = getuser.tbuserroleid_id
            if roleid == 1:
                obj = ProductTypeForm(request.POST)
                if obj.is_valid():
                    f = obj.save(commit=False)
                    f.tbproducttypename =ptype
                    f.save()
                    return render(request, 'producttype.html')
            else:
                return render(request, "login.html")

        except:

            return render(request, "login.html")
    return render(request, 'producttype.html')

def productcategory_view(request):
     if request.method =="POST":
         pcategory = request.POST['txtproductcategory']
         useremail = request.session['useremail']
         getuser = UserInfoTable.objects.get(tbuseremail=useremail)
         roleid = getuser.tbuserroleid_id
         if roleid == 1:
             obj = ProductCategoryForm(request.POST)
             if obj.is_valid():
                 f = obj.save(commit=False)
                 f.tbcategorytype = pcategory
                 f.save()
                 #return render(request, "abc.html")
                 return render(request, "category.html")
         else:
            return render(request, "login.html")
     return render(request, "category.html")


def productbrand_view(request):
    if request.method == "POST":
        pbrand = request.POST['txtproductbrand']
        useremail = request.session['useremail']
        getuser = UserInfoTable.objects.get(tbuseremail=useremail)
        roleid = getuser.tbuserroleid_id
        if roleid == 1:
            obj = ProductBrandForm(request.POST)
            if obj.is_valid():
                f = obj.save(commit=False)
                f.tbbrandname = pbrand
                f.save()
                # return render(request, "abc.html")
                return render(request, "productbrand.html")
        else:
            return render(request, "login.html")
    return render(request, "productbrand.html")

def productsize_view(request):
    category = ProductCategory.objects.all()
    param = {'category': category}
    if request.method == "POST":
        psize = request.POST['txtproductsize']
        pcategoryid = request.POST['categoryid']
        useremail = request.session['useremail']
        getuser = UserInfoTable.objects.get(tbuseremail=useremail)
        roleid = getuser.tbuserroleid_id
        if roleid == 1:
            obj = ProductSizeForm(request.POST)
            if obj.is_valid():
                f = obj.save(commit=False)
                f.tbproductsize = psize
                f.tbcategoryid_id = pcategoryid
                f.save()
                # return render(request, "abc.html")
                return render(request, "productsize.html", param)
        else:
            return render(request, "login.html")
    return render(request, "productsize.html", param)
