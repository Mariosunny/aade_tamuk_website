from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render


from . import models
from . import forms

class WebsiteView(TemplateView):

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class Home(WebsiteView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        newsposts = models.NewsPost.objects.all().order_by("-date")

        if len(newsposts) > 5:

            newsposts = newsposts[:5]

        context.update({
            "newsposts": [{
                "title": newspost.title,
                "date": newspost.date,
                "content": newspost.content[:500] + "..." if len(newspost.content) > 500 else newspost.content,
                "read_more": len(newspost.content) > 500,
                "pk": newspost.pk,
            } for newspost in newsposts]
        })

        events = []

        for event in models.Event.objects.all().order_by("-date"):

            e = {
                "title": event.title,
                "date": event.date,
                "details": event.details[:250] + "..." if len(event.details) > 250 else event.details,
                "pk": event.pk,
                "read_more": len(event.details) > 250,
            }

            if event.location:

                e.update({
                    "location": event.location,
                    })

            events.append(e)

        context.update({
            "events": events,
            })

        return context

class Partners(WebsiteView):

    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class AboutUs(WebsiteView):

    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class AadeCentralTexas(WebsiteView):

    template_name = 'aade_central_texas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class Donations(WebsiteView):

    template_name = 'donations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class ContactUs(WebsiteView):

    template_name = 'contactUs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class Leadership(WebsiteView):

    template_name = 'leadership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;


class Events(WebsiteView):

    template_name = 'events.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        events = []

        for event in models.Event.objects.all().order_by("-date"):

            e = {
                "title": event.title,
                "date": event.date,
                "details": event.details,
                "pk": event.pk,
            }

            if event.location:

                e.update({
                    "location": event.location,
                    })

            events.append(e)

        context.update({
            "events": events,
            })

        return context;


class News(WebsiteView):

    template_name = 'news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        newsposts = models.NewsPost.objects.all().order_by("-date")

        context.update({
            "newsposts": [{
                "title": newspost.title,
                "date": newspost.date,
                "content": newspost.content,
                "pk": newspost.pk,
                "selected": self.kwargs['selected'] if 'selected' in self.kwargs else -1
            } for newspost in newsposts]
        })

        return context;


def admin_login(request):

    form = forms.AdminLoginForm()

    if request.method == 'POST':

        form = forms.AdminLoginForm(request.POST)

        if form.is_valid():

            login(request, authenticate(username="admin",password=form.get_password()))
            return HttpResponseRedirect('/')

    return render(request, 'admin_login.html', {"form": form})


def admin_logout(request):

    logout(request)
    return HttpResponseRedirect('/')


def create_newspost(request):

    form = forms.CreateNewspostForm()

    if request.method == 'POST':

        form = forms.CreateNewspostForm(request.POST)

        if form.is_valid():

            models.NewsPost.objects.create(
                title=form.get_title(),
                content=form.get_content(),
                )
            return HttpResponseRedirect('/news')

    return render(request, 'create_newspost.html', {"form": form})



def delete_newspost(request, pk):

    models.NewsPost.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/news')