from django.shortcuts import render, get_object_or_404, redirect
from .models import HomePage
from wagtail.models import Page
from django.http import JsonResponse


def banking_dashboard(request):
    account = HomePage.objects.first()

    # If no UserAccount exists, create one properly inside the page tree
    if account is None:
        # Get the homepage to add the UserAccount under it
        home_page = Page.objects.get(title="Home")

        # Create and add UserAccount under Home
        account = HomePage(title="Bank Account")
        home_page.add_child(instance=account)
        account.save_revision().publish()  # Publish the page

    return render(request, "home/banking.html", {"balance": account.balance})

def check_balance(request):
    account = HomePage.objects.first()
    return render(request, "home/balance.html", {"balance": account.balance})

def deposit(request):
    if request.method == "POST":
        amount = float(request.POST.get("amount", 0))
        account = HomePage.objects.first()
        account.deposit(amount)
        return redirect("banking_home")
    return render(request, "home/deposit.html")

def withdraw(request):
    if request.method == "POST":
        amount = float(request.POST.get("amount", 0))

        # Ensure there's at least one HomePage object
        homepage, created = HomePage.objects.get_or_create(title="Bank Account", defaults={"balance": 0.0})

        if 0 < amount <= homepage.balance:
            homepage.withdraw(amount)
            return redirect("banking_home")
        else:
            return render(request, "home/withdraw.html", {"error": "Invalid amount or insufficient balance"})

    return render(request, "home/withdraw.html")


