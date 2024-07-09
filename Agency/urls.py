from django.contrib import admin
from django.urls import path,include
from App import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path to access django admin
    path('admin/', admin.site.urls),
    # =========================== FRONTEND SECTION ==============================
    # path to render homepage
    path('',views.home,name="home"),
    #path to render opportunities page
    path('opportunities',views.opportunities, name="opportunities"),
#Path to Login/Logout

    path('',include('django.contrib.auth.urls')),
    #path('logout',include('django.contrib.auth.urls')),
#path to support 

path('support/',views.support,name="support"),

#path to support 

path('add_message/',views.add_message,name="add_message"),

#path to FAQ page
path('faq/',views.faq,name="faq"),

#path to Waiting list 
path('waiting/',views.waiting,name="waiting"),

# =========================== SEND EMAIL ==============================
    # Path to send frontend form
    path('send_email_frontend',views.send_email_frontend,name="email_frontend"),

    # Path to send backend form
    path('send_email_backend',views.send_email_backend,name="email_backend"),

    # Path to send fullstack form
    path('send_email_fullstack',views.send_email_fullstack,name="email_fullstack"),

    # Path to send intern form
    path('send_email_intern',views.send_email_intern,name="email_intern"),


     # =========================== BACKEND SECTION ==============================
    #path to backend homepage
     path('backend/',views.backend,name="backend"),
     #path to notepad
     path('edit_notepad',views.edit_notepad,name="edit_notepad"),
     #path to vacancies
     path('edit_vacancies',views.edit_vacancies,name="edit_vacancies"),
     #path to countdown
     path('edit_countdown',views.edit_countdown,name="edit_countdown"),

]
if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
