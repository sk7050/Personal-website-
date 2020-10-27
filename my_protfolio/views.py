from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from my_protfolio.functions.functions import Upload_File
from .models import Sk_home,Sk_about,get_dataFrom_Sk_about,Sk_cv,Sk_certificate,Sk_online_course,Sk_Interest,Interest_Cata,Project_Cata,Project
from .forms import skfile
from .forms import EmailPostForm


def home_view(request):
    Items=Sk_home.objects.all()
    Items=list(Items)
    Personal_project=Project.objects.order_by('Name')
    details=get_dataFrom_Sk_about()
    Home_page="Its my Home Page"
    cotext={
        'Home_page':Home_page,
        'Home_item':Items,
        'Personal_project': Personal_project,
        'details':details,
        }
    
    return render(request, 'home.html',cotext)


def about_view(request):
    def about_content(form,alert="0"):
        details=get_dataFrom_Sk_about()
        myself='''
            I am Shaikh Abu Faisal, I have done B.sc in EEE .Now I am working as an Asst.Systems Engineer(Computer Hardware System).
            But I have lot of interest aboout computer programing .I know Java ,Python, Django,basic css,basic html,basic bootstrap. Now I am trying to learn machine learning.
            I am a huge fan of,the concept of machine learning.
            Personaly I am working with python base web apps devlopment.
            '''
        context={
            'myself':myself,
            'details':details,
            'Form':form,
            'alert':alert
               }
        return context
    
    if request.method == 'GET':
        form=EmailPostForm()
        contex=about_content(form,alert="0")
        return render(request, 'about.html',contex)
        
    else:
        form =EmailPostForm(request.POST)
        
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            try:
                send_mail(email,message,name, ['sk.faysal08@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            contex=about_content(form=EmailPostForm(),alert="1")
            return render(request, 'about.html',contex)
            
   
    
    
    

def creat_view(request):
    '''if request.method=="POST":
        image=skimage(request.POST,request.FILES)
        if image.is_valid():
            Upload_File(request.FILES['Sk_Image'])
            return HttpResponse("File uploaded successfuly")  
    else:
        image=skimage()
    contex={
        'my_image':image
            } '''
    return render(request,'creat.html')

def upload_view(request):
    print(request.FILES,request.POST)
    image=request.FILES['Sk_Image']
    name=request.POST['Image_Name']
    upload=Sk_home(Sk_Image=image,Image_Name=name)
    upload.save()
    return render(request,'creat.html') 

def cv_view(request):
    cv=Sk_cv.objects.all()
    context={
        'my_cv':cv
    }
    
    return render(request,'cv.html',context)     
         
   
def certificate_view(request):
    certificates=Sk_certificate.objects.all()
    Online_Course=Sk_online_course.objects.all()
    print(certificates)
    context={
         'certificates': certificates,
         'Online_Course': Online_Course
    }
    return render(request,'Certificate.html',context)       
    
def cerdetails_view(request,pk):
    certificates=Sk_certificate.objects.get(pk=pk)
    print(certificates)
    context={
         'certificates': certificates
         }
    return render(request,'cerdetails.html',context)    

def Coursedetails_view(request,pk):
    certificates=Sk_online_course.objects.get(pk=pk)
    print(certificates)
    context={
         'certificates': certificates
         }
    return render(request,'Coursedetails.html',context)        
    
def Personal_interest_view(request):
    Personal_interest=Sk_Interest.objects.order_by('Name')
    Intersest_cat=Interest_Cata.objects.all()
    hobbies='''
        Interests change from person to person. There are numerous Interests such as reading,
        taking pictures, Youtube video making, travelling,codding ,learning new technologies, gardening,
        pet care, knitting, catering, stamp collecting, etc. 
        My list of interests includes travelling,Youtube video making,codding,learning new technologies.'''

    print(Personal_interest)
    context={
        'hobbies': hobbies,
        'interests':Intersest_cat,
         'Personal_interest': Personal_interest
         }
    return render(request,'Personal_interest.html',context)


def Personal_interest(request,pk):
    Intersest_cat=Interest_Cata.objects.filter(pk=pk)
    print(Intersest_cat )
    Personal_interest=Sk_Interest.objects.filter(Interset_catagary_id=pk)
    context={
            'interests':Intersest_cat,
            'Personal_interest': Personal_interest
             }
    return render(request,'Personal_interest.html',context)             
    
        #instance=image.save(commit=False)
      #instance.save()
      #Sk_home.objects.create(Sk_Image=request.POST.get('Sk_Image'),Image_Name=request.POST.get('Image_Name'))
def Personal_project_view(request,id=""):
    if len(id)>0:
        Personal_project=Project.objects.filter(id=id)
        for i in Personal_project:
            D=i.Project_catagary_id
            print(i,D)
            
        project_cat=Project_Cata.objects.filter(id=D)
    
        context={
        
        'project_cat':project_cat,
        'Personal_project': Personal_project
         }
        return render(request,'project_details.html',context)

    else:
        Personal_project=Project.objects.order_by('Name')
        project_cat=Project_Cata.objects.all()
    
        context={
        
        'project_cat':project_cat,
        'Personal_project': Personal_project
         }
        return render(request,'Personal_project.html',context)

def Personal_project(request,pk="",Name=""):
    if len(pk)>0:
        project_cat=Project_Cata.objects.filter(pk=pk)
        Personal_project=Project.objects.filter(Project_catagary_id=pk)
    
    
        context={
        
        'project_cat':project_cat,
        'Personal_project': Personal_project
         }
        return render(request,'Personal_project.html',context)
    


    

