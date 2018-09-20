from django.views.generic.base import TemplateView

from assistant.models import Room, RadioFrequencyRelay

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['house_name'] = 'Home Assistant'
        context['rooms'] = Room.objects.all().order_by("name")

        return context
