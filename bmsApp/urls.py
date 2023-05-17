from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientViewset

router = DefaultRouter()
router.register('client', ClientViewset, basename='client')
# urlpatterns = [
#     path('home/', feed_data)
# ]

# urlpatterns += router.urls
urlpatterns = router.urls