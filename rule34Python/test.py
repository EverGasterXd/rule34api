import yandereRe

r = yandereRe.getArtists(name= "neko-baka")
s = yandereRe.search(tags="neko", limit=3)
print(f"""
name: {r.name}
id: {r.id}
group_id: {r.group_id if r.group_id else 'no tiene grupo'}
urls: {'\n'.join(r.urls.split()) if r.urls else 'no tiene links puestos'}
""")
