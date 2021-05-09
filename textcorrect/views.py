from django.http import HttpRequest,request
from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def correct(request):
    text = request.POST.get("input","default")
    remPunc = request.POST.get("remPunc","off")
    capital = request.POST.get("capital","off")
    extraspaceRem = request.POST.get("extraspaceremover","off")
    puctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    corrected = ""
    if remPunc == 'on' and capital == 'off' and extraspaceRem == 'off':
        for char in text:
            if char not in puctuations:
                corrected = corrected + char

    elif remPunc == 'off' and capital == 'on' and extraspaceRem == 'off':
        corrected = str.upper(text)

    elif remPunc == 'on' and capital == 'on' and extraspaceRem == 'off':
        for char in text:
            if char not in puctuations:
                corrected = corrected + char
        corrected = str.upper(corrected)

    elif extraspaceRem == 'on' and remPunc == 'off' and capital == 'off':
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index-1] == " "):
                corrected = corrected + char

    elif remPunc == 'off' and capital == 'on' and extraspaceRem == 'on':
        for index,char in enumerate(text):
            if not(text[index] == " " and text[index-1] == " "):
                corrected = corrected + char
        corrected = str.upper(corrected)
    elif remPunc == 'on' and capital == 'off' and extraspaceRem == 'on':
        for index,char in enumerate(text):
            if char not in puctuations and not(text[index] == " " and text[index-1] == " "):
                corrected = corrected + char

    elif remPunc == 'on' and capital == 'on' and extraspaceRem == 'on':
        for index,char in enumerate(text):
            if char not in puctuations and not(text[index] == " " and text[index-1] == " "):
                corrected = corrected + char
        corrected = str.upper(corrected)

    else:
        return HttpResponse('''<h3>Error Selecting Checkbox!!!</h3>''')
    
    params = {"corrected":corrected}
    
    return render(request, "correct.html",params)