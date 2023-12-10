from django.urls import path 
from .views import (
        FeedbackView, FeedbackList, FeedbackCreateView,
        NewsDetailView, NewsListView, NewsEditView,
        HeaderNews, HeaderNewsDetailView, HeaderNewsEditView, HeaderNewsListView
          )

urlpatterns = [

    path('feedback/list/', FeedbackList.as_view()), 
    path('feedback/create/', FeedbackCreateView.as_view()),
    path('feedback/<int:id>/', FeedbackView.as_view()), 

    path('header_news/list/', HeaderNewsListView.as_view()), 
    path('header_news/create/', HeaderNewsEditView.as_view()),
    path('header_news/delete/<str:id>/', HeaderNewsEditView.as_view() ),
    path('header_news/detailed/<str:id>/', HeaderNewsDetailView.as_view() ),

    path('news/list/', NewsListView.as_view()), 
    path('news/create/', NewsEditView.as_view()),
    path('news/delete/<str:id>/', NewsEditView.as_view() ),
    path('news/detailed/<str:id>/', NewsDetailView.as_view() ),

]
