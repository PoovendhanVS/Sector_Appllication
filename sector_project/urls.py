"""
URL configuration for sector_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sectorapp.urls')),
    path('logout',include('sectorapp.urls')),
    path('signin/',include('sectorapp.urls')),

    path('admin_board/',include('sectorapp.urls')),
    path('admin_usage/',include('sectorapp.urls')),

    path('user/',include('sectorapp.urls')),
    path('users_list/',include('sectorapp.urls')),
    path('update_user_page/<int:id>/',include('sectorapp.urls')),
    path('del_user_list/<int:id>/',include('sectorapp.urls')),

    path('master/',include('sectorapp.urls')),
    path('master_header_link/',include('sectorapp.urls')),
    path('emp_official/',include('sectorapp.urls')),
    path('update_emp_official/<int:id>',include('sectorapp.urls')),
    path('emp_personal',include('sectorapp.urls')),
    path('add_emp_personal',include('sectorapp.urls')),
    path('view_emp_dte',include('sectorapp.urls')),

    path('type_create',include('sectorapp.urls')),
    path('create_type_dte',include('sectorapp.urls')),
    path('update_type_dte/<int:id>',include('sectorapp.urls')),
    path('del_type_dte/<int:id>/',include('sectorapp.urls')),
    path('view_type_dte/<int:id>/',include('sectorapp.urls')),

    path('billing',include('sectorapp.urls')),
    path('update_sales_dte/',include('sectorapp.urls')),
    path('update_dte/',include('sectorapp.urls')),
    path('del_sales_dte/<int:id>/',include('sectorapp.urls')),

    # path('nxt_billing',include('sectorapp.urls')),
    # path('my_form_view',include('sectorapp.urls')),

    path('get_item_details/',include('sectorapp.urls')),
    
    path('sales_home',include('sectorapp.urls')),
    path('update_sales_page/<int:id>/',include('sectorapp.urls')),
    path('get_item_table/',include('sectorapp.urls')),
    path('update_item_dte/',include('sectorapp.urls')),
    path('edit_item_dte/',include('sectorapp.urls')),
    path('del_sales_page/<str:id>/',include('sectorapp.urls')),
    path('del_list_item/<int:id>/',include('sectorapp.urls')),

    # Session Permission Timeout Page Practice
    path('setsession',include('sectorapp.urls')),
    path('getsession',include('sectorapp.urls')),
    path('delsession',include('sectorapp.urls')),

    path('fileconvert/',include('sectorapp.urls')),

    # Dependent Dropdown List Practies
    # path('select2DDL',include('sectorapp.urls')),
    # path('dropdownlist/',include('sectorapp.urls')),
    # path('dropdownlistnext/',include('sectorapp.urls')),
    
]
