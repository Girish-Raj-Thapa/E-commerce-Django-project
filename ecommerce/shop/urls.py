from django.urls import path, include 
from rest_framework.routers import DefaultRouter 

from . views import CategoriesView, ProductView 

# API 
router = DefaultRouter()
router.register(r'category', CategoriesView)
router.register(r'prodcut', ProductView)

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Page View
frontend_urlpatterns = [

]


# Combined urls patterns
urlpatterns = [
    path('', include(frontend_urlpatterns)),

    # API URLs
    path('', include(api_urlpatterns)),
]