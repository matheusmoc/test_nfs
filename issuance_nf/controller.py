from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import NotaFiscal
from .forms import NotaFiscalForm


class IssuanceIndexView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(IssuanceIndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, pk=None):
        data = NotaFiscal.objects.all()
        context = {'data': data}
        return render(request, 'index.html', context=context)

class IssuanceCreateView(View):
    def get(self, request):
        return render(request, 'create.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_emissao = request.POST.get('data_emissao')

        nota_fiscal = NotaFiscal.objects.create(nome=nome, email=email, telefone=telefone, data_emissao=data_emissao)
        return redirect('nfs_detail', pk=nota_fiscal.pk)


class IssuanceDeleteView(View):
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk')
        nota_fiscal = NotaFiscal.objects.all()
        nota_fiscal.delete()
        return redirect('/nfs')
        
class IssuanceEditView(View):
    def get(self, request, pk):
        nota_fiscal = get_object_or_404(NotaFiscal, pk=pk)
        form = NotaFiscalForm(instance=nota_fiscal)
        return render(request, 'edit.html', {'form': form})
    
    def post(self, request, pk):
        nota_fiscal = get_object_or_404(NotaFiscal, pk=pk)
        form = NotaFiscalForm(request.POST, instance=nota_fiscal)
        if form.is_valid():
            form.save()
            return redirect('edit', pk=pk)
        return render(request, 'edit.html', {'form': form})