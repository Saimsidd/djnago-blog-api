from django.urls import path
from . import views


urlpatterns = [
    path("saimblog/",views.BlogPostListCreate.as_view(),name="blog-post"),
    path("saimblog/<int:pk>/",views.BlogPostRetriveUpdateDestory.as_view(),name="update")
    
]