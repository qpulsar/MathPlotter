from django.shortcuts import render
from django.views import View


class MakerView(View):
    def get(self, request):
        return render(request, 'maker.html')
