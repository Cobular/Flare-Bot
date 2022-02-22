from quart import Quart, make_response, render_template, abort
from dataclasses import dataclass

app = Quart(__name__)

@dataclass
class Page:
    id: str
    status: str

@app.route("/status/<int:bot_id>")
async def status(bot_id: int):
    page = Page(str(bot_id), "Online")
    return await render_template("status.html", page=page)
