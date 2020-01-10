from .views import LinkCreate, LinkShow, RedirectToLongURL
from django.urls import path, include

urlpatterns = [
    path('', LinkCreate.as_view(), name='home'),
    path('link/(<pk>)', LinkShow.as_view(), name='link_show'),
    path('<short_url>/', RedirectToLongURL.as_view(),
              name='redirect_short_url'),
]