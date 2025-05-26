from .models import Blog, BlogImage
from rest_framework import serializers

class BlogImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BlogImage
        fields = ['image']


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname')
    images = serializers.SerializerMethodField()

    # 게시글에 등록된 이미지 가져오기
    def get_images(self, obj):
        image = obj.images.all()  # related_name에 맞게 변경
        return BlogImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Blog
        fields = ['id', 'title', 'created_at', 'user', 'body', 'images']

    def create(self, validated_data):
        instance = Blog.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            BlogImage.objects.create(blog=instance, image=image_data)
        return instance