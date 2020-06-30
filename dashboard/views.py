from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    # def get_context_data(self, **kwargs):
    #     context                     =   super(DashboardView, self).get_context_data(**kwargs)
    #     context['unposted_income']  =   IncomeJournal.objects.aggregate(Sum('amount'))
    #     context['unposted_expense'] =   ExpenseJournal.objects.aggregate(Sum('amount'))
    #     context['posted_income']    =   PostedIncome.objects.aggregate(Sum('amount'))
    #     context['posted_expense']   =   PostedExpense.objects.aggregate(Sum('amount'))                
    #     return context
