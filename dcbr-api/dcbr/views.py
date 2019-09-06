from django.http import HttpResponseRedirect
from django.urls import reverse


def authenticate(request):
    # return render(request, "authenticate.html")
    return HttpResponseRedirect(reverse("oidc_authentication_init"))
