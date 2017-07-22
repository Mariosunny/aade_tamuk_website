from django.views.generic import TemplateView

class WebsiteView(TemplateView):

    pass


class Home(WebsiteView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


