from django.shortcuts import render,redirect
from manager.models import UserInfoTable,roletable,ProductSubCategory,\
    ProductCategory,ProductSize,ProductBrand,ProductDetails,ProductType
from misc import authrize as au
# Create your views here.
def shopkeeper_index_view(request):
    auth = au.authriseuser(request.session["authenticated"], request.session["roleid"], 2)
    if auth == True:
        return render(request, "shopkeeperindex.html")
    else:
        at, message = auth
        if message == "not authorised":
            return redirect("/notauthorised/")
        elif message == "not logged in":
            return redirect("/notlogin/")

def addproduct_view(request):
    ptype = ProductType.objects.all()
    pcategory = ProductCategory.objects.all()
    pbrand = ProductBrand.objects.all()
    psubcategory = ProductSubCategory.objects.all()
    dictionary = {'dict_ptype': ptype, 'dict_pcategory': pcategory, 'dict_brand': pbrand, 'dict_subcategory': psubcategory}
    #if request.method =="POST":


    return render(request, "addproduct.html",dictionary)
