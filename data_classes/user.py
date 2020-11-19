class Main_User:
    def __init__(self, first_name, last_name, email_address, phone_number, country, membership_status, account_created):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.country = country
        self.membership_status = membership_status
        self.account_created = account_created

class Profile:
    def __init__(self, name):
        self.name = name
        self.cs_actions = {}

    def __str__(self):
        return self.__dict__