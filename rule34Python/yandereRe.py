from .reqRe import get, getArtist

def search(tags, limit=None):
    return get(tags, limit)
def getArtists(page:int = None, name:str=None):
    return getArtist(page, name)
def get_random_post(limit=None):
    return get(None, limit)