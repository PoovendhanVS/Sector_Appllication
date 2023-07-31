from django.urls import include, path
from sectorapp import views
from django.urls import path
from .views import generator

urlpatterns = [
    path('',views.signin,name='signin'),

    path('logout',views.logout,name='logout'),

    path('signup',views.home,name='signup'),

    path('admin_board',views.admin_board,name='admin_board'),

    path('admin_usage',views.admin_usage,name='admin_usage'),

    path('user',views.user,name='user'),

    path('users_list',views.users_list,name='users_list'),

    path('update_user_page/<int:id>/',views.update_user_page,name='update_user_page'),

    path('del_user_list/<int:id>/',views.del_user_list,name='del_user_list'),

    path('master',views.master,name='master'),

    path('master_header_link',views.master_header_link,name='master_header_link'),

    path('emp_official',views.emp_official,name='emp_official'),

    path('update_emp_official/<int:id>',views.update_emp_official,name='update_emp_official'),

    # path('emp_personal',views.emp_personal,name='emp_personal'),

    path('add_emp_personal',views.add_emp_personal,name='add_emp_personal'),

    path('del_emp_dte/<int:id>/',views.del_emp_dte,name='del_emp_dte'),

    path('view_emp_dte/<int:id>/',views.view_emp_dte,name='view_emp_dte'),

    path('type_create',views.type_create,name='type_create'),

    path('create_type_dte', views.create_type_dte,name='create_type_dte'),

    path('update_type_dte/<int:id>', views.update_type_dte,name='update_type_dte'),

    path('del_type_dte/<int:id>/',views.del_type_dte,name='del_type_dte'),

    path('view_type_dte/<int:id>/',views.view_type_dte,name='view_type_dte'),

    path('billing',views.billing,name='billing'),

    path('update_sales_dte/',views.update_sales_dte,name='update_sales_dte'),

    path('update_dte/',views.update_dte,name='update_dte'),

    path('del_sales_dte/<int:id>/',views.del_sales_dte,name='del_sales_dte'),

    path('fetch_data/', views.fetch_data, name='fetch_data'),

    path('fetch_type_data/', views.fetch_type_data, name='fetch_type_data'),

    # path('nxt_billing', views.nxt_billing, name='nxt_billing'),

    # path('my_form_view', views.my_form_view, name='my_form_view'),

    path('get_item_details/', views.get_item_details, name='get_item_details'),

    path('sales_home', views.sales_home, name='sales_home'),

    path('update_sales_page/<int:id>/', views.update_sales_page, name='update_sales_page'),

    path('get_item_table/', views.get_item_table, name='get_item_table'),

    path('update_item_dte/', views.update_item_dte, name='update_item_dte'),

    path('edit_item_dte/', views.edit_item_dte, name='edit_item_dte'),

    path('del_sales_page/<str:id>/', views.del_sales_page, name='del_sales_page'),
    
    path('del_list_item/<int:id>/', views.del_list_item, name='del_list_item'),

    path('setsession', views.setsession, name='setsession'),

    path('getsession', views.getsession, name='getsession'),
    
    path('delsession', views.delsession, name='delsession'),

    path('fileconvert/', views.fileconvert, name='fileconvert'),

    # path('select2DDL', views.select2DDL, name='select2DDL'),

    # path('dropdownlist/', views.dropdownlist, name='dropdownlist'),

    # path('dropdownlistnext/', views.dropdownlistnext, name='dropdownlistnext'),

    path('generator/', generator.as_view(), name='generator'),

]