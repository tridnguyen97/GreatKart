from django.contrib.auth.views import LoginView
from vendors.forms import VendorAuthenticationForm

class SignInView(LoginView):
    ''' Sign in for vendor '''
    form_class = VendorAuthenticationForm
    template_name = 'vendor/sign_in.html'

    def get_success_url(self):
        if self.request.user.is_authenticated and self.request.user.is_vendor:
            return 'vendor:vendor_root'