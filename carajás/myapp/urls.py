from rest_framework.routers import DefaultRouter
from .views import CategoryList,ProductsList,SubProductsList

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'Category', CategoryList)
router.register(r'Products', ProductsList)
router.register(r'SubProducts', SubProductsList)

urlpatterns = router.urls