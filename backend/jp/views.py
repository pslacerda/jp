import json
from datetime import datetime

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from flask import request
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

from jp.app import app, customer_updated
from jp.models.models import Product, Customer, Sale, Payment


def jsonify(data):
    if isinstance(data, QuerySet):
        data = list(data.values())
    return json.dumps(data, cls=DjangoJSONEncoder)


def remove_trigram_index(d):
    del d['trigram_index']
    return d


@app.route("/search_customers")
def search_customers():
    query = request.args.get('q', '')
    customer_list = Customer.objects.annotate(
        similarity=TrigramSimilarity('trigram_index', query)
    ).order_by('-similarity')[:10]

    return jsonify({
        'result': [
            remove_trigram_index(model_to_dict(c))
            for c in customer_list
        ]
    })


@app.route("/create_customer", methods=['PUT'])
def create_customer():
    customer = Customer(**request.get_json())
    customer.save()
    customer_updated.send(sender=Customer, instance=customer)
    return jsonify({
        'result': remove_trigram_index(
            model_to_dict(customer)
        )
    })


@app.route("/edit_customer", methods=['POST'])
def edit_customer():
    data = request.get_json()
    pk = data.pop('id')
    Customer.objects.filter(pk=pk).update(**data)
    customer = Customer.objects.filter(pk=pk).first()
    customer_updated.send(sender=Customer, instance=customer)
    return jsonify({
        'result': remove_trigram_index(
            model_to_dict(customer)
        )
    })


@app.route("/create_product", methods=['PUT'])
def create_product():
    product = Product(**request.get_json())
    product.save()
    return jsonify({
        'result': model_to_dict(product)
    })


@app.route("/list_products")
def list_products():
    return jsonify({
        'results': [
            model_to_dict(p)
            for p in Product.objects.all()
        ]
    })


@app.route("/create_sale", methods=['PUT'])
def create_sale():
    data = request.get_json()
    data['customer'] = get_object_or_404(Customer, pk=data['customer'])
    data['product'] = get_object_or_404(Product, pk=data['product'])
    data['date'] = datetime.strptime(data['date'], "%Y-%m-%d").date()
    sale = Sale(**data)
    sale.save()
    return jsonify({
        'results': model_to_dict(sale)
    })


@app.route("/report_sales")
def report_sales():
    customer = get_object_or_404(
        Customer,
        pk=request.args['customer']
    )
    sales = []
    for sale in customer.sale_set.all():
        payments = []
        for payment in sale.payment_set.order_by('-date').all():
            payments.append(model_to_dict(payment))
        sale = model_to_dict(sale)
        sale['payments'] = payments
        sale['product'] = get_object_or_404(Product, pk=sale['product']).description
        sales.append(sale)

    return jsonify({
        'results': sales
    })


@app.route("/create_payment", methods=["PUT"])
def create_payment():
    data = request.get_json()
    data['sale_id'] = data.pop('sale')
    payment = Payment(**data)
    payment.save()
    return jsonify({
        'status': 'ok',
        'payment': model_to_dict(payment)
    })
