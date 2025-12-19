# myapp/api/v2/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def profile(request):
    name = request.data.get("name")
    age = request.data.get("age")
    address = request.data.get("address")   # extra field in v2

    return Response({
        "version": "v2",
        "name": name,
        "age": age,
        "address": address,
    })
