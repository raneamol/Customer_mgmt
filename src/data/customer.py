import datetime
import mongoengine
import pymongo
#from src.data.mongo_setup import global_init
#global_init()
class Customer(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    phone_number = mongoengine.StringField(required=True)
    city = mongoengine.StringField(required=True)
    dob = mongoengine.DateTimeField(required=True)
    gender = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'customer'
    }

'''query = Customer.objects(id="5e32994864e99a43784210b0").delete()
query = Customer.objects()
print(f'You have {len(query)} customers.')
for idx, n in enumerate(query):
    print(f' {idx + 1}. Name:{n.name} \n Email:{n.email} \n Ph no:{n.phone_number} \n' \
          f' City:{n.city} \n Date of birth:{n.dob} \n Gender:{n.gender} \n Id:{n.id}')
    print()
'''