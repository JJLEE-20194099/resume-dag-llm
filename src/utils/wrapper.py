import json

cv_info_key = json.load(open('src/config/cv_info_key.json', 'r'))

def wrap_resume(resume):
    wrap_resume = dict()

    for key in cv_info_key:
        try:
            wrap_resume[cv_info_key[key]] = list(set(resume[key]))
        except:
            wrap_resume[cv_info_key[key]] = []
    return wrap_resume

def wrap_id(obj):
    try:
        obj['_id'] = str(obj['_id'])
    except:pass
    try:
        obj['batch_id'] = str(obj['batch_id'])
    except:pass

    try:
        obj['cv_ids'] = [str(item) for item in obj['cv_ids']]
    except:pass

    return obj