from DjangoApp.import_files.model_views import *
from django.shortcuts import render
from DjangoApp.forms import *   
import urllib2 , urllib
# import urllib.request

# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.views.generic import FormView, DetailView, ListView
from .forms import ArticleForm
from .models import UserProfile, Article
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.deprecation import RemovedInDjango20Warning
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404


array =[]
def index(request):
	Articles = Article.objects.filter(is_publish=1).order_by('-id')[:5]
	lock = LockSystem.objects.get(Name='Blog System')
	return render(request,'mysite/index.html',{'Data':Articles , 'lock':lock})

# def details(request,article_id):
# 	Articles = Article.objects.get(pk=article_id )
# 	lock = LockSystem.objects.get(Name='Blog System')
# 	if article_id in array:
# 		print "again"
# 	else:
# 		array.append(article_id)
# 		Articles.veiw_count +=1
# 		Articles.save()
# 	page = "mysite/details.html"
# 	return render(request,page,{'Data':Articles , 'lock':lock})
@csrf_protect
def Article_create(request):
    if request.method == 'POST':    #if there is data or form submitted
        form = ArticleForm(request.POST)
        if form.is_valid(): #check if all validation return true execute methods
            article =Article(
            subject=form.cleaned_data['subject'], #get the data cleaned
            description=form.cleaned_data['description'],
            # image=self.get_form_kwargs().get('files')['image'],
            author_id=request.POST['user']
            )
            article.save()
            # message.success(request,"successfully created")
            # return HttpResponse('Article Added successfully')
            messages.success(request, 'Article Added successfully')
        return HttpResponseRedirect('/Article/create')

    else:
        form = ArticleForm()
    article=Article.objects.filter(author_id=request.session['_auth_user_id'])
    variables = RequestContext(request, {'form': form,'data':article})
    return render_to_response('mysite/Article_create.html',variables,)

def Article_Edit(request,article_id):
    # article=get_object_or_404(Article,id=article_id)
    # if request.method == 'POST':        
    #         article.subject=request.POST['sub'] #get the data cleaned
    #         article.description=request.POST['des']
    #         # image=self.get_form_kwargs().get('files')['image'],
    #         # author_id=request.POST['user']            
    #         article.save(commit=True)
    #         # return HttpResponse('Article Added successfully')
    #         variables = RequestContext(request, {'artData':article})
    #         return render_to_response('mysite/Article_create.html',variables,)
    # else:        
    #     variables = RequestContext(request, {'artData':article})
    #     return render_to_response('mysite/Article_edit.html',variables,)
################################################################################
    if request.method == 'POST':    #if there is data or form submitted
        article=get_object_or_404(Article,id=article_id)
        form = ArticleForm(request.POST)
        if form.is_valid(): #check if all validation return true execute methods
            article.subject=request.POST['sub'] #get the data cleaned
            article.description=request.POST['des']
            article.save(commit=True)
            
            # message.success(request,"successfully created")
            # return HttpResponse('Article Added successfully')
            messages.success(request, 'Article Added successfully')
        return HttpResponseRedirect('/Article/create')
    else:
        form = ArticleForm()
    # article=Article.objects.filter(author_id=request.session['_auth_user_id'])
    article=get_object_or_404(Article,id=article_id)
    variables = RequestContext(request, {'artData':article})
    return render_to_response('mysite/Article_edit.html',variables,)


################################################################################3
# def add(request,article_id):
# 	Articles = Article.objects.get(pk=article_id)
# 	comments = Comment.objects.all()
# 	ban = banWords.objects.all()
# 	if request.POST['addcomment'] is None: 
# 		print "comment_count"
# 	else:
# 		added= request.POST['addcomment']
# 		com = Comment(content=added, Article_comment_id = Articles)
# 		com.save()
# 		cont = Articles.comment_set.all().count()
# 		Articles.comment_count = cont
# 		Articles.save()
# 	return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})

# def reply(request,comment_id):

# 	# Articles = Article.objects.get(pk=article_id)
# 	comments = Comment.objects.all()
# 	added= request.POST['addcomment']
# 	com = Comment(content=added, Article_comment_id = Articles)
# 	com.save()
# 	cont = Articles.comment_set.all().count()
# 	Articles.comment_count = cont
# 	Articles.save()
# 	return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})



def Delete_comment(request,comment_id):
	comments=comment.objects.get(pk=comment_id)
	comments.delete()

def mark(request,article_id):
	mark =mark.objects.all()
	# mark(user)
	
def GetAllArticle(request):
	Articles = Article.objects.filter(is_publish=1)
	return render(request,'mysite/articles.html',{'Data': Articles})

