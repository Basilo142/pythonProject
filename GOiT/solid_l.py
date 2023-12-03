class Notification:
    def notify(self, message):
        raise NotImplemented


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to email {self.email}')


class Sms(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} sms to phone {self.phone}')


if __name__ == '__main__':
    person = Contact('Alex', 'alex@gmail.com', '+380501555555')
    service_sms = Sms(person.phone)
    service_mail = Email(person.email)
    service_sms.notify('hi')
    service_mail.notify('Fuu')
