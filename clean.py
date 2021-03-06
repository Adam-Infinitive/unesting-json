import pandas as pd
import joblib

def ugly_json():
    single = r'data/expound_response_single2.json'
    df_single = pd.read_json(single)
    services_df = df_single['services']
    locations_df = df_single['locations']
    organization_df = df_single.drop(columns=['services', 'locations'])
    services_dict = dict({'services': services_df})
    locations_dict = dict({'locations': locations_df})
    return services_dict, locations_dict, organization_df


def flatten_json(nested_json, exclude_keys=['']):
    flattened = {}

    def flatten(x, name='', exclude=exclude_keys):
        if type(x) is dict:
            for a in x:
                if a not in exclude and name != 'address_':
                    flatten(x[a], name + a + '_')
        elif type(x) is list:
            if name == 'address_':
                counter = 0
                addr_dict = {}
                for address in x:
                    '''
                    x: list of dictionaries containing address details
                    address: dictionary containing address details
                    '''
                    counter += 1
                    for key in address:
                        a = str(key + '_' + str(counter))
                        addr_dict.update({a: address[key]})
                for key in addr_dict:
                    flatten(addr_dict[key], name + key + '_')
            for a in x:
                flatten(a, name)
        else:
            flattened[name[:-1]] = x

    flatten(nested_json)
    return flattened


services, locations, organization = ugly_json()

un_nested_services = pd.DataFrame([flatten_json(x) for x in services['services']])
un_nested_locations = pd.DataFrame([flatten_json(x) for x in locations['locations']])
print(un_nested_locations.head())
print(un_nested_services.head())
print(organization.head())
