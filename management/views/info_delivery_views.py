import json
from xmlrpc.client import Transport
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from seller.views import constants

from management.models import order_product, order

class DeliveryView(LoginRequiredMixin, View):
    '''
    판매관리/택배배송
    '''
    template_name='delivery_info.html'

    def get(self, request: HttpRequest):
        context={}

        if request.user.is_staff:
            context['staff'] = True
        if request.user.groups.filter(name='seller').exists():
            context['seller'] = True
        
        return render(request, self.template_name, context)

    def put(self, request: HttpRequest):
        context={}
        request.PUT = json.loads(request.body)

        Id = request.PUT.get('id')
        Transport_no = request.PUT.get('transport_no')

        # Update order status 
        order.objects.filter(id=Id).update(
            status=constants.PROCESSING,
            transport_no = Transport_no,
        )

        # Update order-product status of the order
        product_ids=order_product.objects.filter(order_id=Id).values_list('id', flat=True)
        for id in product_ids:
            order_product.objects.filter(id=id).update(
                status=constants.PROCESSING,
            )

        context['success']=True

        return JsonResponse(context, content_type='application/json')

class DeliveryTableView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/택배배송 관리

    Datatable에 넣을 데이터를 받아옵니다.
    '''
    def get(self, request: HttpRequest):
        
        Paid = get_delivery(constants.DELIVERY, constants.PAID)
        Completed = get_delivery(constants.DELIVERY, constants.COMPLETED)
        Processing = get_delivery(constants.DELIVERY, constants.PROCESSING)
        Shipping = get_delivery(constants.DELIVERY, constants.SHIPPING)
        Delivered = get_delivery(constants.DELIVERY, constants.DELIVERED)

        delivery=[] 
        delivered=[]

        delivery.extend(Completed)
        delivered.extend(Paid)
        delivered.extend(Processing)
        delivered.extend(Shipping)
        delivered.extend(Delivered)

        context = {
            'delivery': delivery,
            'delivered': delivered,
        }

        return JsonResponse(context, content_type='application/json')

class ShortdeliveryView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/근거리배송
    '''
    template_name='shortdelivery_info.html'

    def get(self, request: HttpRequest):
        context={}

        if request.user.is_staff:
            context['staff'] = True
        if request.user.groups.filter(name='seller').exists():
            context['seller'] = True
        
        return render(request, self.template_name, context)

    def put(self, request: HttpRequest):
        context={}
        request.PUT = json.loads(request.body)

        Id = request.PUT.get('id')
        Transport_no = request.PUT.get('transport_no')

        # Update order status 
        order.objects.filter(id=Id).update(
            status=constants.PROCESSING,
            transport_no = Transport_no,
        )

        # Update order-product status of the order
        product_ids=order_product.objects.filter(order_id=Id).values_list('id', flat=True)
        for id in product_ids:
            order_product.objects.filter(id=id).update(
                status=constants.PROCESSING,
            )

        context['success']=True

        return JsonResponse(context, content_type='application/json')

class ShortdeliveryTableView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/근거리배송 관리

    Datatable에 넣을 데이터를 받아옵니다.
    '''
    def get(self, request: HttpRequest):

        Paid = get_delivery(constants.SHORTDELIVERY, constants.PAID)
        Completed = get_delivery(constants.SHORTDELIVERY, constants.COMPLETED)
        Processing = get_delivery(constants.SHORTDELIVERY, constants.PROCESSING)
        Shipping = get_delivery(constants.SHORTDELIVERY, constants.SHIPPING)
        Delivered = get_delivery(constants.SHORTDELIVERY, constants.DELIVERED)

        delivery=[] 
        delivered=[]

        delivery.extend(Completed)
        delivered.extend(Paid)
        delivered.extend(Processing)
        delivered.extend(Shipping)
        delivered.extend(Delivered)

        context = {
            'delivery': delivery,
            'delivered': delivered,
        }

        return JsonResponse(context, content_type='application/json')

class PickupView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/포장
    '''
    template_name='pickup_info.html'

    def get(self, request: HttpRequest):
        context={}

        if request.user.is_staff:
            context['staff'] = True
        if request.user.groups.filter(name='seller').exists():
            context['seller'] = True
        
        return render(request, self.template_name, context)

    def put(self, request: HttpRequest):
        context={}
        request.PUT = json.loads(request.body)
        next_status=constants.PROCESSING

        Id = request.PUT.get('id')
        Status = request.PUT.get('status')

        if Status == constants.PROCESSING:
            next_status=constants.DELIVERED

        # Update order status 
        order.objects.filter(id=Id).update(
            status=next_status,
        )
        # Update order-product status of the order
        product_ids=order_product.objects.filter(order_id=Id).values_list('id', flat=True)
        for id in product_ids:
            order_product.objects.filter(id=id).update(
                status=next_status,
            )

        context['success']=True

        return JsonResponse(context, content_type='application/json')


