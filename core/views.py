
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Feedback, HeaderNews, News
from .serializers import FeedbackSerializer, NewsSerializer


class FeedbackList(APIView):
    def get(self, request):
        return Response(FeedbackSerializer(Feedback.objects.all(), many=True).data, status=200)
    
class FeedbackCreateView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            feedback = Feedback.objects.create(**serializer.validated_data)
            return Response(FeedbackSerializer(feedback).data, status=200)

class FeedbackView(APIView):
    def get(self, request, id):
        try:
            feedback = Feedback.objects.get(id=id)
        except:
            return Response({"error" : f"Feedback with id {id} not found"}, status=404)
        return Response(FeedbackSerializer(feedback).data, status=200)
    
    def delete(self, request : HttpRequest, id):
            if bool(request.user and request.user.is_authenticated):
                try:
                    feedback = Feedback.objects.get(id=id)
                except:
                    return Response({"error" : f"Feedback with id {id} not found"}, status=404)
                feedback.delete()
                return Response({'status' : "Removed"}, status=status.HTTP_200_OK) 
            else:
                return Response({'error' : "only manager operation"}, status=status.HTTP_403_FORBIDDEN)
            




class HeaderNewsDeleteView(APIView):
    def delete(self ,reqeust, id):
        try: news = HeaderNews.objects.get(id=id)
        except : return Response({"error" : f"News with id {id} not found"}, 404) 
        
        return Response(NewsSerializer(news).data, 200)

class HeaderNewsListView(APIView):
    def get(self, request):
        return Response(NewsSerializer(HeaderNews.objects.all(), many=True).data, 200)

class HeaderNewsEditView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            valdata = serializer.validated_data
            news = HeaderNews.objects.create(**valdata)
            return Response({}, status=200)

    def delete(self ,reqeust, id):
        try: news = HeaderNews.objects.get(id=id)
        except : return Response({"error" : f"HeaderNews with id {id} not found"}, 404) 
        news.delete()
        return Response({}, 200)
    




class NewsDeleteView(APIView):
    def delete(self ,reqeust, id):
        try: news = News.objects.get(id=id)
        except : return Response({"error" : f"News with id {id} not found"}, 404) 
        
        return Response(NewsSerializer(news).data, 200)

class NewsListView(APIView):
    def get(self, request):
        return Response(NewsSerializer(News.objects.all(), many=True).data, 200)

class NewsEditView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            valdata = serializer.validated_data
            news = News.objects.create(**valdata)
            return Response({}, status=200)

    def delete(self ,reqeust, id):
        try: news = News.objects.get(id=id)
        except : return Response({"error" : f"News with id {id} not found"}, 404) 
        news.delete()
        return Response({}, 200)
    

