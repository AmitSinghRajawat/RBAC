from models import *

class UtilityClass(object):
    def __init__(self):
        pass

    def get_instance(self, role_ids):
        instance_list = []
        try:
            for _id in role_ids:
                if models_dict['role'][_id] == 'Admin':
                    instance = Admin()
                elif models_dict['role'][_id] == 'Manager':
                    instance = Manager()
                elif models_dict['role'][_id] == 'Client':
                    instance = Client()
                elif models_dict['role'][_id] == 'Developer':
                    instance = Developer()
                instance_list.append(instance)
        except Exception as e:
            print e.args
        finally:
            return instance_list