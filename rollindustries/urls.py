from django.urls import path
from . import views as mainView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', mainView.homePage, name='homePage'),
    path('legacy/', mainView.originMode, name='origin'),
]
