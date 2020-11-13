import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wra(*args, **kwargs):
        return json.dumps(func(*args,**kwargs))
    return wra


@to_json
def get_data():
    return {'data': 42}



get_data()