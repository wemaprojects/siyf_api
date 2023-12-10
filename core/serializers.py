from rest_framework import serializers

class FeedbackSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    text = serializers.CharField()
    date = serializers.DateTimeField(read_only=True)
    ip = serializers.CharField(required=False)

class NewsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    image = serializers.ImageField()
    text = serializers.CharField()
