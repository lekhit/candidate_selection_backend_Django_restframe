from rest_framework import generics 
# Create your views here.

from person.models import Person
from person.serializer import PersonSerializer,StatusSerializer

class StatusUpdateAPIView(generics.UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=StatusSerializer
    lookup_field='pk'

Status_Update=StatusUpdateAPIView.as_view()

class ResumeUpdateAPIView(generics.UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=StatusSerializer
    lookup_field='pk'
    
Resume_Update=ResumeUpdateAPIView.as_view()
class PersonDetailAPIView(generics.RetrieveAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

Person_Detail=PersonDetailAPIView.as_view()

class PersonCreateAPIView(generics.CreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer


Person_Create_Detail=PersonCreateAPIView.as_view()

class PersonListAPIView(generics.ListAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer

Person_List_Detail=PersonListAPIView.as_view()

class PersonUpdateAPIView(generics.UpdateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='pk'

Person_Update_Detail=PersonUpdateAPIView.as_view()

class PersonDeleteAPIView(generics.DestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='pk'
    
Person_Delete_Detail=PersonDeleteAPIView.as_view()