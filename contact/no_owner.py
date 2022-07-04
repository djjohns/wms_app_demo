from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin


class NoOwnerCreateView(CreateView):
    """
    Sub-class of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    # Saves form instance, sets current object view, and redirects to get_success_url().
    def form_valid(self, form):
        print("form_valid called")
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(NoOwnerCreateView, self).form_valid(form)


class NoOwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Sub-class the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        print("update get_queryset called")
        """ Limit a User to only modifying their own data. """
        qs = super(NoOwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class NoOwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        print("delete get_queryset called")
        qs = super(NoOwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)


# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
