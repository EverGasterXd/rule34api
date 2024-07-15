import requests
import random
from xml.etree import ElementTree
from collections import namedtuple

Artist = namedtuple('Artist', ['name', 'id', 'group_id', 'urls'])

def get(param: str = None, limit: int = None):

    if(limit < 0):
        raise Exception('the minimum value for "limit" is 0')
        return
    elif(limit > 100):
        raise Exception('the maximium value for "limit" is 100')
        return

    try:
        if param:
            r = requests.get(f"https://yande.re/post.xml?tags={param}")
        else:
            r = requests.get("https://yande.re/post.xml")
        r.raise_for_status()
    except Exception as e:
        raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/rule34api/issues")
    else:
        try:
            tree = ElementTree.fromstring(r.content)
            file_urls = [post.attrib['file_url'] for post in tree.findall('post')]
            comments_id = [post.attrib['id'] for post in tree.findall('post')]
            if file_urls:
                random_urls = random.sample(file_urls, min(limit, len(file_urls)))
                return '\n'.join(random_urls)          
            else:
                return 'No se encontraron resultados.'
        except Exception as e:
            raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/rule34api/issues")
        
def getArtist(page= int, name= str) -> Artist:
    if page is None and name is None:
        raise ValueError('Debe proporcionar un número de página o un nombre de artista.')

    try:
        if name:
            r = requests.get(f"https://yande.re/artist.xml?name={name}")
        else:
            if page < 1:
                raise ValueError('El valor mínimo para "page" es 1.')
            r = requests.get(f"https://yande.re/artist.xml?page={page}")
        r.raise_for_status()

        tree = ElementTree.fromstring(r.content)
        artists = tree.findall('artist')

        if artists:
            artist = random.choice(artists)
            name_user = artist.attrib.get('name', 'not found')
            id = artist.attrib.get('id', 'not found')
            group_id = artist.attrib.get('group_id', 'not found')
            urls = artist.attrib.get('urls', 'not found')
            return Artist(name_user, id, group_id, urls)
        else:
            return Artist('No se encontraron resultados en la página especificada.', '', '', '')

    except Exception as e:
        raise Exception(f"ERROR: {e}\n\nPlease contact EverGaster or open an issue at https://github.com/EverGasterXd/rule34api/issues")
