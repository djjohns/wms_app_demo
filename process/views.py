from process.models import Process
from process.owner import (
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


class ProcessOrderView(OwnerCreateView):
    model = Process
    fields = ["order_number", "upc", "weight"]


class ProcessUpdateView(OwnerUpdateView):
    model = Process
    fields = ["order_number"]


class ProcessDeleteView(OwnerDeleteView):
    model = Process
