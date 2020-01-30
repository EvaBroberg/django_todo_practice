from django.shortcuts import render, HttpResponse
from .models import Item

def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html",{'items': results})

def create_an_item(request):
    return render(request, "item_form.html")
    