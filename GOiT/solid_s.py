class ValidPhoneNumber(Exception):
    pass


class PersonInfo:
    def value_of(self):
        raise NotImplemented


class PersonPhoneNumber(PersonInfo):
    def __init__(self, phone: str, operator_code: str):
        if operator_code != '050':
            raise ValidPhoneNumber
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f'+38({self.operator_code}){self.phone}'


class PersonAddress(PersonInfo):
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person:
    def __init__(self, name: str, phone: PersonPhoneNumber, address: PersonAddress):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.name}'

    def get_phone_number(self):
        return f'{self.name}: {self.phone.value_of()}'

    def get_person_address(self):
        return f'{self.name}: {self.address.value_of()}'


if __name__ == '__main__':
    phone = PersonPhoneNumber('1555555', '050')
    address = PersonAddress('123', 'Kyiv', 'srt_t')
    person = Person('Alex', phone, address)
    print(person, person.get_person_address(), person.get_phone_number(), sep='\n')

