from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

  # member
  path('member-list/', views.memberList, name="member-list"),
	path('member-create/', views.memberCreate, name="member-create"),
	path('member-delete/<str:pk>/', views.memberDelete, name="member-delete"),

  # region
  path('region-list/', views.regionList, name="region-list"),
	path('region-create/', views.regionCreate, name="region-create"),


  # real-estate
	path('re-post-list/', views.realEstatePostList, name="re-post-list"),
	path('re-post-detail/<str:pk>/', views.realEstatePostDetail, name="re-post-detail"),
	path('re-post-create/', views.realEstatePostCreate, name="re-post-create"),

	path('re-post-update/<str:pk>/', views.realEstatePostUpdate, name="re-post-update"),
	path('re-post-delete/<str:pk>/', views.realEstatePostDelete, name="re-post-delete"),

	path('re-post-report/<str:pk>/', views.realEstatePostReport, name="re-post-report")


]