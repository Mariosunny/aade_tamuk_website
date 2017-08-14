from django.views.generic import TemplateView

from . import models

class WebsiteView(TemplateView):

    pass


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

        return context;


class News(WebsiteView):

    template_name = 'news.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        newsposts = models.NewsPost.objects.all().order_by("-date")

        print(self.kwargs)

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
