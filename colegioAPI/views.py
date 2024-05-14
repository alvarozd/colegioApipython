from rest_framework import viewsets
from .serializer import GradoSerializer , PersonaSerializer


from .models import Grado , Persona
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PersonaviewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class login(APIView):
    def post(self, request):
        email = request.query_params.get('email')
        contrasena = request.query_params.get('contrasena')

        if email is None or contrasena is None:
            return Response({'success': False, 'idPersona': None}, status=status.HTTP_400_BAD_REQUEST)

        try:
            persona = Persona.objects.get(correo=email, contrasena=contrasena)
            return Response({'success': True, 'idPersona': persona.idpersona}, status=status.HTTP_200_OK)
        except Persona.DoesNotExist:
            return Response({'success': False, 'idPersona': None}, status=status.HTTP_404_NOT_FOUND)