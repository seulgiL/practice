from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer,
    ArticleDetailSerializer,
    CommentListSerializer,
    CommentCreateSerializer,
)





@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.order_by('-pk')
        # articles => query set / article => instance : Json, dic 아님!
        # 직렬화 과정
        serializer = ArticleListSerializer(articles, many=True)
        
        # data 형태 (JSON or dict)
        return Response(serializer.data)

    elif request.method == 'POST':
        # request.POST, request.GET 이제 안쓰고 ==> request.data로 사용
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'message':'이거 진짜 됩니까?'})


# detail 대신 retrieve라는 표현 많이 사용(single modle instance)
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        article.delete()
        return Response({'message': f'{pk}번 게시물이 삭제되었습니다.'}, status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def article_comment_list_create(request, pk):
    article  = get_object_or_404(Article, pk=pk)
    if request.method == 'GET': 
        comments = get_list_or_404(article.comment_set.order_by('-pk'))
        serializers = CommentListSerializer(comments, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def article_comment_update_delete(request, article_pk, pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(article.comment_set, pk=pk)
    if request.method == 'PUT':
        serializer = CommentCreateSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({'message': f'{pk}번 댓글이 삭제되었습니다.'})

