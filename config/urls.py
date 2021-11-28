from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        description='Oddiy Blog project APIsi',
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="khusanboy9700@mail.ru"),
        license=openapi.License(name="Blog project litsenziyasi"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),  # new
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/allauth/', include('allauth.urls')),
    # path('openapi', get_schema_view(
    #     title='Blog API',
    #     description='Django rest framewokini o`rganish uchun blog API loyihasi',
    #     version='1.0.0',
    # ), name='openapi-schema'),
    path('swagger/', schema_view.with_ui(  # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(  # new
        'redoc', cache_timeout=0), name='schema-redoc'),

]
