# Create your views here.
from django.views.generic import View
from django.shortcuts import render
from recognize.models import Catagory, Member

class Recognize(View):
    
    ''' recognize page which shows all members and catagory hierarchy'''

    template_name = "recognize1.html"
    
    def get(self, request):
        members_list = Member.objects.all().order_by('?')
        catagories = Catagory.objects.all()
        return render(request, self.template_name, {"members_list":members_list,"catagories":catagories})


# Create your views here.
