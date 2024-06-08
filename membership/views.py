from rest_framework import generics
from .serializers import MemberSerializer
from .models import Member

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class MemberListCreateView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    model = Member
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        member = serializer.save()
        refresh = RefreshToken.for_user(member)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data)
    
class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    model = Member

