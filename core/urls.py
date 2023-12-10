from django.urls import path 
from .views import (
        FeedbackView, FeedbackList, FeedbackCreateView,
        NewsDeleteView, NewsListView, NewsCreateView,
        HeaderNews, HeaderNewsDeleteView, HeaderNewsCreateView, HeaderNewsListView
          )

urlpatterns = [

    path('feedback/list/', FeedbackList.as_view()), 
    path('feedback/create/', FeedbackCreateView.as_view()),
    path('feedback/<int:id>/', FeedbackView.as_view()), 

    path('header_news/list/', HeaderNewsListView.as_view()), 
    path('header_news/create/', HeaderNewsCreateView.as_view()),
    path('header_news/delete/<str:id>/', HeaderNewsDeleteView.as_view() ),
    # path('header_news/detailed/<str:id>/', HeaderNewsDeleteView.as_view() ),

    path('news/list/', NewsListView.as_view()), 
    path('news/create/', NewsCreateView.as_view()),
    path('news/delete/<str:id>/', NewsDeleteView.as_view() ),
    # path('news/detailed/<str:id>/', newdele.as_view() ),
]
