from django.db import models

class Sk_home(models.Model):
    Sk_Image = models.ImageField(upload_to='all_image/')
    Image_Name=models.CharField(max_length=50)
    
    


    def __str__(self):
        return self.Image_Name


class Sk_about(models.Model):
    Full_Name= models.CharField(max_length=50)
    Phone_Number=models.IntegerField()
    Email_Number=models.EmailField()
    Fb_Urls=models.URLField()
    Link_Urls=models.URLField()
    
    
    
    def __str__(self):
        return self.Full_Name
    
class Sk_cv(models.Model):
    Sk_cv = models.FileField(upload_to='all_image/')
    cv_Name=models.CharField(max_length=50)
    
    


    def __str__(self):
        return self.cv_Name

class Sk_certificate(models.Model):
    
    Exam_Name=models.CharField(max_length=50)
    Roll_Number=models.IntegerField()
    Bord_Name=models.CharField(max_length=50)
    Result=models.FloatField()
    Certificate_Image = models.ImageField(upload_to='all_image/')
    
    


    def __str__(self):
        return self.Exam_Name
class Sk_online_course(models.Model):
    
    Course_Name=models.CharField(max_length=50)
    Institute_Name=models.CharField(max_length=50)
    Result=models.CharField(max_length=40,null="")
    Course_Image = models.ImageField(upload_to='all_image/')
    
    


    def __str__(self):
        return self.Course_Name

class Interest_Cata(models.Model):
    Interest_Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Interest_Name


class Sk_Interest(models.Model):
    Interset_catagary=models.ForeignKey(Interest_Cata, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Date=models.DateTimeField('date published')
    Img1_url=models.CharField(max_length=10000, blank=True)
    Img_url=models.CharField(max_length=10000, blank=True)
    vid_url=models.CharField(max_length=10000, blank=True)
    
    def __str__(self):
        return self.Name

class Project_Cata(models.Model):
    Project_catagory_name=models.CharField(max_length=50)

    def __str__(self):
        return self.Project_catagory_name
class Project(models.Model):
    Project_catagary=models.ForeignKey(Project_Cata, on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Language=models.CharField(max_length=100, blank=False)
    Img1_url=models.CharField(max_length=10000, blank=True)
    vid_url=models.CharField(max_length=10000, blank=True)
    File_url=models.CharField(max_length=10000, blank=True)
    web_url=models.CharField(max_length=10000, blank=True)
    Description=models.TextField()
    
    def __str__(self):
        return self.Name

def get_dataFrom_Sk_about():
        details=Sk_about.objects.all()
        
        return list(details)