from rest_framework.decorators import api_view
from rest_framework.response import Response


# for creating pdf 

import fpdf 
import datetime 

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


        pdf = fpdf.FPDF(format='letter') 
        pdf.add_page() #create new page
        pdf.set_font("Arial", size=10) # font and textsize
        to='''To,
        The Public information Officer '''+toname+"\n"+todesignation+"\n"+toaddress+"\n"
        pin="678442"
        name=fromname 
        adr=fromaddress
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        questions=list(questions)


        text= "\n     APPLICATION FOR SUPPLYING INFORMATIONS UNDER THE RIGHT TO INFORMATION ACT, 2005.\n\n\n\n\n\n\n\nTo,\nThe Public information Officer"+str(to)+'''\nPIN:'''+str(pin)+'''
        from: '''+name+ '''
        '''+adr+'''
        Sir,
        Date:'''+date+'''
        \nSub: RTI Application U/s 6(1) of the RTI Act,05; read with W.B. RTI Rules,06(Amended and in force till date). (Gist of the subject matter of the information sought. (concerned department, year etc
        details) if you do not know these details then avoid it.
        \nSir/Madam/Authority,\n As cited abovel, Shri / Smt '''+name+''', a permanent resident of '''+adr+''', and being a citizen of Republic Of India and the rights conferred in the RTI Act,05 to the citizens, I would like to know the following information's from you, under section 6 sub-section (1) of the said act.
        \n(1) '''+questions[0]+''' \n(2) '''+questions[1]+''' \n(3) '''+questions[2]+'''

        I would like to receive these information's in printed format, and through Post, at my address/ I will personally receive these information's from your office, do not send any information's through Post.
        Requesting you, If the information sought pertains another department and/ or another authority then transfer it under section 6(4) of the RTI Act,05 and sent a intimation to me. Please send the information's within time specified under section 7(1) of the said act. If you, at any circumstances, reject this RTI application then do send the mandatory information's u/s 7(8)(i), 7(8)(ii), 7(8)(iii) of the said act.
        \nYour's faithfully,
        \n'''+name
        pdf.multi_cell(0, 6, txt =text, border = 0, 
                        align= 'J', fill=False)

        # pdf.cell(200, 10, txt="your text", ln=2, align="L")
        # pdf.cell(200, 10, txt="your text", ln=3, align="L")
        pdf.output("test6.pdf")
        url="file:///home/unknown/Desktop/programs/Miniproject/final/error/firstTestCase/backend/test6.pdf"
        return Response({"message":"success" ,"url":url})
    else:
        return Response({"success":False})