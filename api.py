from database import *

def assign_roles(user_id, roles):
    '''
    responsible for assignment of roles to the user_id
    :param user_id: id in users table in database
    :param roles: can be Admin, Developer etc.
    :return: success or failure status of role assignment
    '''
    response_msg, status_code = '', 1
    try:
        for role in roles:
            if models_dict['users'].has_key(user_id):
                is_present = False
                for role_type in models_dict['user_roles'][user_id]:
                    if role.__class__ == role_type.__class__:
                        is_present = True
                if is_present is False:
                    models_dict['user_roles'][user_id].append(role)
            else:
                status_code = 0
    except Exception as e:
        status_code = 0
        response_msg = e.args
    finally:
        return response_msg, status_code

def remove_roles(user_id, roles):
    '''
    responsible for removal for roles from the user_id
    :param user_id: id in users table in database
    :param roles: can be Admin, Developer etc.
    :return: success or failure status of role removal
    '''
    response_msg, status_code = '', 1
    try:
        for role in roles:
            if models_dict['user_roles'].has_key(user_id):
                for role_type in models_dict['user_roles'][user_id]:
                    if role.__class__ == role_type.__class__:
                        models_dict['user_roles'][user_id].remove(role_type)
            else:
                status_code = 0
    except Exception as e:
        status_code = 0
        response_msg = e.args
    finally:
        return response_msg, status_code

def check_authorization(user_id, action_idx, resource_id):
    '''
    responsible for checking for a particular user_id if authorized to access resource with access_type
    :param user_id: id in users table in database
    :param action_idx: access_type index value for a permission index
    :param resource_id: id in resource table in database
    :return: returns Authorization status
    '''
    response_msg, status_code = 'Not Authorized', 1
    try:
        for role in models_dict['user_roles'][user_id]:
            if role.authorization_dict[models_dict['resource'][resource_id]][action_idx] == '1':
                response_msg = 'Authorized'
                break
    except Exception as e:
        response_msg = e.args
        status_code = 0
    finally:
        return response_msg, status_code