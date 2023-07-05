from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse

def get_completion(prompt):
    print(prompt)
    query = f"for '{prompt}': this is a sample response yooo"
    return query

def planner(request):
    return render(request, 'main.html')


def planner_chat(request):
    prompt = request.POST.get('prompt')
    response = get_completion(prompt)
    return JsonResponse({'response': response})