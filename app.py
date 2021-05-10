from sanic import Sanic
from sanic.response import text, json
from service_layer.service import add_energy_source

app=Sanic(__name__)


@app.get("/")
async def hello_world(request):
    return text("hello How are you??")




if __name__ == "__main__":
    app.run(auto_reload=True, debug=True, workers=4)