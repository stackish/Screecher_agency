from django.contrib import admin
from App.models import Registered_email,Support,Message,Notepad,Vacancies,Countdown,Waiting
from django.utils.html import format_html
# Register your models here.

#1) PREVENT DUPLICATED EMAILS

class Registered_emailAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_per_page = 10

admin.site.register(Registered_email,Registered_emailAdmin)



#2) TECHNICAL SUPPORT

class SupportAdmin(admin.ModelAdmin):
    list_filter = ['Situation','person']
    list_display = ['email','person','option', 'created_at','status','_']
    search_fields =['person','option']
    list_per_page = 10


    #Function to change the icons (Done -- Pending)

    def _(self,obj):
        if obj.Situation == 'Done':
            return True
        else:
            return False

    _.boolean = True

    #function to color the the text (Done -- Pending)
    def status(self,obj):
        if obj.Situation == 'Done':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Situation))

    status.allow_tags = True


admin.site.register(Support,SupportAdmin)


#3)  MESSAGE
class MessageAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = ['id','created_at','status','_']
    list_per_page = 10


     #Function to change the icons (READ -- Pending)

    def _(self,obj):
        if obj.Situation == 'Read':
            return True
        else:
            return False

    _.boolean = True



     #function to color the the text (READ -- Pending)
    def status(self,obj):
        if obj.Situation == 'Read':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Situation))

    status.allow_tags = True

admin.site.register(Message,MessageAdmin)




#Notepad

class NotepadAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Notepad,NotepadAdmin)



# Job Vacancies 

class VacanciesAdmin(admin.ModelAdmin):
    list_display =['frontend','backend','fullstack','intern']
admin.site.register(Vacancies,VacanciesAdmin)


#COUNTDOWN

class CountdownAdmin(admin.ModelAdmin):
    list_display = ['timer']


admin.site.register(Countdown,CountdownAdmin)



# Waiting list

class WaitingAdmin(admin.ModelAdmin):
    list_filter = ['Situation','job']
    search_fields = ['email']
    list_display = ['job','email','created_at','status','_']
    list_per_page = 10


     #Function to change the icons (READ -- Pending)

    def _(self,obj):
        if obj.Situation == 'Read':
            return True
        else:
            return False

    _.boolean = True



     #function to color the the text (READ -- Pending)
    def status(self,obj):
        if obj.Situation == 'Read':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Situation))

    status.allow_tags = True

admin.site.register(Waiting, WaitingAdmin)