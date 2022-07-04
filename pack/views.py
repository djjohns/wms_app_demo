from pack.models import Pack
from pack.owner import (
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


class PackOrderView(OwnerCreateView):
    model = Pack
    fields = ["order_number"]


class PackUpdateView(OwnerUpdateView):
    model = Pack
    fields = ["order_number"]


class PackDeleteView(OwnerDeleteView):
    model = Pack
