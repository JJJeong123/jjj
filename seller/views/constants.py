'''Order status'''

# 결제완료, 상품준비완료, 배송준비중, 배송지연, 배송중, 배송완료
PAID = '0'
COMPLETED = '1'
PROCESSING = '2'
SHIPPING = '3'
DELIVERED = '4'

# 환불접수, 환불처리중, 환불 완료
REFUND_RECEIVED = '5'
REFUND_PROCESSING = '6'
REFUNDED = '7'

# 취소접수, 취소처리중, 취소완료
CANCEL_REQUESTED = '8'
CANCEL_PROCESSING = '9'
CANCELED = '10'


'''Order type'''

# 택배배송, 근거리배송, 포장, 드라이브스루
DELIVERY = '0'
SHORTDELIVERY = '1'
PICKUP = '2'
DRIVETHRU = '3'