class PickupTableView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/포장 관리

    Datatable에 넣을 데이터를 받아옵니다.
    '''
    def get(self, request: HttpRequest):
        user_id=request.user.id

        Paid = get_delivery(constants.PICKUP, constants.PAID)
        Completed = get_delivery(constants.PICKUP, constants.COMPLETED)
        Processing = get_delivery(constants.PICKUP, constants.PROCESSING)
        Delivered = get_delivery(constants.PICKUP, constants.DELIVERED)

        delivery=[] 
        delivered=[]

        delivery.extend(Completed)
        delivery.extend(Processing)
        delivered.extend(Paid)
        delivered.extend(Delivered)

        context = {
            'delivery': delivery,
            'delivered': delivered,
        }

        return JsonResponse(context, content_type='application/json')


class DrivethruView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/드라이브스루
    '''
    template_name='drivethru_info.html'

    def get(self, request: HttpRequest):
        context={}

        if request.user.is_staff:
            context['staff'] = True
        if request.user.groups.filter(name='seller').exists():
            context['seller'] = True
        
        return render(request, self.template_name, context)

    def put(self, request: HttpRequest):
        context={}
        request.PUT = json.loads(request.body)
        next_status=constants.PROCESSING

        Id = request.PUT.get('id')
        Status = request.PUT.get('status')

        if Status == constants.PROCESSING:
            next_status=constants.DELIVERED

        # Update order status 
        order.objects.filter(id=Id).update(
            status=next_status,
        )
        # Update order-product status of the order
        product_ids=order_product.objects.filter(order_id=Id).values_list('id', flat=True)
        for id in product_ids:
            order_product.objects.filter(id=id).update(
                status=next_status,
            )

        context['success']=True

        return JsonResponse(context, content_type='application/json')

class DrivethruTableView(LoginRequiredMixin, View):
    '''
    관리자/판매관리/드라이브스루 관리

    Datatable에 넣을 데이터를 받아옵니다.
    '''
    def get(self, request: HttpRequest):
        user_id=request.user.id

        Paid = get_delivery(constants.DRIVETHRU, constants.PAID)
        Completed = get_delivery(constants.DRIVETHRU, constants.COMPLETED)
        Processing = get_delivery(constants.DRIVETHRU, constants.PROCESSING)
        #Shipping = get_delivery(constants.DRIVETHRU, constants.SHIPPING)
        Delivered = get_delivery(constants.DRIVETHRU, constants.DELIVERED)

        delivery=[] 
        delivered=[]

        delivery.extend(Completed)
        delivery.extend(Processing)
        delivered.extend(Paid)
        #delivered.extend(Shipping)
        delivered.extend(Delivered)

        context = {
            'delivery': delivery,
            'delivered': delivered,
        }

        return JsonResponse(context, content_type='application/json')

def get_all_delivery(type):
    return order.objects.filter(type=type,  DeleteFlag='0')\
              .values('call', 'code', 'order_no', 'status', 'transport_no', 'date', 'id')

def get_delivery(type, status):
    return order.objects.filter(type=type, status=status, DeleteFlag='0')\
              .values('call', 'code', 'order_no', 'status', 'transport_no', 'date', 'id')

