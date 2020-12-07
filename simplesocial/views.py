from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

#test page view
class TestPage(TemplateView):
    template_name = 'test.html'
#thanks page view
class ThanksPage(TemplateView):
    template_name = 'thanks.html'
#home page view
class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
