import requests

from bs4 import BeautifulSoup

from src.utilities.db import DB


def gen_favicons():
    db = DB()
    banks = db.select("BANK")
    
    errors = []
    
    for bank in banks:
        try:
            url = bank[2]

            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            icon_link = soup.select_one("link[rel*=icon]")["href"]

            if not icon_link.startswith("http"):
                if url[-1] == "/":
                    url = url[:-1]
                if icon_link[0] == "/":
                    icon_link = icon_link[1:]
                icon_link = url + "/" + icon_link

            icon = requests.get(icon_link)
            with open(f"src/assets/{bank[0]}.ico", "wb") as f:
                f.write(icon.content)

        except Exception as e:
            print(e)
            errors.append(bank[0])

    if len(errors) > 0:
        return {"status": "ok", "errors": errors}
    else:
        return {"status": "ok"}
