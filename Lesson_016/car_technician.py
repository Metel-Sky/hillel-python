class CarTechnician:
    def __init__(self, name: str, phone: str, address: str, comment: str = ''):
        self.name = name
        if self._validate_phone_number(phone):
            self.phone = phone
        else:
            raise ValueError(f'{phone} is not a valid phone number')
        self.address = address
        self.comment = comment

    @staticmethod
    def _validate_phone_number(phone: str):
        clean = phone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        if clean[0] == '+':
            clean = clean[1:]
        return clean.isdigit()

    def __str__(self):
        return f"Авторемонтник {self.name}, {self.phone}, {self.address}"

    # repr = representation, вызывается когда CarTechnician - подобъект другого объекта
    """
    def __repr__(self):
        return str(self)"""

    def maintenance(self, car):
        print(f'{self} проводит техобслуживание {car}')

    def repair(self, car):
        print(f'{self} проводит ремонт {car}')

    def diagnose(self, car):
        print(f'{self} проводит диагностику {car}')