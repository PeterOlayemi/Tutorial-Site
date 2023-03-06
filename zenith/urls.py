from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='zenith'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('signup/', views.signup, name ='signup'),
    path('signin/', auth_views.LoginView.as_view(), name='login'),
    path('signout/', views.signout, name = 'logout'),
    path('studentregister/', views.studentregister, name='studentregister'),
    path('image_upload/', views.hotel_image_view, name = 'image_upload'),
    path('viewprofile/', views.viewprofile, name='studentprofile'),
    path('editprofile/<int:_id>/',views.editprofile, name='editprofile'),
    path('editdp/<int:_id>/',views.editdp, name='editdp'),
    path('message/',views.message, name='message'),
    path('payments/',views.payment, name='paymenthome'),
    path('paymentfile/',views.paymentfile, name='paymentfile'),
    path('paymentdetail/',views.paymentdetail, name='paymentdetail')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
