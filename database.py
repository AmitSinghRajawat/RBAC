'''
key-value pair non persistent database.
session-level persistency.
'''
models_dict = {}
models_dict['users']={}
models_dict['users'][1]='Amit'
models_dict['users'][2]='Eshan'
models_dict['users'][3]='Parmil'
models_dict['users'][4]='Abhishek'
models_dict['users'][5]='Harsh'

models_dict['user_roles']={}
models_dict['user_roles'][1]=[]
models_dict['user_roles'][2]=[]
models_dict['user_roles'][3]=[]
models_dict['user_roles'][4]=[]
models_dict['user_roles'][5]=[]

models_dict['access_type']={}
models_dict['access_type'][1]='Read'
models_dict['access_type'][2]='Write'
models_dict['access_type'][3]='Delete'

models_dict['role']= {}
models_dict['role'][1]='Admin'
models_dict['role'][2]='Manager'
models_dict['role'][3]='Client'
models_dict['role'][4]='Developer'

models_dict['resource'] = {}
models_dict['resource'][1]='third-party'
models_dict['resource'][2]='catalogue-resource'