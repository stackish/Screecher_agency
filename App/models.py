from django.db import models

# Create your models here.
# Prevent duplicate emails

#! PREVENTS DUPLICATED EMAILS
class Registered_email(models.Model):
    email = models.CharField(max_length=200)
    

    def __str__(self):
        return self.email



#2) SUPPORT

class Support(models.Model):

    PERSON ={
        ('Employee', 'Employee'),
        ('Candidate', 'Candidate'),
    }

    OPTIONS = {
        ('l lost my account','l lost my account'),        
        ('My password does not work','My password does not work'),        
        ('Update resume','Update resume'),        
        ('Others','Others'),        
    }


    SITUATION = {
        ('Done','Done'),
        ('pending','pending'),
    }


    terms = models.BooleanField("take responsibility",default=False)
    message = models.TextField()
    person = models.CharField(choices=PERSON,max_length=50)
    option = models.CharField(choices=OPTIONS,max_length=50)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50,null=True,default="Pending",choices=SITUATION)


    def __str__(self):
        return self.person


#(3) MESSAGE

class Message(models.Model):
    
    SITUATION = {
        ('Read','Read'),
        ('Unread','Unread'),
    }
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50,null=True,default="Unread",choices=SITUATION)



#4) NOTEPAD

class Notepad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()

    def __str__(self):
        return self.title



#5) VACANCIES

class Vacancies(models.Model):
    id = models.IntegerField(primary_key=True)
    frontend = models.CharField(max_length=100)
    backend = models.CharField(max_length=100)
    fullstack = models.CharField(max_length=100)
    intern = models.CharField(max_length=100)

    def __str__(self):
        return self.frontend



#6)  COUNTDOWN
class Countdown(models.Model):
    id = models.IntegerField(primary_key=True)
    timer = models.CharField(max_length=100)



#7) WAITING LIST
JOB = (
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('Fullstack','Fullstack'),
    ('Intern','Intern'),
)

SITUATION = {
    ('Read','Read'),
    ('Unread','Unread'),
    }

class Waiting(models.Model):
    job = models.CharField(choices=JOB,max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    Situation = models.CharField(max_length=50,null=True,default="Unread",choices=SITUATION)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_document = models.FileField()
    company_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job
