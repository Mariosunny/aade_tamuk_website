from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from . import models
from . import forms

CONTACT_EMAIL = "tyler.hurson@students.tamuk.edu"
SENDER_EMAIL = "glassplotful@gmail.com"


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

        slides = []

        for slide in models.Slide.objects.all().order_by("position"):

            slides.append({
                "title": slide.title,
                "body": slide.body,
                "img": slide.image.url,
                "url": slide.link,
                })

        context.update({"slides": slides})

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

def contact_us(request):

    form = forms.ContactUsForm()

    if request.method == 'POST':

        form = forms.ContactUsForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data.get('name')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')

            send_mail(
                "Thank you for contacting AADE-TAMUK",
                "Thank you for contacting AADE-TAMUK. We will respond to your message as soon as possible.\n\nYour original message:\n\n" + message +
                "\n\nTyler Hurson\nAADE-TAMUK Webmaster",
                CONTACT_EMAIL,
                [email],
            )

            send_mail(
                "AADE: " + name + " has contacted us",
                name + " has contacted the AADE using our website's Contact Us form.\n\nTheir email:\n\n" + 
                email + "\n\nTheir message:\n\n" + message,
                SENDER_EMAIL,
                [CONTACT_EMAIL],
            )

            return render(request, 'contactUs.html', {"form": forms.ContactUsForm(), "submitted": True})

    return render(request, 'contactUs.html', {"form": form})


class Leadership(WebsiteView):

    template_name = 'leadership.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;


class Calendar(WebsiteView):

    template_name = 'calendar.html'

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

class MeetingsGallery(WebsiteView):
    template_name = 'meetings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = models.Album.objects.filter(category=1)

        pictures = models.Picture.objects.filter(album__in=albums).order_by("album")
        context.update({
            "pictures": [{
                "album": picture.album,
                "image": picture.image,
                "caption": picture.caption
            } for picture in pictures],
            "albums": [{
                "name": album.name
            } for album in albums]
        })

        return context

class Album(WebsiteView):
    template_name = 'album.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = self.request.GET.get('album')
        pictures = models.Picture.objects.filter(album__name=a)
        print(len(pictures))
        context.update({
            "pictures": [{
                "album": picture.album,
                "image": picture.image,
                "caption": picture.caption
            } for picture in pictures]
        })

        return context
