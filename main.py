import pandas as pd


def ugly_json():
    file = r'expound_response_single2.json'
    df = pd.read_json(file)
    print(df)
    services = df['services']
    locations = df['locations']
    services=dict({'services': services })
    locations= dict({'locations': locations})
    return services, locations


def flatten_json(nested_json, exclude=['']):
    """Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
            exclude: Keys to exclude from output.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name='',exclude=exclude):
        if type(x) is dict:
            for a in x:
                if a not in exclude: flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name)  # + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out


services, locations = ugly_json()

unested_services = pd.DataFrame([flatten_json(x) for x in services['services']])
unested_locations = pd.DataFrame([flatten_json(x) for x in locations['locations']])

print(unested_services)
print(unested_locations)