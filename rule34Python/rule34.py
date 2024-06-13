from .req import get, get_comments

def search(tags: str = None, limit=int):
    return get(tags, limit)
    
def getCommets(limit= int):
    return get_comments(limit=limit)
def get_random_post(limit=int):
    return get(None, limit)
    