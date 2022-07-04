from verify.models import Verify
from verify.owner import (
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


class VerifyProductView(OwnerCreateView):
    model = Verify
    fields = [
        "order_number",
        "customer_number",
        "upc",
        "weight",
        "qty",
        "warehouse",
        "location",
    ]


class VerifyUpdateView(OwnerUpdateView):
    model = Verify
    fields = ["customer_number"]


class VerifyDeleteView(OwnerDeleteView):
    model = Verify
