import mechanicalsoup

url = "http://olympus.realpython.org/login"

with mechanicalsoup.Browser() as browser:
    page = browser.get(url)

    html = page.soup

    form = html.select("form")[0]
    for t in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
        for h in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
            for u in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                for n in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                    for d in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                        for e in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                            for r in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                                for D in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                                    for U in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                                        for dd in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":
                                            for E in "poiuytrewqlkjhgfdsasmnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ":

                                                form.select("input")[0]["value"] = "zeus"
                                                form.select("input")[1]["value"] = t+h+u+n+d+e+r+D+U+dd+E

                                                logged = browser.submit(form,page.url)

                                                print(t+h+u+n+d+e+r+D+U+dd+E)
                                                print(logged.url)