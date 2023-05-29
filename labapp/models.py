from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.

class Patient(models.Model):
    
    pname=models.CharField(max_length=100)
    number=models.CharField(max_length=15)
    email=models.CharField(max_length=100)
    pdesc=models.CharField(max_length=150)
    dname=models.CharField(max_length=100)    
    is_deleted=models.CharField(max_length=5)
    pid=models.IntegerField()
    
    

class Testname(models.Model):
    test_name = models.CharField(max_length=100)
    tid=models.IntegerField()
    price=models.IntegerField()
  
class Tests(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    test=models.ForeignKey(Testname,on_delete=models.CASCADE)
    
class Bill(models.Model):
    #bpname=models.ForeignKey(Patient,on_delete=models.CASCADE)
    number=models.CharField(max_length=15)
    dname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    test=models.ForeignKey(Tests,on_delete=models.CASCADE)  
    pname=models.CharField(max_length=100)
    test_name=models.CharField(max_length=15)   
    pid=models.IntegerField()
    tid=models.IntegerField()
    price=models.IntegerField()
    barcode=models.ImageField(upload_to='images/',blank=True,null=True)

    def save(self,*args, **kwargs):
        CODE_39=barcode.get_barcode_class('code39')
        code = CODE_39(f'{self.pname}{self.pid}{self.test_name}',writer=ImageWriter())
        buffer = BytesIO()      
        code.write(buffer)
        self.barcode.save('barcode.jpg', File(buffer),save=False)
        return super().save(*args,**kwargs)
    


    

