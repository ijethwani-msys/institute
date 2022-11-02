from rest_framework.views import APIView
from rest_framework.response import Response

class Home(APIView):
    def post(self,request):
        data = request.data
        return Response({"your_data":data})