# Create your views here.
def home(request):
	
	return render(request,'mysite/home.html',{'message': sentence})
   


def login_user(request, template_name='registration/login.html', extra_context=None): 
    # add to make remeber 
    if request.COOKIES.has_key('sessionid'):
        if request.session.has_key('username'):
          username = request.session['username']
          return render(request, 'home.html', {"username" : username})
    else:
        ######## just if 
        response = auth_views.login(request, template_name) 
        if request.POST.has_key('remember_me'):   
            request.session.set_expiry(1209600) # 2 weeks
                #ADD To make remember me
            request.session['username'] = request.POST['username']
            request.session['passward'] =request.POST['password']
            session.save()
        if not request.POST.has_key('remember_me', None):
            request.session.set_expiry(0)
        return render_to_response('login.html', context_instance=RequestContext(request))
# def formView(request):
#    if request.session.has_key('username'):
#       username = request.session['username']
#       return render(request, 'home.html', {"username" : username})
#    else:
#       return render(request, 'login.html', {})
# @login_required(login_url='/login/')
# def main(request):
# def login(request):
#    username = 'not logged in'
   
#    if request.method == 'POST':
#       MyLoginForm = LoginForm(request.POST)
      
#       if MyLoginForm.is_valid():
#          username = MyLoginForm.cleaned_data['username']
#          request.session['username'] = username
#       else:
#          MyLoginForm = LoginForm()
            
#    return render(request, 'loggedin.html', {"username" : username}
		
def logout(request,template_name='registration/logout.html', extra_context=None):
    logout(request)
    return redirect('login')
    # return render(request,'login.html')
# 4 views for password reset:
# - password_reset sends the mail
# - password_reset_done shows a success message for the above
# - password_reset_confirm checks the link the user clicked and
#   prompts for a new password
# - password_reset_complete shows a success message for the above

