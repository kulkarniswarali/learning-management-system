from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('courses',views.courses, name='courses'),
    path('trainers',views.trainers, name='trainers'),
    path('course-details/<int:pk>/',views.courseDetails, name='courseDetails'),
    path('my-courses',views.mycourses, name='mycourses'),
    path('course-attempt/<int:pk>/',views.courseAttempt, name='courseAttempt'),
    path('checkout', views.checkout, name="checkout"),

    path('admin-panel', views.adminPanel, name="adminPanel"),
    path('users', views.users, name="users"),
    path('edit-users/<int:pk>', views.editusers, name="editusers"),
    path('courseMgmt', views.courseMgmt, name="courseMgmt"),
    path('subscribe/<int:pk>', views.subscribe, name="subscribe"),
]
urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)