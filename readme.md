# Customer_mgmt


Customer_mgmt is a python based CLI application.

In this app, one can:
  - Add customer in a mongodb database
  - Delete customer
  - Update customer name
  - View a customer by id
  - View all customers


### Tech

Customer_mgmt uses a number of open source projects to work properly:

* [MongoDb](https://www.mongodb.com/download-center/community) - For backend development
* [Python](https://www.python.org/downloads/) - For working with MongoDB
* [ pymongo ](https://api.mongodb.com/python/current/) - Distribution tool for working with MongoDB
* [mongoengine](mongoengine.org) - mongoengine a python object data mapper for mongodb.



### Installation

Create a virtual environment before starting the project
```sh
$ cd customer_mgmt
$ python3 -m venv env
```
For activating the virtual environment[Windows]
```sh
$ cd customer_mgmt
$ env\bin\activate.bat
```

Run  the requirements.txt
```sh
$ cd customer_mgmt
$ pip install -r requirements.txt
$ 
```

For running the main program

```sh
$ cd ../customer_mgmt/src/
$ python program.py
```

### Code style

Follow PEP8: https://www.python.org/dev/peps/pep-0008/
Use pycodestyle to automatically check for PEP8.