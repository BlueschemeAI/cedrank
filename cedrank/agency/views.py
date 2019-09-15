from django.shortcuts import render, redirect
from agency.forms import DebtorsAddForm, CreditorsAddForm
from agency.models import Debtors, Creditors
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def debtors(request):
    debtors_form = DebtorsAddForm()
    if request.method == 'POST':
        debtors_form = DebtorsAddForm(request.POST, request.FILES)
        if debtors_form.is_valid():
            debtors = debtors_form.save(commit=False)
            debtors.save()
            debtors_form = DebtorsAddForm()
            return redirect('debtors')
        else:
            messages.error(request, f'Can not able to add debtors')
            return redirect('debtors')

    debtors_form = DebtorsAddForm()
    return render(request,'debtors.html', { 'debtors': Debtors.objects.all(), 'creditors': Creditors.objects.all() })


def updateDebtors(request, id):
    updateDebtor = Debtors.objects.get(id=id)
    form = DebtorsAddForm(request.POST, instance=updateDebtor)
    if form.is_valid():
        form.save()
        form = DebtorsAddForm()
        return redirect("debtors")
    return render(request, 'debtors.html', { 'debtors': Debtors.objects.all() })


def creditors(request):
    creditors_form = CreditorsAddForm()
    if request.method == 'POST':
        creditors_form = CreditorsAddForm(request.POST, request.FILES)
        if creditors_form.is_valid():
            creditors = creditors_form.save(commit=False)
            #creditors.document = request.FILES['document']
            creditors.save()
            subject = 'Added as Creditors'
            message = ' Hi \n You have been added as Creditors'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [creditors.email]
            send_mail(subject, message, email_from, recipient_list)

            #messages.error(request, f'Your account has been created. Please login.')
            return render(request,'creditors.html', { 'creditors':Creditors.objects.all() })
        else:
            messages.error(request, f'Can not able to add creditors')
            return redirect('creditors')
    else:
        creditors_form = CreditorsAddForm()
    return render(request,'creditors.html', { 'creditors':Creditors.objects.all() })
