from django.shortcuts import render
from manager.models import Skill, About, Project, Contact


def home(request):
    projects = Project.objects.all()

    android = 0
    ios = 0
    web = 0

    for p in projects:
        if p.category == "android and ios":
            android += 1
            ios += 1
        elif p.category == "ios":
            android += 1
        elif p.category == "ios":
            android += 1
        else:
            web += 1

    params = {
        'android': android,
        'ios': ios,
        'web': web,
    }
    if request.method == 'POST':
        post_request(request)
    return render(request, 'home.html', params)


def project(request):
    projects = Project.objects.all()
    params = {
        'projects': projects
    }
    if request.method == 'POST':
        post_request(request)
    return render(request, 'project.html', params)


def about(request):
    skills = Skill.objects.all()
    about_details = About.objects.all()
    params = {
        'abouts': about_details,
        'skills': skills,
    }
    if request.method == 'POST':
        post_request(request)
    return render(request, 'about.html', params)


def contact(request):
    if request.method == 'POST':
        post_request(request)

    return render(request, 'contact.html')


# common methods
def post_request(request):
    name = request.POST['name']
    phone_number = request.POST['phone_number']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    person = Contact(name=name, phone_number=phone_number, email=email, subject=subject, message=message)
    person.save()
