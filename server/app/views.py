from django.views.generic import TemplateView

from . import models

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


class AdminLogin(WebsiteView):

    template_name = 'admin_login.html'

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
