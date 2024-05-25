from django.shortcuts import render,redirect
from .models import Transaction
from books.models import Book
from .forms import DepositForm, TransactionForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from .constants import DEPOSIT,RETURN
from django.contrib import messages
from django.views.generic import CreateView, ListView

# Create your views here.


def send_transaction_email(user, amount, subject, template, receiver=None):
    message = render_to_string(
        template, {"user": user, "amount": amount, "receiver": receiver}
    )
    send_email = EmailMultiAlternatives(subject, "", to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = "transaction/transaction_form.html"
    model = Transaction
    title = ""
    success_url = reverse_lazy("profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )  # template e context data pass kora
        context.update({"title": self.title})

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"

    def get_initial(self):
        initial = {"transaction_type": DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        # if not account.initial_deposit_date:
        #     now = timezone.now()
        #     account.initial_deposit_date = now
        account.balance += (
            amount  # amount = 200, tar ager balance = 0 taka new balance = 0+200 = 200
        )
        account.save(update_fields=["balance"])

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully',
        )
        send_transaction_email(
            self.request.user,
            amount,
            "Deposit Message",
            "transaction/deposit_email.html",
        )
        return super().form_valid(form)


# class Transaction(models.Model):
#     account = models.ForeignKey(
#         UserAccount, related_name="transactions", on_delete=models.CASCADE
#     )

#     amount = models.DecimalField(decimal_places=2, max_digits=12)
#     balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
#     transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["timestamp"]


def return_book(request,id):
    book = Book.objects.get(pk=id)
    amount = book.price

    request.user.account.balance += amount

    Transaction.objects.create(
        account=request.user.account,
        amount=amount,
        balance_after_transaction=request.user.account.balance,
        transaction_type =RETURN
    )

    messages.success(
        request,
        f'{"{:,.2f}".format(float(amount))}$ was returned to your account successfully',
    )
    send_transaction_email(
        request.user,
        request.user.account.amount,
        "Book Return Message",
        "transaction/return_book_email.html",
    )

    return redirect("home")
