from .reqRe import get, getArtist

def search(tags= str, limit:int =None):
    """search for tags:

    Args:
        tags = str 
        limit = int or None.

    """

    return get(tags, limit)
def getArtists(page:int = None, name:str=None):
    """Get artist

    Args:
        page: int,
        name: str.

        
    Get:
        name,
        id,
        group_id,
        urls,
    """

    return getArtist(page, name)
def get_random_post(limit=None):
    return get(None, limit)