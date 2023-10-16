import requests
import tempfile
from PIL import Image
from bs4 import BeautifulSoup
from src.utilities.db import DB
from src.utilities.s3 import upload_file


def gen_favicons():
    db = DB()
    banks = db.select("BANK")

    temp_dir = tempfile.TemporaryDirectory()

    errors = []

    for bank in banks:
        try:
            url = bank[2]

            headers = {
                'Host': url.split("/")[2],
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
            }

            session = requests.Session()
            response = session.get(url, headers=headers)

            if response.status_code == 403:
                response = session.get(url, headers=headers)
            
            if response.status_code == 403:
                raise Exception(f"{bank[1]} Rejected connection")

            page = response.content
            soup = BeautifulSoup(page, "html.parser")
            icon_link = soup.select_one("link[rel*=icon]")["href"]

            if not icon_link.startswith("http"):
                if url[-1] == "/":
                    url = url[:-1]
                if icon_link[0] == "/":
                    icon_link = icon_link[1:]
                icon_link = url + "/" + icon_link

            icon = session.get(icon_link)
            with open(f"{temp_dir.name}/{bank[0]}.ico", "wb") as f:
                f.write(icon.content)

            # Change icon size to 30x30
            image = Image.open(f"{temp_dir.name}/{bank[0]}.ico")
            image = image.resize((30, 30))
            image.save(f"{temp_dir.name}/{bank[0]}.ico")

            # Upload to S3
            upload_file(
                f"{temp_dir.name}/{bank[0]}.ico", f"favicon/{bank[0]}.ico")

        except Exception as e:
            print(e)
            errors.append(bank[0])

    temp_dir.cleanup()

    if len(errors) > 0:
        return {"status": "ok", "errors": errors}
    else:
        return {"status": "ok"}
