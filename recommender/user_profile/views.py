from allauth.account.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CustomLogout(LogoutView):
    template_name = "accounts/logout.html"


class ProfileView(TemplateView):
    model = User
    context_object_name = "user"
    template_name = "accounts/profile.html"

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.request.user.username
        context = super().get_context_data(**kwargs)
        query = User.objects.prefetch_related("watch_list", "comments").get(username=user)
        watch_list = query.watch_list.all()
        comments = query.comments.all()
        context["watch_list"] = watch_list
        context["comments"] = comments
        return context
