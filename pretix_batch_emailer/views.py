from django.views.generic import FormView
from pretix.control.permissions import EventPermissionRequiredMixin
from pretix_batch_emailer.forms import CollectBulkOrdersForm
from django.http import (
    HttpResponseRedirect,
)
from django.template.loader import render_to_string


class CollectOrders(EventPermissionRequiredMixin, FormView):
    form_class = CollectBulkOrdersForm
    template_name = "pretix_batch_emailer/collect_bulk_orders.html"
    permission = "can_view_orders"

    def get(self, request, *args, **kwargs):
        form = CollectBulkOrdersForm()
        return render_to_string(
            "pretix_batch_emailer/collect_bulk_orders.html",
            {
                "form": CollectBulkOrdersForm,
                "organizer": request.event.organizer,
                "event": request.event,
            },
            request=request,
        )

    def get_success_url(self) -> str:
        print("success")
        return ""

    def form_invalid(self, form):
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))
