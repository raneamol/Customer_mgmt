import mongoengine
import data.mongo_setup as mongo_setup
import services.data_service as svc


def main():
    mongo_setup.global_init()
    opening_message()

    action = input("Enter anything between 1-6:")
    action = action.strip().lower()
    if (action == '1' or action == 'a'):
        add_customer()
    elif (action == '2' or action == 'd'):
        delete_customer()
    elif (action == '3' or action == 'u'):
        update_customer()
    elif (action == '4' or action == 'g'):
        get_customer()
    elif (action == '5' or action == 'c'):
        get_all_customer()
    elif (action == '6' or action == 'x' or action == 'exit'):
        exit_app()
    else:
        print("Enter valid command:")
    return


def opening_message():
    print("***************Welcome*****************")
    print()
    print("1. [A]dd a customer:")
    print()
    print("2. [D]elete a customer:")
    print()
    print("3. [U]pdate customer details:")
    print()
    print("4. [G]et a customer details:")
    print()
    print("5. Get details of all [c]ustomers:")
    print()
    print("6. E[x]it")
    print()


def add_customer():
    name = input('Enter name:')
    email = input("Enter email id:").strip().lower()

    old_account = svc.find_email(email)
    if old_account:
        print("Error: Account with email {} already exists".format(email))
        return

    phone_number = input("Enter phone number:")
    city = input("Enter city:")
    dob = input("Enter date of birth in [YYYY-MM-DD] format:")
    gender = input("Male or Female:")
    gender = gender.strip().lower()
    if (gender == 'male' or gender == 'm'):
        gender = 'Male'
    elif (gender == 'female' or gender == 'f'):
        gender = 'Female'
    else:
        print('Enter valid input')
        return

    svc.add_customer(name, email, phone_number, city, dob, gender)
    print("Success: Customer is added.")
    return


def delete_customer():
    get_all_customer()
    customerObjectList = svc.get_all_customer()
    customerObject = customerObjectList[int(input("Which number customer do you want to delete:")) - 1]
    svc.delete_customer(customerObject)
    print("The entry is Deleted.")
    return


def update_customer():
    get_all_customer()
    customerObjectList = svc.get_all_customer()
    customerObject = customerObjectList[int(input("Which customer's name do you want to update(number):")) - 1]
    updated_name = input("Enter the updated name:")
    svc.update_customer(customerObject, updated_name)
    print("Query is updated.\n")
    print("Updated document:")
    query = svc.get_customer(updated_name)
    '''for idx, n in enumerate(query):
        print(f' {idx + 1}. Name:{n.name} \n Email:{n.email} \n Ph no:{n.phone_number} \n' \
              f' City:{n.city} \n Date of birth:{n.dob} \n Gender:{n.gender} \n Id:{n.id}')
        print()'''
    show_output(query)




def get_customer():
    name = input("Enter the name of the customer")
    query = svc.get_customer(name)
    print(f'You have {len(query)} customer.')
    '''for idx, n in enumerate(query):
        print(f' {idx + 1}. Name:{n.name} \n Email:{n.email} \n Ph no:{n.phone_number} \n' \
              f' City:{n.city} \n Date of birth:{n.dob} \n Gender:{n.gender} \n Id:{n.id}')
        print()'''
    show_output(query)


def get_all_customer():
    query = svc.get_all_customer()
    print(f'You have {len(query)} customers.')
    '''for idx, n in enumerate(query):
        print(f' {idx + 1}. Name:{n.name} \n Email:{n.email} \n Ph no:{n.phone_number} \n' \
              f' City:{n.city} \n Date of birth:{n.dob} \n Gender:{n.gender} \n Id:{n.id}')
        print()'''
    show_output(query)


def exit_app():
    exit()


def show_output(query):
    for idx, n in enumerate(query):
        print(f' {idx + 1}. Name:{n.name} \n Email:{n.email} \n Ph no:{n.phone_number} \n' \
              f' City:{n.city} \n Date of birth:{n.dob} \n Gender:{n.gender} \n Id:{n.id}')
        print()


if __name__ == '__main__':
    main()
