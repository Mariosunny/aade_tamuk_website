from django.views.generic import TemplateView

from . import models

class WebsiteView(TemplateView):

    pass


class Home(WebsiteView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context.update({
            "newsposts": models.NewPost.objects.all()
        })

        return context

class Partners(WebsiteView):

    template_name = 'partners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;

class AadeTamuk(WebsiteView):

    template_name = 'aade_tamuk.html'

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

class Officers(WebsiteView):

    template_name = 'officers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context;
