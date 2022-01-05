#-this is a python function, for the category dropdown to work
#-import this to  garment setting.py
from .models import Category 

def menu_links(request):
   links = Category.objects.all()
   return dict(links=links)