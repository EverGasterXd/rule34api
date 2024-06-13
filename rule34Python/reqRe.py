import requests
import random
from xml.etree import ElementTree

def get(param=None, limit=3):
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
            if file_urls:
                random_urls = random.sample(file_urls, min(limit, len(file_urls)))
                return '\n'.join(random_urls)
            else:
                return 'No se encontraron resultados.'
        except Exception as e:
            raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/rule34api/issues")