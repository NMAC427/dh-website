from django.conf.urls import url

from . import views

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<date>[0-9]+[\/][0-9]+[\/][0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealView.as_view(), name='display_meal'),
    url(r'^meal/(?P<pk>[0-9]+)/rate/$', views.RateMealView.as_view(), name='rate_meal'),
    url(r'^menu/add$', views.MenuAddView.as_view(), name='add_menu'),
    url(r'^menu/(?P<pk>[0-9]+)/edit$', views.MenuEditView.as_view(), name='edit_menu'),
    url(r'^menu/(?P<pk>[0-9]+)/delete$', views.MenuDeleteView.as_view(), name='delete_menu'),
    url(r'^modify_lateplate/(?P<meal_pk>[0-9]+)/(?P<user_pk>[0-9]+)/$', views.modify_lateplate, name='modify_lateplate'),
    url(r'^shopper/(?P<pk>[0-9]+)/$', views.ShopperView.as_view(), name='shopper'),
    url(r'^auto_lateplates/$', views.auto_lateplates, name='auto_lateplates'),
    url(r'^submit_auto_lateplates/$', views.submit_auto_lateplates, name="submit_auto_lateplates"),
    url(r'^menu_reviews/', views.ReviewsView.as_view(), name="menu_reviews")
]

