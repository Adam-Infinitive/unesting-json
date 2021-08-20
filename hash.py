import pandas as pd
import joblib
import json

full = r'data/expound_midlands.json'
copy = r'data/expound_midlands_copy.json'

def export():
    with open(full, 'r') as in_json_file:

        json_dict = json.load(in_json_file)

        # print(json_dict)
        # print(type(json_dict))
        # print(json_dict.keys())
        obj_list = json_dict['organizations']
        # print(json_dict['organizations'])
        counter = 0
        for x in obj_list:
            counter+=1
            print(counter)

export()

def hash(obj):

    # df_full=pd.read_json(full)
    # # print(df_full)
    obj_df = pd.read_dict(obj)

    df_hash=joblib.hash(obj_df, hash_name='sha1')
    print(df_hash)