from enum import Enum

class UserTypeChoice(Enum):
    SUPER_ADMIN = "SA"
    DOCTOR = "DOC"
    CUSTOMER = "CUSTOMER"
     
    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def mappings(cls):
        return tuple((i.value, i.name.lower().replace('_', ' ')) for i in cls)

    @classmethod
    def super_admin(cls):
        return cls.SUPER_ADMIN.value

    @classmethod
    def doctor_user(cls):
        return cls.DOCTOR.value
    
    @classmethod
    def customer_user(cls):
        return cls.CUSTOMER.value

