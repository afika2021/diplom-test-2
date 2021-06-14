from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Favorit(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        favorit = self.session.get(settings.FAVORIT_SESSION_ID)
        if not favorit:
            # save an empty cart in the session
            cart = self.session[settings.FAVORIT_SESSION_ID] = {}
        self.favorit = favorit

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.favorit:
            self.favorit[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.favorit[product_id]['quantity'] = quantity
        else:
            self.favorit[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.FACORIT_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favorit:
            del self.favorit[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.favorit.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.favorit[str(product.id)]['product'] = product

        for item in self.favorit.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.favorit.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.favorit.values())

    def clear(self):
        del self.session[settings.FAVORIT_SESSION_ID]
        self.session.modified = True