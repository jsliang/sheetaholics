# Create your views here.

import datetime
import generator
from django.http import HttpResponse
from django.shortcuts import render_to_response
from dottedlined.models import Log

# http://127.0.0.1:8000/getpdf?dotColor=%23000000&lineColor=%23000000&gridSize=8&pageWidth=210&pageHeight=297&marginInner=20&marginOuter=15&marginTop=15&marginBottom=15&dotDiameter=0.4&lineWidth=0.2&pageCount=2

def index(request):
    return render_to_response('dottedlined/form.html')

def getpdf(request):
    l = Log(query_string = request.META['QUERY_STRING'], remote_addr = request.META['REMOTE_ADDR'])
    l.save()

    pdf_filename = "dottedlinedsheets_%s.pdf" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_filename
    
    config = {}
    for key, value in request.GET.items():
        value = value.strip()

        if key != 'dotColor' and key != 'lineColor':
            config[key] = float(value)
        else:
            config[key] = value
    
    response.write(generator.get_pdf_content(config))
    
    return response
