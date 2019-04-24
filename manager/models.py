from django.db import models

# Create your models here.
class roletable(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=255, unique=True, default="")

class UserInfoTable(models.Model):
    tbuserroleid=models.ForeignKey(roletable, on_delete=models.CASCADE)
    tbuseremail= models.CharField(max_length=255, primary_key=True)
    tbusername = models.CharField(max_length=255)
    tbuserpassword = models.CharField(max_length=255)
    tbusermob = models.CharField(max_length=255)
    tbuseraltmob = models.CharField(max_length=255)
    tbuserimage = models.CharField(max_length=255)
    tbuserpan = models.CharField(max_length=255, null=True)
    tbuserpanimage = models.CharField(max_length=255, null=True)
    tbuseradhar =models.CharField(max_length=255, null=True)
    tbuseradharimage = models.CharField(max_length=255, null=True)
    tbisactive =models.BooleanField(default=True)
    tbuseraddress = models.CharField(max_length=255)
    tbuserpincode = models.IntegerField()
    tbotp = models.CharField(max_length=255,default="",null=True)
    tbotptime = models.CharField(max_length=255, default="", null=True)
    tbisverified = models.BooleanField(default=False)
    tbauthtoken = models.CharField(max_length=255,null=True)



class ProductType(models.Model):
    tbproducttypeid = models.AutoField(primary_key=True)
    tbproducttypename = models.CharField(max_length=255, unique=True)
    type_is_active = models.BooleanField(default=True)

class ProductCategory(models.Model):
    tbcategoryid = models.AutoField(primary_key=True)
    tbcategorytype = models.CharField(max_length=255, unique=True)
    category_is_active = models.BooleanField(default=True)


class ProductBrand(models.Model):
    tbbrandid = models.AutoField(primary_key=True)
    tbbrandname = models.CharField(max_length=255, unique=True)
    brand_is_active = models.BooleanField(default=True)

class ProductSize(models.Model):
    tbproductsizeid = models.AutoField(primary_key=True)
    tbproductsize = models.CharField(max_length=255)
    tbcategoryid = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,default="")
    size_is_active = models.BooleanField(default=True)

class ProductSubCategory(models.Model):
    tbsubcategoryid = models.AutoField(primary_key=True)
    tbsubcategoryname = models.CharField(max_length=255, unique=True)
    #fksizeid = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    fkcategoryid = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class ProductDetails(models.Model):
    tbproductid = models.AutoField(primary_key=True)
    fkproducttypeid = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    fkproductcategoryid = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,default="")
    fkproductbrandid = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    #fkproductsizeid = models.ForeignKey(ProductSize, on_delete=models.CASCADE,default="")
    fksubcategoryid = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE,default="")
    tbuseremail = models.ForeignKey(UserInfoTable, on_delete=models.CASCADE)
    tbproductname = models.CharField(max_length=255)
    tbproductprice = models.IntegerField()
    tbproductquantity = models.IntegerField()
    tbproductdescription = models.CharField(max_length=255)
    tbproductimage1 = models.CharField(max_length=255)
    tbproductimage2 = models.CharField(max_length=255, null=True)
    tbproductimage3 = models.CharField(max_length=255, null=True)
    tbproductimage4 = models.CharField(max_length=255, null=True)
    tbproductimage5 = models.CharField(max_length=255, null=True)
    tbproductimage6 = models.CharField(max_length=255, null=True)
    tbproductimage7 = models.CharField(max_length=255, null=True)
    publishdate = models.CharField(max_length=255)
    product_is_active = models.BooleanField(default=True)


class ProductStock(models.Model):
    tbproductstockid = models.AutoField(primary_key=True)
    fkproductid = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
    fkproductsizeid = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    tbproductquantity = models.IntegerField()
    stock_is_active = models.BooleanField(default=True)

