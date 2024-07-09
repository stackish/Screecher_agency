from django.shortcuts import render,reverse
#new imports
from django.http import HttpResponseRedirect #Redirect the page after the submit 
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from App.models import Registered_email,Support,Message,Notepad,Vacancies,Countdown,Waiting
from django.contrib.auth.decorators import login_required   #Login required to access private pages
from django.views.decorators.cache import cache_control #Destroy the Session after logout
from django.core.files.storage import FileSystemStorage
 


 # =========================== FRONTEND SECTION ==============================

# Create your views here.
def home(request):
    template_name="App/home.html"
   
    return render(request,template_name)

# function to render opportunities page
def opportunities(request):
    myJob = Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    template_name="App/opportunities.html"
    context ={"vacancies":myJob,"countdowns":myCountdown}
   
    return render(request,template_name,context)


#fuunction to render support page

def support(request):
    if request.method == "POST":
        
        #check if email exists
        email = request.POST['email']

        if Support.objects.filter(email= email).exists():
            messages.info(request,".")#argument inside the message cannot be empty
            return HttpResponseRedirect(reverse('support'))

        else:
            support = Support()
            message = request.POST['message']
            terms = request.POST['terms']
            person = request.POST['person']
            option = request.POST['option']
            email = request.POST['email']

            support.message = message
            support.terms = terms
            support.person = person
            support.option = option
            support.email = email
            support.save()
            messages.success(request,"We will review your request !")
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect(reverse('backend'))

    else:
        template_name ="App/support.html"
        return render(request,template_name)
            

#MESSAGE

def add_message(request):
    if request.method == 'POST':
        if request.POST.get('message'):
            message = Message()
            message.text = request.POST.get('message')
            message.save()
            messages.success(request,"Message sent successfully !")
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'App/home.html')

#FAQ page

def faq(request):
    template_name ="App/faq.html"
    return render(request,template_name)

#Waiting List

def waiting(request):
    if request.method ==  'POST':
    # check if email exist in the database
        email = request.POST['email']

        if Waiting.objects.filter(email = email).exists():
            messages.warning(request,".")
            return HttpResponseRedirect(reverse('waiting'))
            
        else:
            
            file = request.FILES['profile']
            attach= FileSystemStorage()
            profile_doc = attach.save(file.name ,file)
            waiting = Waiting(
            job = request.POST.get('job'),
            email = request.POST.get('email'),
            message = request.POST.get('message'),
            profile_document = profile_doc
            )
            waiting.save()

            messages.success(request,"Successfully registered")
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,"App/waiting_list.html")


    


    
# =============================== RESUMES ========================= 

 # a) Function to send frontend form
def send_email_frontend(request):
    if request.method == 'POST':

        #Check if email exists in database

        email = request.POST['email']
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request,"We already have your resume in our DB")
            return HttpResponseRedirect(reverse("opportunities"))
        
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            #Register inside DB
            contact = Registered_email()
            contact.email=email
            contact.save()

           
        
            template = loader.get_template('resume_form.txt')
            context ={

            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'address':address,
            'experience':experience,
            'skills':skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
           "Frontend - Candidiate",message,
           "Frontend Opportunity",
           ["iifeanyi570@gmail.com"] 
            )
            email.content_subtype='html'
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            
            messages.success(request,"Frontend resume sent successfully !")
            return HttpResponseRedirect('/')


 #  b) Function to send backend form
def send_email_backend(request):
    if request.method == 'POST':

        #Check if email exists in database

        email = request.POST['email']
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request,"We already have your resume in our DB")
            return HttpResponseRedirect(reverse("opportunities"))
        
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            #Register inside DB
            contact = Registered_email()
            contact.email=email
            contact.save()


           
        
            template = loader.get_template('resume_form.txt')
            context ={

            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'address':address,
            'experience':experience,
            'skills':skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
           "Backend - Candidiate",message,
           "Backend Opportunity",
           ["iifeanyi570@gmail.com"] 
            )
            email.content_subtype='html'
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
           
            messages.success(request,"Backend resume sent successfully !")
            return HttpResponseRedirect('/')

 #  c) Function to send fullstack form

def send_email_fullstack(request):
    if request.method == 'POST':

        #Check if email exists in database

        email = request.POST['email']
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request,"We already have your resume in our DB")
            return HttpResponseRedirect(reverse("opportunities"))
        
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            #Register inside DB
            contact = Registered_email()
            contact.email=email
            contact.save()

           
        
            template = loader.get_template('resume_form.txt')
            context ={

            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'address':address,
            'experience':experience,
            'skills':skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
           "Fullstack - Candidiate",message,
           "Fullstack Opportunity",
           ["iifeanyi570@gmail.com"] 
            )
            email.content_subtype='html'
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            
            messages.success(request,"Fullstack resume sent successfully !")
            return HttpResponseRedirect('/')

#  d) Function to send intern form

def send_email_intern(request):
    if request.method == 'POST':

        #Check if email exists in database

        email = request.POST['email']
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request,"We already have your resume in our DB")
            return HttpResponseRedirect(reverse("opportunities"))
        
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')
            #Register inside DB
            contact = Registered_email()
            contact.email=email
            contact.save()

           
        
            template = loader.get_template('resume_form.txt')
            context ={

            'name':name,
            'age':age,
            'email':email,
            'phone':phone,
            'address':address,
            'experience':experience,
            'skills':skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
           "Intern - Candidiate",message,
           "Intern Opportunity",
           ["iifeanyi570@gmail.com"] 
            )
            email.content_subtype='html'
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            
            messages.success(request,"Intern resume sent successfully !")
            return HttpResponseRedirect('/')















 # =========================== BACKEND SECTION ==============================
from django.http import HttpResponse
#Backend homepage

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def backend(request):
    total = Registered_email.objects.all().count()
    myNote = Notepad.objects.all()
    myJob =  Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    
    template_name="App/backend.html"
    context = {"count":total, 'notepads':myNote,"vacancies":myJob,"countdowns":myCountdown}
    return render(request,template_name,context)




#edit notepad
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_notepad(request):
    if request.method == "POST":
        notepad = Notepad.objects.get(id = request.POST.get('id'))
        if notepad != None:
            notepad.title = request.POST.get('title')
            notepad.text = request.POST.get('text')
            notepad.save()
            
            messages.success(request,"Notepad updated successfully !")
            return HttpResponseRedirect(reverse('backend'))



#Vacancies
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_vacancies(request):
    if request.method == "POST":
        vacancy = Vacancies.objects.get(id = request.POST.get('id'))
        if vacancy != None:
            vacancy.frontend = request.POST.get('frontend')
            vacancy.backend = request.POST.get('backend')
            vacancy.fullstack = request.POST.get('fullstack')
            vacancy.intern = request.POST.get('intern')
            vacancy.save()
            messages.success(request,"Job Vacancies updated")
            return HttpResponseRedirect(reverse('backend'))




#COUNTDOWN
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_countdown(request):
    if request.method == "POST":
        countdown =   Countdown.objects.get(id =request.POST.get('id'))
        if countdown != None:
            countdown.timer = request.POST.get('timer')
            countdown.save()
            messages.success(request,"Countdown updated successfully !")
            return HttpResponseRedirect(reverse('backend'))





