from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from agency import views as agency_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',users_views.register, name='signup'),
    path('',users_views.login, name='login'),
    path('debtors/',agency_views.debtors, name='debtors'),
    path('filteredDebtors/',agency_views.filteredDebtors, name='filteredDebtors'),
    path('updateDebtors/<int:id>/',agency_views.updateDebtors, name='updateDebtors'),
    path('creditors/',agency_views.creditors, name='creditors'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('agency.api.urls')),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

