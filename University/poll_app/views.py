from django.shortcuts import render,get_object_or_404
from poll_app.forms import UserProfileInfoForm,UserForm,Questionform,AnswerForm
from poll_app.models import Instructors,Questions,Answers,User
from itertools import chain
#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
   return render(request,'poll_app/index.html')

@login_required
def panel(request):
    ishead = request.user.groups.filter(name='head').exists()
    print(ishead)

    postingdone = False
    username = request.user.username

    postedquestions = Questions.objects.all()
    postedquestions_id =Questions.objects.values_list('id')

    print(postedquestions_id)
    print(postedquestions)
    if request.method == "POST":
        form = Questionform(data=request.POST)
        if form.is_valid():
            form.save()
            postingdone = True
    else:
        form = Questionform()
    return render(request,'poll_app/panel.html',
                {'form': form,
                'username':username,
                'ishead':ishead,
                'postingdone':postingdone,
                'postedquestions':postedquestions,
                })

@login_required
def question(request,qid):
    ishead = request.user.groups.filter(name='head').exists()
    content= Questions.objects.get(id=qid)

    answered = False


    postedanswers = Answers.objects.filter(QID = qid)
    query_of_answers = postedanswers.values('userid')
    users_queryset = User.objects.filter(id = query_of_answers)
    list_of_users = users_queryset.values('username')



    userids = []
    descriptions = []

    for p in postedanswers:
       userids.append(p.userid)
       descriptions.append(p.Description)
    print(userids)

    usernames = []

    for u in userids:
       thisuser = User.objects.get(id = u)
       usernames.append(thisuser)
    print('this user usernames list')
    print(usernames)
    desc_and_user = usernames + descriptions
    print(desc_and_user)
    print('this is descriptions list')
    print(descriptions)
    count = len (descriptions)
    print(count)

    if request.method == "POST":

        Answer_form = Answers()

        if qid and request.user.id and request.POST.get('Answer'):

            Answer_form.QID =  qid
            Answer_form.userid = request.user.id
            Answer_form.Description = request.POST.get('Answer')
            Answer_form.save()

            answered = True
        else:
            print("some input errors")
            print(request.POST.get('userid'))
            print(request.POST.get('qid'))
            print(request.POST.get('Answer'))
    my_dict ={'form':content,'answered':answered,'ishead':ishead,'postedanswers':postedanswers,'usernames':usernames,'range':range(count)}
    return render(request,'poll_app/questions.html',my_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in , nice ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def question_remove(request,qid):

    question = get_object_or_404(Questions,pk=qid)
    question.delete()
    return render(request,'poll_app/panel.html')



def signup(request):

   registered = False

   if request.method == "POST":

       signup_form  = UserForm(data=request.POST)
       profile_form = UserProfileInfoForm(data=request.POST)

       if signup_form.is_valid() and profile_form.is_valid():

          user = signup_form.save()
          user.set_password(user.password)
          user.save()

          #READ ABOUT .SAVE !
          profile = profile_form.save(commit=False)
          profile.user = user

          if 'profile_pic' in request.FILES:
              profile.profile_pic == request.FILES['profile_pic']

          profile.save()


          registered = True
       else:
          print(signup_form.errors,profile_form.errors)
   else:
        signup_form = UserForm()
        profile_form = UserProfileInfoForm()

   return render(request,'poll_app/signup.html',{
                         'UserForm':signup_form,
                         'userProfileInfoForm':profile_form,
                         'registered':registered
                                 })


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('panel'))
            else:
                return HttpResponse("account not active")
        else:
            print("someone tried to login and failed")
            print("username : {} and password : {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'poll_app/login.html',{})
