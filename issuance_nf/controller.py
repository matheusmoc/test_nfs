from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Emissor


class IssuanceViewIndex(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(IssuanceViewIndex, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk=None):
        data = Emissor.objects.all()
        context = {'data': data}
        return render(request, 'index.html', context=context)

class IssuanceViewIndexCreate(View):
    def get(self, request):
        return render(request, 'create.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_emissao = request.POST.get('data_emissao')

        emissor = Emissor.objects.create(nome=nome, email=email, telefone=telefone, data_emissao=data_emissao)
        return redirect('nfs_detail', pk=emissor.pk)


class IssuanceViewIndexDelete(View):
    def delete(self, request, pk):
        emissor = get_object_or_404(Emissor, pk=pk)
        emissor.delete()
        return HttpResponse("Emissor deletado com sucesso!")

class IssuanceViewIndexUpdate(View):
    def get(self, request):
        return render(request, 'update.html')
    
    def put(self, request, pk):
        emissor = get_object_or_404(Emissor, pk=pk)
        emissor.nome = request.POST.get('nome')
        emissor.email = request.POST.get('email')
        emissor.telefone = request.POST.get('telefone')
        emissor.data_emissao = request.POST.get('data_emissao')
        emissor.save()
        return HttpResponse("Emissor atualizado com sucesso!")
