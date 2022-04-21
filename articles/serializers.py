from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'



class ArticleDetailSerializer(serializers.ModelSerializer):
    # commnet_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comment_set에 위와 같이 디폴트로 들어있음...
    # comment_set = CommentListSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comment_set', 'comment_count')
        # => comment_set pk만 보임



class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        # read_only도 가능
        exclude = ('article', )