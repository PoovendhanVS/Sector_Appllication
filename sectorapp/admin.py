from django.contrib import admin
from .models import ProductsModel,ItemModel, Country, State, District, AccessoriesModel, addCountryModel, addDistrictModel, addStateModel

# Register your models here.
admin.site.register(ProductsModel)
admin.site.register(ItemModel)
admin.site.register(Country) 
admin.site.register(State)
admin.site.register(District)
admin.site.register(AccessoriesModel)
admin.site.register(addCountryModel)
admin.site.register(addStateModel)
admin.site.register(addDistrictModel)
