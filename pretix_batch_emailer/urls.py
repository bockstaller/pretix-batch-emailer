from django.conf.urls import url

from pretix_batch_emailer.views import CollectOrders

urlpatterns = [
    url(
        r"^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/batch_emailer/orders",
        CollectOrders.as_view(),
        name="collect_orders",
    ),
]
