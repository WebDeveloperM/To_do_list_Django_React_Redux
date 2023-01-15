from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBack
# end
# Create your views here.


@api_view(['GET'])
def index(request):
    api_urls = {
        'List': "/task-list/",
        'Detail View': "/task-detail/<str:pk>/",
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

# class TaskFilterOrSearch(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = (DjangoFilterBackend, SearchFilter)
#     filter_fields = ('title')


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    
    return Response({"tasks": serializer.data})


@api_view(["GET"])
def taskDetail(request, slug):
    task = Task.objects.get(slug=slug)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({}, 400)


@api_view(['PUT'])
def taskUpdate(request, slug):
    task = Task.objects.get(slug=slug)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response({}, 400)


@api_view(['DELETE'])
def taskDelete(request, slug):
    Task.objects.get(slug=slug).delete()
    print('Slug')
    return Response('Item Successful deleted')


