import datetime
import bson

from data.customer import Customer


def add_customer(name, email, phone_number, city, dob, gender):
    customer = Customer()
    customer.name = name
    customer.email = email
    customer.phone_number = phone_number
    customer.city = city
    customer.dob = dob
    customer.gender = gender

    customer.save()

    return customer


def delete_customer(customerObject):
    customerObject.delete()
    return


def update_customer(customerObject,updated_name):
    customerObject.update(set__name=updated_name)
    return


def get_customer(name):
    query = Customer.objects(name=name)

    return query


def get_all_customer():
    query = Customer.objects()
    return query





def find_email(email):
    #.first()-retrieving the first result and return none f no result exists.
    customer = Customer.objects(email=email).first()
    return customer
