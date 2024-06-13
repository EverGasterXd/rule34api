import requests
from xml.etree import ElementTree
import random

def get(param, limit=None):
    try:
        r = requests.get(f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={param}")
    except Exception as e:
        raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/sara_api/issues")
    else:
        try:
            tree = ElementTree.fromstring(r.content)
            file_urls = [post.attrib['file_url'] for post in tree.findall('post')]
            if file_urls:
                # Seleccionar 3 URLs aleatorias
                random_urls = random.sample(file_urls, min(limit, len(file_urls)))
                return '\n'.join(random_urls)
            else:
                return None
        except Exception as e:
            raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/sara_api/issues")

