from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
    DeleteView,
    FormView,
)
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


from .models import Event
from .forms import EventHostForm, JoinForm


User = get_user_model()


class EventList(ListView):
    model = Event
    context_object_name = "events"


class EventHost(CreateView):
    model = Event
    form_class = EventHostForm
    success_url = "/hosted"  # TODO: Use reverse

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user, _ = User.objects.get_or_create(email=email, username=email)
        event = form.instance
        event.host = user
        event.save()
        return super().form_valid(form)


class EventHostSuccess(TemplateView):
    template_name = "circles/success.html"


class EventDeleteView(DeleteView):
    """Allows the host to delete the event. Secret Link"""

    # TODO: This is only an idea
    model = Event


class EventJoin(FormView):
    """Asks user for mail. Sends mail with details for event"""

    template_name = "circles/join_form.html"
    success_url = "/joined"  # TODO

    form_class = JoinForm

    def get_context_data(self, **kwargs):
        event = get_object_or_404(Event, pk=self.kwargs["id"])
        # TODO: Check if event is in the past
        # TODO: Check if event is full
        data = super().get_context_data(**kwargs)
        data["event"] = event
        return data

    def form_valid(self, form):
        event = Event.objects.get(pk=self.kwargs["id"])
        email = form.cleaned_data["email"]
        user, _ = User.objects.get_or_create(email=email, username=email)
        event.participants.add(user)
        # TODO: Send mail
        return super().form_valid(form)