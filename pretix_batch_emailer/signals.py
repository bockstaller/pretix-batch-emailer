from distutils.util import strtobool
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from pretix import settings
from pretix.control.signals import html_page_start, nav_topbar, html_head
from pretix_batch_emailer.forms import CollectBulkOrdersForm
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.templatetags.static import static
from pretix_batch_emailer.views import CollectOrders


@receiver(nav_topbar, dispatch_uid="pretix_batch_emailer")
def nav_topbar_f(sender, request=None, **kwargs):
    return [
        {
            "label": _("Email visible orders"),
            "url": "#batch-emailer",
        }
    ]


@receiver(html_page_start, dispatch_uid="pretix_eventparts")
def order_eventpart_selection_public(sender, **kwargs):
    x = CollectOrders().get(sender)
    return x


@receiver(html_head, dispatch_uid="pretix_eventparts")
def batch_emailer_script(sender, **kwargs):
    url = static("pretix_batch_emailer/batch-emailer.js")
    return f"<script src='{url}'> </script>"
