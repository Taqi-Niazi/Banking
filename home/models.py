# from django.db import models

# from wagtail.models import Page


# class HomePage(Page):
#     pass
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

class HomePage(Page):
    balance = models.FloatField(default=0.0)

    content_panels = Page.content_panels + [
        FieldPanel("balance"),
    ]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()

