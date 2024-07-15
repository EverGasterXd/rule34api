from .req import get, get_comments

def search(tags: str, limit=int):
    """
    search for tags

    tags = str

    limit = int
    """
    return get(tags, limit)
    
def getCommets(limit= int):
    """ 
    get comments random

    limit = int 
    """
    return get_comments(limit=limit)
def get_random_post(limit=int):
    return get(None, limit)

    