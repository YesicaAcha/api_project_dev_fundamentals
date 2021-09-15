from truck_delivery_yess.person import Person


class Client(Person):
    """ Class representing a Client """
    def __init__(self, ci, name, email, cellphone, address, nit):
        super(Client, self).__init__(ci, name, email, cellphone, address)
        self.nit = nit

    def to_dict(self):
        dict_init = self.__dict__
        dict_init.pop("nit", None)
        return dict_init


