from rest_framework import serializers
from .models import Invoice, Local
from django.urls import reverse

class InvoiceSerializer(serializers.ModelSerializer):
    #path = serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = '__all__'

    def get_queryset(self):
        return Ingrediente.objects.all()
        
    def get_path(self, ingrediente):
        return 'https://tarea02taller.herokuapp.com{}'.format(reverse('ingrediente-details', args=[ingrediente.id]))


"""class IngredienteSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    class Meta:
        model = Ingrediente
        #url = serializers.HyperlinkedIdentityField(view_name = 'Ingredient')
        fields = ['path']
        
    def get_queryset(self):
        return Ingrediente.objects.all()
        
    def get_path(self, ingrediente):
        return 'https://tarea02taller.herokuapp.com{}'.format(reverse('ingrediente-details', args=[ingrediente.id]))

class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        #url = serializers.HyperlinkedIdentityField(view_name='Burger')
        fields = ['id','nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']

    def get_queryset(self):
        return Hamburguesa.objects.all()"""