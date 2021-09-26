1. install Python tren trang python
2. install jupyter : 
pip install jupyter
3. tao ra 1 moi truong ao moi
python -m venv tenmoitruong
tenmoitruong\scripts\activate.bat (active tren window)
cd thumucchua requirements cai dat 
pip install -r requrements.txt va thuong chua file jupyter
jupyter notebook
4. deactive (thoat)
5. Python tenfile.py (Cd toi thu muc chua file tenfile.py nay da)
6. Deploy app github - azure
https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask
git clone https://github.com/Azure-Samples/python-docs-hello-world 
cd python-docs-hello-world
az  webapp up --sku B1 --name nguyentrongluan-bike-rental(ten Appserivce)
https://(ten Appserivce).azurewebsites.net
7. Xoa 1 thu muc trong linux https://vi.joecomp.com/how-remove-directory-linux
8. Deploy tu github sang Azure 
https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask
9. Autodepployment CICD
https://github.blog/2015-09-15-automating-code-deployment-with-github-and-azure/
10. sau khi sua code thi go lenh az webapp up de restart lai service


Django
1. vao venv
2. cd toi thu muc chua project (co file manage.py)
python manage.py runserver de chay
3. tao 1 project moi:  django-admin startproject tenproject
tao 1 app moi trong project 
To create your app, make sure you’re in the same directory as manage.py and type this command: python manage.py startapp tenapp
4. Voi app moi tao:
- sua views.py de thiet lap hien thi, cac viec muon lam gi do
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
- them urls:
+ o app moi tao. tao them file urls.py 
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
+ o file urls cua Project 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), #polls la tenpp
    path('admin/', admin.site.urls),
]
5. Tao bang chay database:
python manage.py migrate 
Luu y phai khai bao app trong setting.py phan installed app
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .schema (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.
5. Make models change
We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.

Models : read/write data la o models.py nay
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
INSTALLED_APPS = [
    'polls.apps.PollsConfig',#khai bao app Polls o day
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] 
  chay lenh python manage.py makemigrations polls  de khai bao models(migrate database) //Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.
  Chay lenh Mygrate lai de update database python manage.py migrate
  
6. create admin
python manage.py createsuperuser
7. De add them cac bang (trong models.py) co the modify o trang admin
chen them file tenapp/admin.py
from django.contrib import admin

from .models import Question  #Question la 1 bang trong models cua app

admin.site.register(Question)

8. Thiet ke chi tiet views cho tung app
a.File tenapp/views.py

from .models import Question# khong import thi khong tuong tac duoc voi co so du lieu o duoi


from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
b.File tenapp/urls.py  luon phai sua ca cap views va urls
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
c. them template
Them thu muc templates trong APP. Sau do lai tao them 1 thu muc con tenapp trong thu muc templates, thu muc nay se gom cac file nhu index.html...
edit template vd: file index.html 
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

Note