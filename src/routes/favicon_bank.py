from fastapi.responses import RedirectResponse, Response

from src.utilities.db import DB


def return_favicon(bank_id):
    # check if the bank exists in the database
    # TODO: cache this in redis
    db = DB();
    banks = db.select("BANK", {"id": bank_id})
    del db
    if len(banks) == 0:
        return Response(status_code=404, content="{\"message\": \"Bank not found\"}")
    # return file
    return RedirectResponse(f"https://findata-assets.s3.amazonaws.com/favicon/{bank_id}.ico")