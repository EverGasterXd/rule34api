<div align="center">
    <br />
    <p>
       <a href="https://discord.gg/GTJtFGUNV5"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Rule34Logo.png", width="200", height="100">
        </a>
    </p>
    <br />
</div>
this api is designed for the connection between rule34 and discord users.

## Version
- 0.0.0.7: fix when returning information and improve in README.md
- 0.0.0.9: new yandere.re
- 0.0.1.1: new fuctions, random comments and get artist info yandere.re
- 0.0.1.3: decorated

## Installation
```shell
pip install rule34Py
```
## Usage rule34
to start import ``rule34Python`` 

```shell
from rule34Python import rule34

Rule34 = rule34.search("catgirl", limit=3)

print(Rule34)
```

## Rule34

the functions in rule34 are as follows:

### Search

find a name specific to your taste 
requirements | descriptions
---|---
limit| is the limit of images to be sent
Comments | gets random comments from the same tag you posted 
tags | will be the content that will be searched in the api to return the link.

### random_post

search for an allatory publication
requirements | descriptions
---|---
limit| is the limit of images to be sent

will be the content that will be searched in the api to return the link.
## usage yandere.re

to start import ``rule34Python``
#### page example
```shell


import yandereRe

r = yandereRe.getArtists(page=6)

print(f"""
name: {r.name}
id: {r.id}
group_id: {r.group_id if r.group_id else 'no tiene grupo'}
urls: {'\n'.join(r.urls.split()) if r.urls else 'no tiene links puestos'}
""")
```
#### name example
```shell
#page example

import yandereRe

r = yandereRe.getArtists(name= "neko-baka")

print(f"""
name: {r.name}
id: {r.id}
group_id: {r.group_id if r.group_id else 'no tiene grupo'}
urls: {'\n'.join(r.urls.split()) if r.urls else 'no tiene links puestos'}
""")
```
## New yandere.re

the functions in yandere.re are as follows:

### Search

find a name specific to your taste 

requirements | descriptions
---|---
limit| is the limit of images to be sent
tags [optional]| will be the content that will be searched in the api to return the link.

### random_post

search for an allatory publication
requirements | descriptions
---|---
limit| is the limit of images to be sent

### Search Artist

search artist you want or one alatorio de yandere.re 
requirements | descriptions
---|---
name |search directly with the user's name on the page
page |search for an alatorian user of the page you posted

## coming soon

### rule34 improvements

improvements | Description
---|---
Deleted Images | get images deleted from the page
 creator_id | get the id of the user who uploaded it
 created_at | show the date of creation of the publication
 
### future functions

pages | Description
---|---
booru | will connect to the booru api