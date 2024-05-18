from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):
    
    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para o passado!')

        # Verificar se já existem 4 reservas para o mesmo dia
        reservas_existentes = Reserva.objects.filter(data=data).count()
        if reservas_existentes >= 4:
            raise forms.ValidationError('Já existem 4 reservas para este dia. Escolha outra data.')
        return data
    
    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 
            'tamanho', 'observacoes'
        ]
