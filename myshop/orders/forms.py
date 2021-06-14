from django import forms
from .models import Order



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
        'first_name': 'Имя', 
        'last_name': 'Фамилия',
        'email':'Email',
         'address': 'Ваш адрес доставки', 
         'postal_code': 'Почтовый индекс',
         'city': 'Телефон',
        }

        error_messages = {
        'first_name': {
        	'null':"Введите в поле Имя свои данные",
        	'required' : "Поле Имя обязательное для заполнения!"}, 
        'last_name': {
        	'null':"Введите в поле Фамилия свои данные",
        	'required' : "Поле Фамилия обязательное для заполнения!"},
        'email':{
        	'null':"Введите в поле Емайл свои данные",
        	'required' : "Поле Емайл обязательное для заполнения!"},
        'address': {
        	'null':"Введите в поле Адрес свои данные",
        	'required' : "Поле Адрес обязательное для заполнения!"}, 
        'postal_code': {
        	'null':"Введите в поле Индекс свои данные",
        	'required' : "Поле Индекс обязательное для заполнения!"},
        'city': {
        	'null':"Введите в поле Телефон свои данные",
        	'required' : "Поле Телефон обязательное для заполнения!"},
        }