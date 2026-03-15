from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WeatherSerializer, TodoSerializer


# Create your views here.

class WeatherView(APIView):
    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# In-memory store
TODOS = []
NEXT_ID = 1


class TodoView(APIView):
    def get(self, request):
        serializer = TodoSerializer(TODOS, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        global NEXT_ID
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.validated_data
            todo["id"] = NEXT_ID
            # increment counter
            NEXT_ID += 1
            TODOS.append(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        for todo in TODOS:
            if todo["id"] == id:
                completed = request.data.get("completed")
                if completed is None:
                    return Response(
                        {"error": "completed field required"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                todo["completed"] = completed
                return Response(todo, status=status.HTTP_200_OK)
        return Response(
            {"error": "Todo not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, id):
        for i, todo in enumerate(TODOS):  # Why enumerate() is used You need the index to remove the item from the list:TODOS.pop(i)
            if todo["id"] == id:
                TODOS.pop(i)
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_204_NO_CONTENT)