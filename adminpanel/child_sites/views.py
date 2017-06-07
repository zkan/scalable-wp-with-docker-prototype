from django.shortcuts import render
from django.views.generic import TemplateView


class ChildSiteAddView(TemplateView):
    template = 'index.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
