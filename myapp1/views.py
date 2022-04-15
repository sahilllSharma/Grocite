from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import OrderItemForm, InterestForm
from .models import Type, Item, Client
# Create your views here.
# def index(request):
#     item_list = Item.objects.all().order_by('-price')[:7]
#     response = HttpResponse()
#     heading1 = '<p>' + 'Different Types: ' + '</p>'
#     response.write(heading1)
#     for item in item_list:
#      para = '<p>'+ str(item.price) + ': ' + str(item) + '</p>'
#      response.write(para)
#     client_list= Client.objects.all()
#     return response

def about(request):
    return render(request, 'myapp1/about0.html')
    # No, we are not passing any variables because we will not be using any object to render the data.

# def detail(request, type_no):
#     typeId = get_object_or_404(Type, pk=type_no)
#     # type_with_id = Type.objects.get(id=type_no)
#     itemsType = Item.objects.filter(type=typeId)
#     response = HttpResponse()
#     headingTitle = '<p>' + 'Items having type ' + str(typeId) + '</p>'
#     response.write(headingTitle)
#     for item in itemsType:
#         textLine1 = '<p>' + str(item.price) + ': ' + str(item) + '</p>'
#         response.write(textLine1)
#     return response
def detail(request, type_no):
    typeId = get_object_or_404(Type, pk=type_no)
    itemsType = Item.objects.filter(type=typeId)
    return render(request, 'myapp1/detail0.html', {'typeId': typeId,'itemsType' : itemsType })
    # Yes, we need to pass context variable since we need to display all the items with particular type

def test(request):
    return redirect('about/')

def itemdetail(request, item_id):
    item = Item.objects.get(id=item_id)
    msg = ''
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            msg = 'Your interest is "{}" in item "{}" with quantity "{}" and comments "{}"'
            interest = form.cleaned_data['interested']
            quantity = form.cleaned_data['quantity']
            comments = form.cleaned_data['comments']
            msg = msg.format(interest, item.name, quantity, comments)
    else:
        form = InterestForm()
    return render(request, 'myApp1/itemdetail.html', {'form': form, 'item': item, 'msg': msg})

def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    return render(request, 'myapp1/index0.html', {'type_list': type_list})
    # Yes we are passing type_list as a context variable because we want to render the list of all types on the home page

def items(request):
		itemlist = Item.objects.all().order_by('id')[:20]
		return render(request, 'myapp1/items.html', {'itemlist': itemlist})

def placeorder(request):
    msg = ''
    itemlist = Item.objects.all()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.items_ordered <= order.item.stock:
                order.save()
                msg = 'Your order has been placed successfully.'
                order.item.stock -= order.items_ordered
                order.item.save()
            else:
                msg = 'We do not have sufficient stock to fill your order.'
            return render(request, 'myapp1/order_response.html', {'msg': msg})
    else:
        form = OrderItemForm()
    return render(request, 'myapp1/placeorder.html', {'form': form, 'msg': msg, 'itemlist': itemlist})


