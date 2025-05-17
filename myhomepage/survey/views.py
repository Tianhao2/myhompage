from django.shortcuts import render, redirect
from .models import SurveyResponse
from django.utils.timezone import now


def survey_form(request, category):
    if request.method == 'POST':
        SurveyResponse.objects.create(
            category=category,
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            q1=request.POST.get('q1', ''),
            q2=request.POST.get('q2', ''),
            q3=request.POST.get('q3', ''),
            q4=request.POST.get('q4', ''),
            q5=request.POST.get('q5', ''),
            q6=request.POST.get('q6', ''),
            q7=request.POST.get('q7', ''),
            q8=request.POST.get('q8', ''),
            q9=request.POST.get('q9', ''),
            q10=request.POST.get('q10', ''),
            created_at=now()
        )
        return redirect(f'/survey/{category}/thankyou/')

    return render(request, 'survey/form.html', {'category': category})


def survey_thankyou(request, category):
    return render(request, 'survey/thankyou.html', {'category': category})
