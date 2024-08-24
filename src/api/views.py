from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from django.db.models import Q

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer


# Create your views here.


@api_view(["GET"])
def status(request):
    data = {
        "status": "Server is in good health",
        "endpoints": [
            "/v1/healthcheck",
            "/v1/advocates",
            "/v1/advocates/:username",
            "/v1/companies",
        ],
    }
    return Response(data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def advocates_list(request):
    """
    API endpoint for geting and adding advocates
    """
    if request.method == "GET":
        query = request.GET.get("query")
        if query is None:
            query = ""
        advocates = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query)
        )
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        advocate = Advocate.objects.create(
            username=request.data["username"], bio=request.data["bio"]
        )

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            return Response("Advocate does not exist")

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response("User has been deleted")


@api_view(["GET"])
def companies_list(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query is None:
            query = ""
        companies = Company.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
