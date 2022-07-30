from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# rti pdf 
@api_view(['POST'])
def createpdf(request):
    if request.method == 'POST':
        # print(request.data)
        referenceid = request.data['refernceid']
        fromname = request.data['fromname']
        fromaddress = request.data['fromaddress']
        toname = request.data['toname']
        todesignation = request.data['todesignation']
        toaddress = request.data['toaddress']
        onewordrti = request.data['onewordrti']
        questions = request.data['questions']

        print(referenceid,fromname,fromaddress,toname,todesignation,toaddress,onewordrti,questions)
        return Response({"message":"success"})
    else:
        return Response({"success":False})