#@deprecate_current_app
@csrf_protect
def password_reset(request,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   extra_context=None,
                   html_email_template_name=None,
                   extra_email_context=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


# @deprecate_current_app
def password_reset_done(request,
                        template_name='registration/password_reset_done.html',
                        extra_context=None):
    context = {
        'title': _('Password reset sent'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
# @deprecate_current_app
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


# @deprecate_current_app
def password_reset_complete(request,
                            template_name='registration/password_reset_complete.html',
                            extra_context=None):
    context = {
        'login_url': resolve_url(settings.LOGIN_URL),
        'title': _('Password reset complete'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@sensitive_post_parameters()
@csrf_protect
@login_required
# @deprecate_current_app
def password_change(request,
                    template_name='registration/password_change_form.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('password_change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one.
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': _('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)


@login_required
# @deprecate_current_app
def password_change_done(request,
                         template_name='registration/password_change_done.html',
                         extra_context=None):
    context = {
        'title': _('Password change successful'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)

    

def edit_view(request):
    
    # profile = request.user.get_profile()
    title="Welcome %s" %(request.user)
    # user_id = User.objects.get(request.POST['profile_id']) 
    user_id = request.user.id
    instance1=get_object_or_404(User,id=user_id)

    instance2=get_object_or_404(UserProfile,user_id=user_id)
    # return HttpResponse(instance2.user_id)
    form1=UserForm(request.POST or None, instance=instance1)
    form2=UserProfileForm(request.POST , request.FILES)

    if form1.is_valid() and form2.is_valid():

        instance1=form1.save(commit=True)
        # instance2.image = form2.image
        instance2.image = form2.cleaned_data['image']
        instance2.user_id = user_id
        instance2.save()
    context={
        'tempelate_title':title ,
        'insatance1':instance1,
        'insatance2':instance2,
        'form1':form1 ,
        # 'form2':form2 ,
    }
    return render(request,"edit.html",context)
@csrf_protect
def register(request):
    if request.method == 'POST':    #if there is data or form submitted
        form = RegistrationForm(request.POST)
        if form.is_valid(): #check if all validation return true execute methods
            user = User.objects.create_user(
            username=form.cleaned_data['username'], #get the data cleaned
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'],
            )
            send_mail('Thanks', 'Thanks for subscribing to Our Website We appreciate it', settings.EMAIL_HOST_USER,
            [user.email], fail_silently=False)
            return HttpResponseRedirect('/upload/') #after registering go to another URL

    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/index.html',variables,)
    

def register_success(request):
    return render_to_response(  #go to a specific HTML Page
    'registration/success.html',
    )




def details(request, article_id=None):
    instance = Article.objects.get(pk=article_id )
    tags=instance.tags.all()
    word=tags[0]
    tagobj = Tag.objects.get(tag_title=word )
    related_articles=tagobj.article_set.all()
    u_id=instance.author
    name=u_id.username

    context = {
        "subject": instance.subject,
        "description": instance.description,
        "image": instance.image,
        "date": instance.date,
        "username": name,
        "tag": word,
        "Data":related_articles,
        "veiw_count":instance.veiw_count,
        "instance":instance,
        #"id":article_id,
        
    }
    return render(request, "mysite/details.html", context)



def comment(request, article_id):
    if article_id:
        if request.method == 'POST':
            text_of_comment = request.POST.get('content')
            comment = Comment.objects.create(text = text_of_comment, Article = Article.objects.get(id=article_id))
            comment.save()
            comments = Article.objects.get(id = article_id)
            all_comments = comments.comment_set.all()
            args = {}
            args.update(csrf(request))
            args['all_comments'] = all_comments
            return HttpResponseRedirect('/poems/get/%s' % article_id, args)
        else:
            comments = Article.objects.get(id = article_id)
            all_comments = comments.comment_set.all()
            args = {}
            args.update(csrf(request))
            args['all_comments'] = all_comments
            return HttpResponseRedirect('/poems/get/%s' % article_id, args)
 
# def add(request,article_id):
#     Articles = Article.objects.get(pk=article_id)
#     comments = Comment.objects.all()
#     ban = banWords.objects.all()
#     if request.POST['addcomment'] is None: 
#         print "comment_count"
#     else:
#         added= request.POST['addcomment']
#         com = Comment(content=added, Article_comment_id = Articles)
#         com.save()
#         cont = Articles.comment_set.all().count()
#         Articles.comment_count = cont
#         Articles.save()
#     return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})

def add(request,article_id):
    Articles = Article.objects.get(pk=article_id)
    comments = Comment.objects.all()
    ban = banWords.objects.all()
    added= request.POST['addcomment']
    for word_ban in ban:
        added = added.replace( word_ban.word , ' ***** ')
    if request.POST['addcomment'] is None: 
        print "comment_count"
    else:
        com = Comment(content=added, Article_comment_id = Articles)
        com.save()
        cont = Articles.comment_set.all().count()
        Articles.comment_count = cont
        Articles.save()
    return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})

# def reply(request,article_id,comment_id):
#     Articles = Article.objects.get(pk=article_id)
#     comments = Comment.objects.get(pk=comment_id)
#     comments = Comment.objects.all()
#     added= request.POST['AddReplyComment']
#     com = Comment(content=added, Article_comment_id = Articles,reply=comments)
#     com.save()
#     return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})
# def GetAllArticle(request):
#   Articles = Article.objects.filter(is_publish=1)
#   return render(request,'mysite/articles.html',{'Data': Articles})

def reply(request,article_id,comment_id):
    Articles = Article.objects.get(pk=article_id)
    commens = Comment.objects.get(pk=comment_id)
    comments = Comment.objects.all()
    ban = banWords.objects.all()
    added= request.POST['AddReplyComment']
    for word_ban in ban:
        added = added.replace( word_ban.word , ' ***** ')
    com = Comment(content=added, Article_comment_id = Articles,reply=commens)
    com.save()
    return render(request,'mysite/details.html',{'Articles':Articles,'comments':comments})
# Create your views here.
def home(request):
    return render(request,'mysite/home.html',{'message':'Hello django, ana zeina'})



def marked(request,article_id):
    articles = Article.objects.get(id= article_id) 
    user = get_object_or_404(User,id=request.session['_auth_user_id'])
    # articles = Article.objects.get(id=article_id)
    markadd= mark(User_mark_id=user, Article_mark_id=articles)
    markadd.save()
    return HttpResponse('Article Added successfully')

def unmarked(request,article_id):
    articles = Article.objects.get(id= article_id) 
    user = get_object_or_404(User,id=request.session['_auth_user_id'])
    marks = mark.objects.get(User_mark_id=user, Article_mark_id=articles)
    marks.delete()
    return HttpResponse('Article remove successfully')

def liked(request,comment_id):
    comments = Comment.objects.get(id= comment_id) 
    user = get_object_or_404(User,id=request.session['_auth_user_id'])
    likes = like.objects.get(User_like_id=user, Comment_like_id=comments)
    likes.save()
    return HttpResponse('Article remove successfully')
    
def unliked(request,comment_id):
    comments =Comment.objects.get(id=comment_id) 
    user = get_object_or_404(User,id=request.session['_auth_user_id'])
    likes = like.objects.get(User_like_id=user, Comment_like_id=comments)
    likes.delete()
    return HttpResponse('Article remove successfully')
        