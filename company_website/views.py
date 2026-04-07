from django.shortcuts import render
from django.views.generic import TemplateView


def cw_home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for visiting our company!",
    }
    return render(request, "cw_home.html", context=context)


class AboutPageView(TemplateView):
    template_name = "cw_about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main St, Anytown, USA"
        context["phone_number"] = "555-555-5555"
        return context
