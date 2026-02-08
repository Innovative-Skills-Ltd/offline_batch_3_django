
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from sample.models import User

def sample_view(req):

    return HttpResponse("Offline Batch 3")

def sum(req):
    x = 1
    y = 2
    z = x+y
    return HttpResponse(z)

def demo_template(req):
    response_text = f"""
    Method: {req.method}
    GET data: {req.GET}
    POST data: {req.POST}
    Path: {req.path}
    Full Path: {req.get_full_path()}
    User: {req.user}
    Headers: {dict(req.headers)}
    """

    name = "salman"
    password="1234"
    data ={'uname':name,'pw':password}

    #return HttpResponse(response_text, content_type="text/plain")
    return render(req,'demo.html',data)

def demo_insert(req):

    name = req.POST.get('uname')
    conpw = req.POST.get('conpw')

    pw = req.POST.get('pw')
    if(len(name)==0 or len(pw)==0 or len(conpw)==0):
        return HttpResponse("these field can not be empty")
    else:

        if (pw!=conpw):
            return HttpResponse("The password does not match")
        elif(len(name)>20):
            return HttpResponse("the name size must be below 21")
        # else:
        #     User.objects.create(u_name=name,password=pw)
        #     return HttpResponse("Successfully Done")

        else:
            create_user = User(u_name=name,password=pw)
            create_user.save()
            return redirect('show_user')

    #which insert approach is fast, when to use, why it is fast or slow
    # if len(name)==0 or len(pw)==0:
    #     return HttpResponse("the field can not be empty")

def user_list(req):
    data = User.objects.all().order_by('-id')
    d = {'users':data}
    return render(req,'show_user.html',d)

def editUser(req,uid):
    single_user = get_object_or_404(User,id=uid)
    s_user = {"data":single_user}
    return render(req,'edit_user.html',s_user)

def update_user(req):

    name = req.POST.get('uname')
    conpw = req.POST.get('conpw')
    uid = req.POST.get('id')

    pw = req.POST.get('pw')
    if(len(name)==0 or len(pw)==0 or len(conpw)==0):
        return HttpResponse("these field can not be empty")
    else:

        if (pw!=conpw):
            return HttpResponse("The password does not match")
        elif(len(name)>20):
            return HttpResponse("the name suidize must be below 21")
        # else:
        #     User.objects.create(u_name=name,password=pw)
        #     return HttpResponse("Successfully Done")

        else:
            print(uid)
            user = get_object_or_404(User,id=uid)
            user.u_name = name
            user.password = pw
            user.save()
            return redirect('show_user')

    # #which insert approach is fast, when to use, why it is fast or slow
    # # if len(name)==0 or len(pw)==0:
    # #     return HttpResponse("the field can not be empty")

    

