



from django.urls import path

from api import views



urlpatterns = [
    path('token/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),

]

