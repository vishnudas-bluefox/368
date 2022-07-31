import fpdf 
import datetime 

pdf = fpdf.FPDF(format='letter') 
pdf.add_page() #create new page
pdf.set_font("Arial", size=10) # font and textsize
to=input('''To,
The Public information Officer ''')
pin=input("pin  : ")
name=input("name")
adr=input("adress ")
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
ques1 =input("enter your first question")
ques2 =input("enter your second question")
ques3 =input("enter your third question")


text= "\n     APPLICATION FOR SUPPLYING INFORMATIONS UNDER THE RIGHT TO INFORMATION ACT, 2005.\n\n\n\n\n\n\n\nTo,\nThe Public information Officer"+str(to)+'''\nPIN:'''+str(pin)+'''
from:'''+name+ '''
'''+adr+'''
Sir,
Date:'''+date+'''
\nSub: RTI Application U/s 6(1) of the RTI Act,05; read with W.B. RTI Rules,06(Amended and in force till date). (Gist of the subject matter of the information sought. (concerned department, year etc
details) if you do not know these details then avoid it.
\nSir/Madam/Authority,\n As cited abovel, Shri / Smt '''+name+''', a permanent resident of '''+adr+''', and being a citizen of Republic Of India and the rights conferred in the RTI Act,05 to the citizens, I would like to know the following information's from you, under section 6 sub-section (1) of the said act.
\n(1) '''+ques1+''' \n(2) '''+ques2+''' \n(3) '''+ques3+'''

I would like to receive these information's in printed format, and through Post, at my address/ I will personally receive these information's from your office, do not send any information's through Post.
Requesting you, If the information sought pertains another department and/ or another authority then transfer it under section 6(4) of the RTI Act,05 and sent a intimation to me. Please send the information's within time specified under section 7(1) of the said act. If you, at any circumstances, reject this RTI application then do send the mandatory information's u/s 7(8)(i), 7(8)(ii), 7(8)(iii) of the said act.
\nYour's faithfully,
\n'''+name
pdf.multi_cell(0, 6, txt =text, border = 0, 
                 align= 'J', fill=False)

# pdf.cell(200, 10, txt="your text", ln=2, align="L")
# pdf.cell(200, 10, txt="your text", ln=3, align="L")
pdf.output("test6.pdf")