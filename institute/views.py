from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
def home(request):
    return HttpResponseRedirect("/api/")

# class Home(APIView):
#     def post(self,request):
#         data = request.data
#         return Response({"your_data":data})
