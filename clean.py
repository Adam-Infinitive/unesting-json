import pandas as pd
import json
import ast

def ugly_json():
    file=r'data/expound_response_single2.json'
    df = pd.read_json(file)
    services = df['services']
    locations = df['locations']
    services=dict({'services': services})
    locations= dict({'locations': locations})
    return services, locations


def flatten_json(nested_json, exclude_keys=['']):
    flattened = {}

    def flatten(x, name='', exclude=exclude_keys):
        if type(x) is dict:
            for a in x:
                if name == 'address_':
                    print('skip')
                elif a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:

            if name == 'address_':
                list_of_addresses = []
                for address in x:
                    list_of_addresses.append(address)
                counter = 0
                addr_dict = {}
                for address in list_of_addresses:
                    counter+=1
                    for key in address.keys():
                        a = str(key + '_' + str(counter))
                        addr_dict.update({a:address[key]})
                print(addr_dict)
                for a in addr_dict:
                    print(addr_dict[a])
                    flatten(addr_dict[a], name + a + '_')
            i = 0
            for a in x:

                flatten(a, name)
                i += 1
        else:
            flattened[name[:-1]] = x

    flatten(nested_json)
    return flattened


services, locations = ugly_json()

un_nested_services = pd.DataFrame([flatten_json(x) for x in services['services']])
un_nested_locations = pd.DataFrame([flatten_json(x) for x in locations['locations']])
