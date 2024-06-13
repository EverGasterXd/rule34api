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

## Installation
```shell
pip install rule34Py
```
## Usage
to start import ``rule34Python`` 

```shell
from rule34Python import rule34

Rule34 = rule34.search("catgirl", limit=3)

print(Rule34)
```

## Rule34

the functions in rule34 are as follows:

### Search
requirements | descriptions
---|---
limit| is the limit of images to be sent
tags | will be the content that will be searched in the api to return the link.

### random_post
requirements | descriptions
---|---
limit| is the limit of images to be sent

will be the content that will be searched in the api to return the link.

## coming soon

### rule34 improvements
improvements | Description
---|---
Deleted Images | get images deleted from the page
Comments | get comments of the image that is being called up
 creator_id | get the id of the user who uploaded it
 created_at | show the date of creation of the publication
 
### future functions

pages | Description
---|---
booru | will connect to the booru api
yandere.re | connect to the yandere.re api