from cars.forms import CallbackForm
from rent.forms import  ReturnCarForm


class CallbackMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['forma']= CallbackForm()
        return context


