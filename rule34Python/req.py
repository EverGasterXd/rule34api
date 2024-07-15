import requests
import random
from xml.etree import ElementTree
from bs4 import BeautifulSoup

def get_comments(post_id:str =None, limit= int):
    if(limit < 0):
        raise Exception('the minimum value for "limit" is 0')
        return
    elif(limit > 100):
        raise Exception('the maximium value for "limit" is 100')
        return
    try:
        r = requests.get(f"https://api.rule34.xxx/index.php?page=dapi&s=comment&q=index&post_id={post_id}")
        r.raise_for_status()
    except Exception as e:
        raise Exception(f"ERROR: > {e}\n\n\nPlease contact Evergaster or open an issue in https://github.com/EverGasterXd/rule34api/issues")
    else:
        comments_tree = ElementTree.fromstring(r.content)
        comments = [comment.attrib['body'] for comment in comments_tree.findall('comment')]
        comments_full = random.sample(comments, min(limit, len(comments)))
        if limit is not None:
            return '\n'.join(comments_full)+'.'
        else:
            return comments

def get(param:str = None, limit= int):
    if(limit < 0):
        raise Exception('the minimum value for "limit" is 0')
        return
    elif(limit > 100):
        raise Exception('the maximium value for "limit" is 100')
        return
    try:
        if param:
            r = requests.get(f"https://api.rule34.xxx//index.php?page=dapi&s=post&q=index&tags={param}")
        else:
            r = requests.get("https://api.rule34.xxx//index.php?page=dapi&s=post&q=index")
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