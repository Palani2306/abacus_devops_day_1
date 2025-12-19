
# from django.urls import path
# from . import views
# from .views import SimplePostView,UserAPI 
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SimplePostView, UserAPI, StudentViewSet



router = DefaultRouter()
router.register(r'students', StudentViewSet)

 

urlpatterns=[
path('hello/',views.hello),
path('bye/',views.bye),
path('echo/',views.echo),
path('update/', views.update_echo),     # PUT
path('delete/', views.delete_echo),     # DELETE
path('cbv-view/',views.SimplePostView.as_view()),
path('drf-post/',views.UserAPI.as_view()),
path('', include(router.urls)),
path('simple-page/',views.simple_page),
path('newstudent/', views.student_apis),
path("login/", views.login_page),
path("home/", views.home),
path("api-login/",views.ProfileAPI.as_view()),
path("jwt/login/", TokenObtainPairView.as_view()),
path("jwt/refresh/", TokenRefreshView.as_view()),

# inbuilt authentication api
path("api-token-auth/", obtain_auth_token)   


]