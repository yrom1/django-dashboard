from django.shortcuts import render

# from .models import Team


def dashboard(request):
    # list_teams = Team.objects.filter(team_level__exact="U09") # it's inspecting into the varname 🤯
    context = {'title': 'dashboard'}
    return render(request, 'template.html', context) # makes HttpResponse

def projects(request):
    # list_teams = Team.objects.filter(team_level__exact="U09") # it's inspecting into the varname 🤯
    context = {'title': 'projects'}
    return render(request, 'template.html', context) # makes HttpResponse

def home(request):
    # list_teams = Team.objects.filter(team_level__exact="U09") # it's inspecting into the varname 🤯
    context = {'title': 'Ryan'}
    return render(request, 'template.html', context) # makes HttpResponse
