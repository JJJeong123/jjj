from django.urls import path

from . import views
from .views import info_product_views, info_member_views, info_order_views, info_qna_views, info_shop_views

app_name = 'management'

urlpatterns=[
    #점포 관리
    path('shop', info_shop_views.ShopView.as_view(), name='shop'),
    #상품 관리
    path('product', info_product_views.ProductView.as_view(), name='product'),
    #회원 관리
    path('member', info_member_views.MemberView.as_view(), name='member'),
    #주문 관리
    path('order', info_order_views.OrderView.as_view(), name='order'),
    #path('order-data', info_order_views.PassData.as_view(), name='order-data')
    #path('order-detail', info_order_views.GetDetail.as_view(), name='order-detail'),

    #문의 관리
    path('qna', info_qna_views.QnaView.as_view(), name='qna'),
    path('qna-post/<str:id>', info_qna_views.QnaPostView.as_view(), name='qna-post'),
    path('qna-edit/<str:id>', info_qna_views.QnaEditView.as_view(), name='qna-edit'),

]