from django.shortcuts import redirect
from .forms import RegisterForm
from django.views.generic import FormView, ListView
from .models import Order
from django.utils.decorators import method_decorator
from user.decorators import login_required


# Create your views here.
@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__email=self.request.session.get('user'))
        return queryset
