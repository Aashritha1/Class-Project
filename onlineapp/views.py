from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from onlineapp.models import College
from onlineapp.serializers import CollegeSerializer,StudentSerializer,MockTest1Serializer
from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from onlineapp.models import *
from django.template import loader
from django.shortcuts import render
# View (in blog/views.py)
def index(request):
    return HttpResponse("hello")

#def testcookies(request, templates):
 #   response = render(request, templates)  # django.http.HttpResponse
  #  response.set_cookie(key='id', value=1)
   # return response

def testsession(request):
    request.session.setdefault("counter",0)
    call_func=request.session["counter"]+1
    request.session["counter"]=call_func
    return HttpResponse(request.session["counter"])

def testcookies(request):
    call_func=request.session.setdefault("counter",0)
    response=HttpResponse()
    response.set_cookie("onlineapp"+str(request.session["counter"]),"this is a cookie",max_age=60)
    response.write("<html><body><table>")
    for key,value in request.COOKIES.iteritems():
        response.write("<tr><th>{0}</th><th>{1}</th></tr>".format(key,value))
    response.write(("</table></body></html>"))
    return response


def collegeinfo(request):
    collegelist=College.objects.all()
    template=loader.get_template('onlineapp/index1.html')
    context={
        'collegelist':collegelist,
    }
    return HttpResponse(template.render(context,request))


def marksinfo(request,c_id):
    mlist=MockTest1.objects.values('student__name','total').filter(student__college__id=c_id).order_by('-total')
    template=loader.get_template('onlineapp/index.html')
    context={
        'mlist':mlist,
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def college_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = College.objects.all()
        serializer = CollegeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CollegeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def college_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollegeSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CollegeSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



@csrf_exempt
def student_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def student_marks_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = MockTest1.objects.get(student__id=pk)
    except MockTest1.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MockTest1Serializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MockTest1Serializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def college_stud_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.filter(college__id=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(snippet,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


from django.contrib.auth.decorators import login_required

@login_required
def like_category(request,pk):

    cat_id = None
    if request.method == 'GET':
        print("aashritha")
       # print("abcgd%s "%(request.GET['id']))
        cat_id=pk

    likes = 0
    if cat_id:
        cat = College.objects.get(id=cat_id)
        template = loader.get_template('onlineapp/template.html')
        if cat:
            likes = likes + 1
            cat.save()

    return HttpResponse(likes)