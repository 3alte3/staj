from django.contrib import admin
from django.urls import path, re_path, include
from showroom.views import *
from buyer.views import *
from provider.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Api swagger",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.kek.com/policies/terms/",
      contact=openapi.Contact(email="contact@asd.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/v1/showroom/', ShowroomAPIView.as_view()),
    path('api/v1/charact_showroom/', Charact_ShowroomAPIView.as_view()),
    path('api/v1/cars/', CarsAPIView.as_view()),
    path('api/v1/history/', HistoryAPIView.as_view()),
    path('api/v1/unique/', UniqueBuyersAPIView.as_view()),
    path('api/v1/buyers/',BuyerAPIView.as_view()),

    path('api/v1/buyersdelete/<int:pk>',BuyerAPIViewDelete.as_view()),
    path('api/v1/buyersHistory/',BuyerHistoryAPIView.as_view()),

    path('api/v1/provider/',ProviderAPIView.as_view()),

    path('api/v1/providerListOfCarsDelete/<int:pk>',ListOfCarsAPIViewDelete.as_view()),
    path('api/v1/providerListOfCars/',ListOfCarsAPIView.as_view()),


    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
