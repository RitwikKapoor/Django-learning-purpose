from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

monthly_challenges = {
    "january": "Work in 1",
    "february": "Work in 2",
    "march": "Work in 3",
    "april": "Work in 4",
    "may": "Work in 5",
    "june": "Work in 6",
    "july": "Work in 7",
    "august": "Work in 8",
    "september": "Work in 9",
    "october": "Work in 10",
    "november": "Work in 11",
    "december": None,
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        # raise Http404() - Set Debug to True in production to use it
