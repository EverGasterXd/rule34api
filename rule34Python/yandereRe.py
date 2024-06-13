from .reqRe import get

def search(tags, limit=None):
    return get(tags, limit)

def get_random_post(limit=None):
    return get(None, limit)