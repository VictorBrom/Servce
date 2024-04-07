from django.shortcuts import render
from .models import Partners, Contracts
from .forms import PartnersForms, ContractsForms
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
def partners_index(request):
    partners = Partners.objects.all()
    form = PartnersForms()
    return render(request, 'partners/partners.html', {'partners': partners, 'form': form})


def contract_index(request, id_partner):
    contract = Contracts.objects.filter(partner=id_partner)
    return render(request, 'partners/contracts.html', {'contract': contract})



class PartnerContracts(View):
    def get(self, request):
        form = ContractsForms()
        return render(request, 'partners/create_contracts.html', {'form': form})

    def post(self, request):
        form = ContractsForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        return render(request, 'partners/create_contracts.html', {'form': form})



class PartnerIndex(View):
    def get(self, request):
        form = PartnersForms()
        return render(request, 'partners/create_partner.html', {'form': form})

    def post(self, request):
        form = PartnersForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        return render(request, 'partners/create_partner.html', {'form': form})