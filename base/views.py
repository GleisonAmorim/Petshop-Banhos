from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm
from base.models import Contato, Reserva



def inicio(request):
    return render(request, 'inicio.html')

'''def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
            sucesso = True
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
    resposta = {
        'telefone': '(16) 9999-9999',
        'responsavel': 'Maria Silva',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', resposta)'''

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    resposta = {
        'telefone': '(16) 9999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', resposta)
        

def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    resposta = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', resposta)

# Função para renderizar a página do blog com posts fictícios
def blog(request):
    # Lista de posts fictícia para demonstração
    posts = [
        {
            'titulo': 'Cuide da saúde bucal do seu pet',

            'conteudo':'Na Happy Pet, oferecemos os melhores produtos e acessórios para cuidar da saúde bucal do seu animal de estimação. Venha até nossa loja conferir nossa seleção de escovas de dentes, brinquedos dentais, alimentos específicos para saúde bucal e muito mais!',
       
            
        },
        {
            'titulo': 'Passeio no parque',
            'conteudo': 'Na Happy Pet, temos os melhores acessórios para tornar esses passeios ainda mais agradáveis. Venha até nossa loja  conferir nossa seleção de coleiras confortáveis, guias resistentes, brinquedos interativos e muito mais para garantir que seu pet tenha a melhor experiência possível no parque!',

        
            
        },
        {
            'titulo': 'Alimentação saudável',
            'conteudo': 'Na Happy Pet, oferecemos os melhores produtos de alimentação para seu pet. Venha até nossa loja conferir nossa seleção de rações, snacks e alimentos naturais para garantir a saúde e a felicidade do seu companheiro.',

        },
    ]
    
    return render(request, 'blog.html', {'posts': posts})
