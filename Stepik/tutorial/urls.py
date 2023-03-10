"""Stepik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, register_converter
from tutorial import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('<yyyy:variable>', views.numeric_func),
    path('table/<slug:name>', views.get_row, name='get_link'),
    path('form', views.FeedBackView.as_view(), name='get_form'),
    path('form/<int:id_form>', views.FeedBackView.post, name='update_form'),
    path('<variable>', views.page, name='main-link'),
]
