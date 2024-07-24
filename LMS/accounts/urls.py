from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns=[
    # path('',views.index)
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html") , name="logout" ),
]
urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)