from django import forms
from manager.models import roletable, UserInfoTable,ProductBrand,\
    ProductCategory,ProductSubCategory,ProductType,ProductDetails,\
    ProductSize,ProductStock


class roletableForm(forms.ModelForm):
    class Meta():
        model = roletable
        exclude = ["roleid", "rolename"]


class UserInfoTableForm(forms.ModelForm):
    class Meta():
        model = UserInfoTable

        exclude = ["tbuserroleid", "tbuseremail", "tbusername", "tbuserpassword", "tbusermob",
                  "tbuseraltmob", "tbuserimage", "tbuserpan", "tbuserpanimage", "tbuseradhar",
                   "tbuseradharimage", "tbisactive", "tbuseraddress", "tbuserpincode", "tbotp",
                   "tbotptime", "tbisverified", "tbauthtoken"]


class ProductTypeForm(forms.ModelForm):
    class Meta():
        model = ProductType
        exclude = ["tbproducttypeid", "tbproducttypename", "type_is_active"]

class ProductCategoryForm(forms.ModelForm):
    class Meta():
        model = ProductCategory
        exclude = ["tbcategoryid", "tbcategorytype", "category_is_active"]

class ProductBrandForm(forms.ModelForm):
    class Meta():
        model = ProductBrand
        exclude = ["tbbrandid", "tbbrandname", "brand_is_active"]


class ProductSizeForm(forms.ModelForm):
    class Meta():
        model = ProductSize
        exclude = ["tbproductsizeid", "tbproductsize", "tbcategoryid", "size_is_active"]

class ProductSubCategoryForm(forms.ModelForm):
    class Meta():
        model = ProductSubCategory
        exclude = ["tbsubcategoryid","tbsubcategoryname","fkcategoryid"]



class ProductDetailsForm(forms.ModelForm):
    class Meta():
        model = ProductDetails
        exclude = ["tbproductid","fkproducttypeid","fkproductcategoryid",
                   "fkproductbrandid","fksubcategoryid","tbproductname",\
    "tbproductprice",\
    "tbproductdescription","tbproductimage1","tbproductimage2",\
    "tbproductimage3",\
    "tbproductimage4","tbproductimage5","tbproductimage6","tbproductimage7",
                   "tbproductquantity","publishdate",\
    "product_is_active","tbuseremail"]


class ProductStockForm(forms.ModelForm):
    class Meta():
        model = ProductStock
        exclude = ["tbproductstockid","fkproductid","fkproductsizeid","tbproductquantity",
                   "stock_is_active"]
