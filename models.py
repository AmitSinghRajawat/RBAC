from database import *
from abc import abstractmethod,ABCMeta

class Abstract_Role_Class:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_permission(self):
        raise NotImplementedError

    def set_permission(self):
        raise NotImplementedError

class Admin(Abstract_Role_Class):
    def __init__(self):
        self.authorization_dict = {}
        self.authorization_dict[models_dict['resource'][1]]='111'
        self.authorization_dict[models_dict['resource'][2]]='111'

    def get_permission(self, resource_name=None):
        if self.authorization_dict.has_key(resource_name):
            return self.authorization_dict[resource_name]
        elif resource_name is None:
            return self.authorization_dict
        else:
            raise 'Resource unavailable'

    def set_permission(self, resource_name, authorization_pattern):
        if self.authorization_dict.has_key(resource_name):
            self.authorization_dict[resource_name]=authorization_pattern
        else:
            raise 'Resource unavailable'

class Manager(Abstract_Role_Class):
    def __init__(self):
        self.authorization_dict = {}
        self.authorization_dict[models_dict['resource'][1]]='110'
        self.authorization_dict[models_dict['resource'][2]]='111'

    def get_permission(self, resource_name=None):
        if self.authorization_dict.has_key(resource_name):
            return self.authorization_dict[resource_name]
        elif resource_name is None:
            return self.authorization_dict
        else:
            raise 'Resource unavailable'

    def set_permission(self, resource_name, authorization_pattern):
        if self.authorization_dict.has_key(resource_name):
            self.authorization_dict[resource_name]=authorization_pattern
        else:
            raise 'Resource unavailable'

class Client(Abstract_Role_Class):
    def __init__(self):
        self.authorization_dict = {}
        self.authorization_dict[models_dict['resource'][1]]='100'
        self.authorization_dict[models_dict['resource'][2]]='100'

    def get_permission(self, resource_name=None):
        if self.authorization_dict.has_key(resource_name):
            return self.authorization_dict[resource_name]
        elif resource_name is None:
            return self.authorization_dict
        else:
            raise 'Resource unavailable'

    def set_permission(self, resource_name, authorization_pattern):
        if self.authorization_dict.has_key(resource_name):
            self.authorization_dict[resource_name]=authorization_pattern
        else:
            raise 'Resource unavailable'

class Developer(Abstract_Role_Class):
    def __init__(self):
        self.authorization_dict = {}
        self.authorization_dict[models_dict['resource'][1]]='100'
        self.authorization_dict[models_dict['resource'][2]]='111'

    def get_permission(self, resource_name=None):
        if self.authorization_dict.has_key(resource_name):
            return self.authorization_dict[resource_name]
        elif resource_name is None:
            return self.authorization_dict
        else:
            raise 'Resource unavailable'

    def set_permission(self, resource_name, authorization_pattern):
        if self.authorization_dict.has_key(resource_name):
            self.authorization_dict[resource_name]=authorization_pattern
        else:
            raise 'Resource unavailable'