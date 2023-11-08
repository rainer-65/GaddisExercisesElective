# Create a Person class
class Person:
    # Initialize the person attibutes
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # Create accessor and mutator methods for the attributes
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    # Create thr mutator methods
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    # Return the current state of the object
    def __str__(self):
        return 'Name: ' + self.__name + '\n' \
                                        'Address: ' + self.__address + '\n' \
                                                                       'Age: ' + str(self.__age) + '\n' \
                                                                                                   'Phone: ' + self.__phone


# Create the main function
def main():
    # Create 3 objects, one for you, one for your friend and one for your family
    my_personal_info = Person('John Major', '10000 NYC', 29, '332-3321-6997')
    my_friend_info = Person('Peter Barrett', '10277 NYC', 30, '332-3262-1388')
    my_family_info = Person('Mike Johnson', '10128 NYC', 63, '332-6076-5926')

    print('These are the details of the personal information you entered ...')
    print('=================================================================')
    print()
    print('My Personal Details')
    print('-------------------')
    print(my_personal_info)

    print()
    print('My Friend Details')
    print('-----------------')
    print(my_friend_info)

    print()
    print('My Personal Member Details')
    print('--------------------------')
    print(my_family_info)


if __name__ == '__main__':
    main()
