# myapp/api/v1/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def profile(request):
    name = request.data.get("name")
    age = request.data.get("age")

    return Response({
        "version": "v1",
        "name": name,
        "age": age,
    })
