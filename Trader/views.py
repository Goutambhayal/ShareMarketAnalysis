from django.http import HttpResponse;
from django.shortcuts import render;
from django.db import connection;
from intradayData.models import intradata

def homePage(request):
    return render(request,'index.html')

def intraday(request):
    context={}
    try:
       if request.method=='POST':
           context={ 'goutam':50}
           companyName=(request.POST.get('companyName'))
           marketCap=(request.POST.get('marketCap'))
           n=float(request.POST.get('initialPrice'))
           n2=float(request.POST.get('maxOfGap'))
           n3=float(request.POST.get('minOfGap'))
           n4=float(request.POST.get('finalPrice'))
           n1=n4-n
           maxOfGap=(n2-n1)*100/n1
           
           minOfGap=(n3-n1)*100/n1
           
           gap=maxOfGap-minOfGap
           
           finalGain=(n4-n1)*100/n1
           
           n5=float(request.POST.get('dayHighPrice'))
           dayHigh=(n5-n1)*100/n1
           n6=float(request.POST.get('dayLowPrice'))
           dayLow=(n6-n1)*100/n1
           c=dayHigh-dayLow
           if (-20<gap<=20 and gap<=c and maxOfGap<=dayHigh and minOfGap>=dayLow and  -20<maxOfGap<=20 and -20<minOfGap<=20 and finalGain<=20 and dayHigh<=20 and dayLow>-20):
              en = intradata(companyName=companyName,marketCap=marketCap,initialPrice=n1,finalPrice=n4,maximaOfGap=maxOfGap,minimaOfGap=minOfGap,gap=gap,finalGain=finalGain,dayHigh=dayHigh,dayLow=dayLow)
              en.save()
           else:
              context['error'] = {'check': "Please check data you entered"}
                   
                 
              
       else:
          pass
    except Exception as e:
       print(f"An error occurred: {e}")  # This will log the error to the console
       raise
    return render(request,'intraday.html',context)
def dayTwo(request):
    context={}
    try:
       if request.method=='POST':
           companyName=(request.POST.get('companyName'))
           n=float(request.POST.get('initialPrice'))
           n2=float(request.POST.get('maxOfGap'))
           n3=float(request.POST.get('minOfGap'))
           n4=float(request.POST.get('finalPrice'))
           n1=n4-n
           maxOfGap=(n2-n1)*100/n1
           
           minOfGap=(n3-n1)*100/n1
           
           gap=maxOfGap-minOfGap
           
           finalGain=(n4-n1)*100/n1
           
           n5=float(request.POST.get('dayHighPrice'))
           dayHigh=(n5-n1)*100/n1
           n6=float(request.POST.get('dayLowPrice'))
           dayLow=(n6-n1)*100/n1
           c=dayHigh-dayLow
           if (-20<gap<=20 and c>=gap and -20<maxOfGap<=20 and maxOfGap<=dayHigh and minOfGap>dayLow and -20<minOfGap<=20 and finalGain<=20 and dayHigh<=20 and dayLow>-20):
              with connection.cursor() as cursor:
                 query="UPDATE intradaydata_intradata SET maximaOfGap1 = %s,minimaOfGap1 = %s,gap1 = %s,finalgain1 = %s,finalPrice1 = %s, dayHigh1=%s,dayLow1=%s WHERE companyName=%s"
                 cursor.execute(query,[maxOfGap,minOfGap,gap,finalGain,n4,dayHigh,dayLow,companyName]) 
           else:
              context['error'] = {'check': "Please check data you entered"}
                   
           
       else:
          pass
    except Exception as e:
       print(f"An error occurred: {e}")  # This will log the error to the console
       raise

    
    return render(request,'day2.html',context)
def dayThree(request):
    context={}
    try:
       if request.method=='POST':
           companyName=(request.POST.get('companyName'))
           n=float(request.POST.get('initialPrice'))
           n2=float(request.POST.get('maxOfGap'))
           n3=float(request.POST.get('minOfGap'))
           n4=float(request.POST.get('finalPrice'))
           n1=n4-n
           maxOfGap=(n2-n1)*100/n1
           
           minOfGap=(n3-n1)*100/n1
           
           gap=maxOfGap-minOfGap
           
           finalGain=(n4-n1)*100/n1
           
           n5=float(request.POST.get('dayHighPrice'))
           dayHigh=(n5-n1)*100/n1
           n6=float(request.POST.get('dayLowPrice'))
           dayLow=(n6-n1)*100/n1
           c=dayHigh-dayLow
           if (-20<gap<=20 and gap<=c and maxOfGap<dayHigh and minOfGap>dayLow and  -20<maxOfGap<=20 and -20<minOfGap<=20 and finalGain<=20 and dayHigh<=20 and dayLow>-20):
              with connection.cursor() as cursor:
                 query="UPDATE intradaydata_intradata SET maximaOfGap2 = %s,minimaOfGap2 = %s,gap2 = %s,finalgain2 = %s,finalPrice2 = %s, dayHigh2=%s,dayLow2=%s WHERE companyName=%s"
                 cursor.execute(query,[maxOfGap,minOfGap,gap,finalGain,n4,dayHigh,dayLow,companyName]) 
           else:
              context['error'] = {'check': "Please check data you entered"}
           
              
       else:
          pass
    except Exception as e:
       print(f"An error occurred: {e}")  # This will log the error to the console
       raise
    return render(request,'day3.html',context)

def banknifty(request):
    return render(request,'banknifty.html')

def midcapnifty(request):
    return render(request,'midcapnifty.html')

def sensex(request):
    return render(request,'sensex.html')

def niftyfifty(request):
    return render(request, 'niftyfifty.html')