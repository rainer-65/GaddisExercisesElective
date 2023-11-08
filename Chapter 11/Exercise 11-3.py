# Programming Exercise 11-3

import person


def main():
    # Local variables
    name = ''
    address = ''
    phone_number = ''
    cust_number = 0
    on_list_flag = False

    # Get data attributes.
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    phone_number = input('Enter the phone number: ')
    cust_number = input('Enter the customer number: ')
    on_list = input('Does the customer wish to be '
                    'on the mailing list?(Yes/No) ')

    if on_list == 'Yes':
        on_list_flag = True
    else:
        on_list_flag = False

    # Create an instance of Customer.
    customer = person.Customer(name, address, phone_number,
                               cust_number, on_list_flag)

    # Display information.
    print('Customer information: ')
    print(f'Name: {customer.get_name()}')
    print(f'Address: {customer.get_address()}')
    print(f'Phone number: {customer.get_phone_number()}')
    print(f'Customer Number: {customer.get_cust_number()}')
    print(f'On Mailing List: {customer.get_on_list()}')


# Call the main function.
if __name__ == '__main__':
    main()
