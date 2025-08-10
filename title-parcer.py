from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

html = page.read().decode()

print(html)
print(html[html.find("<title>")+len("<title>"):html.find("</title>")])
