# Create your views here.
from django.views.generic import View
from django.shortcuts import render
from analyze.views import Analyze, states_list, dates_list

class Compare(View):
    
    template_name = "compare.html"
    
    def get(self, request):
        analyze_obj = Analyze()
        records_dict = analyze_obj.get_stored_data()
        
        return render(request, self.template_name, {'states_list':states_list,'records_dict':records_dict,'dates_list':dates_list,'dates_count':len(dates_list)})