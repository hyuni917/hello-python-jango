from django.shortcuts import redirect
from .forms import RegisterForm
from django.views.generic import FormView


# Create your views here.
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    # 폼 유효성 검사 실패시
    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    # 폼을 생성할때 어떤 인자값을 전달해서 만들것인지 결정하는 함수
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
