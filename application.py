import sys
from api import *
import utility
utils = utility.UtilityClass()

class Application_Layer(object):
    def __init__(self, initialization):
        if initialization:
            self.show_users()

    def show_users(self):
        print 'Select user_id \nId\tUser_name'
        for _id, user in models_dict['users'].items():
            print '{}\t{}'.format(_id, user)
        try:
            user_id = input()
        except:
            print 'Invalid parameter. Exiting...'
            sys.exit()
        print "\nSelect action \n 1. Assign role(s) to user \n 2. Remove role(s) from user \n 3. Check Authorization \n 4. Exit"
        action_id = input()
        if action_id == 1:
            print "Select roles to assign\nId\tRole_name"
            for _id, role_name in models_dict['role'].items():
                print '{}\t{}'.format(_id, role_name)
            roles = input()
            role_instances = utils.get_instance(roles)
            response_msg, status_code = assign_roles(user_id, role_instances)
            if status_code:
                print '----------Success----------'
            else:
                print '----------Failure----------'
            self.show_users()

        elif action_id == 2:
            print "Select roles to remove \nId\tRole_name"
            for _id, role_name in models_dict['role'].items():
                print '{}\t{}'.format(_id, role_name)
            roles = input()
            role_instances = utils.get_instance(roles)
            response_msg, status_code = remove_roles(user_id, role_instances)
            if status_code:
                print '----------Success----------'
            else:
                print '----------Failure----------'
            self.show_users()

        elif action_id == 3:
            print "Select action type: \nId\tAction"
            for _id, action in models_dict['access_type'].items():
                print '{}\t{}'.format(_id, action)
            action_id = input()
            print "Select resource type:\n Id\tResource"
            for _id, resource in models_dict['resource'].items():
                print '{}\t{}'.format(_id, resource)
            resource_id = input()
            response_msg, status_code = check_authorization(user_id, action_id - 1, resource_id)
            print "----------{}----------".format(response_msg)
            self.show_users()

        elif action_id == 4:
            print "Are you sure want to exit"
            response = raw_input()
            if response.lower() == 'y':
                sys.exit()

            else:
                self.show_users()

if __name__ == '__main__':
    Application_Layer(initialization=True)
