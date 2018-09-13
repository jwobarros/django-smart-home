from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "audio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['house_name'] = 'CASA DOS UNIVERSITÁRIOS'
        return context
