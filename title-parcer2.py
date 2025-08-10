from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html = page.read().decode()

pattern = "<title.*?>.*?</title.*?>"

result = re.search(pattern,html,re.IGNORECASE)
title = result.group()
title = re.sub("<.*?>","",title)

print(title)
