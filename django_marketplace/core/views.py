from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
        },
    )


def contact(request):
    return render(request, "core/contact.html")
def about(request):
    return render(request, "core/about.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            # Redirect to the login page upon successful signup
            return redirect('/login/')  # Use the URL name instead of "/login/"

    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form,})
