from django.urls import path, include
from apis.views import weather, menu, images

urlpatterns = [
    path('test', weather.helloworld),
    path('weather', weather.weather),
    path('menu', menu.get_menu),
    # path('image', images.image),
    path('imagetext', images.image_text),
    path('image', images.ImageView.as_view())
]
