from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from .forms import TranslateForm
import re


#API
class translateApi(APIView):
    render_classes = [TemplateHTMLRenderer,]
    template_name = 'index.html'

    def get(self, request):
        outdata = " "
        return Response({'outdata' : outdata})

    def post(self, request):
        txt = request.POST['sendertext']
        ####### operations ########
        outtext = txt
        # Not English
        reg_en = re.compile(r'[A-Za-z]')
        flag_en = re.search(reg_en , txt)
        if flag_en == None :
            a = 'ال'
            b = 'لا'
            outtext = txt.replace(a,b)
        else :
            # English & Persian
            reg_fa = re.compile(r'[ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدپوآأإييئؤةك]')
            flag_fa = re.search(reg_fa , txt)
            if flag_fa != None :
                outtext = ""
                list_outtext = txt.split(" ")
                result_outtext = []
                for lo in list_outtext :
                    flag_fa = re.search(reg_fa , lo)
                    if flag_fa != None :
                        result_outtext.append(lo)
                    else :
                        result_outtext.append(lo[::-1])
                outtext = " ".join(result_outtext)
        ##### End Operations #####
        return Response({'outdata' : outtext})




