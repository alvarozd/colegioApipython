from rest_framework import serializers
from .models import Grado , Persona

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grado
        fields='__all__'

class PersonaSerializer(serializers.ModelSerializer):
    nombreRol = serializers.ReadOnlyField(source='idrol.nombrerol')
    nombreSexo = serializers.ReadOnlyField(source='idsexo.nombresexo')

    class Meta:
        model = Persona
        fields = ['documento', 'primernombre', 'segundonombre', 'primerapellido', 'segundoapellido', 'nombreRol', 'nombreSexo', 'fotografia', 'telefono', 'correo', 'estado']