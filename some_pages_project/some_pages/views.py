from django.views.generic import TemplateView

class RecepiesPageView(TemplateView):
    template_name = 'recepies.html'
class VanillaCakePageView(TemplateView):
    template_name = 'vanilla-biscuit.html'
class ChocolateCakePageView(TemplateView):
    template_name = 'chocolate-biscuit.html'
class RedVelvetCakePageView(TemplateView):
    template_name = 'red-velvet-cake.html'
class CreamCheesePageView(TemplateView):
    template_name = 'base-cream-cheese.html'