import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    """View to handle dashboard."""

    template_name = "dashboard/dashboard.html"

    def get(self, request, *args, **kwargs):
        match request.GET.get("data"):
            case "county":
                with open(
                    os.path.join(
                        settings.BASE_DIR,
                        "sigipo",
                        "static",
                        "json",
                        "cu-all.topo.json",
                    )
                ) as file:
                    file = json.load(file)
                return JsonResponse(data=file)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
