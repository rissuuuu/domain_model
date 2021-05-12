from pydantic.networks import HttpUrl
from sanic import Sanic
from sanic.response import text, json
from service_layer import service
from service_layer import abstract
from sanic.response import HTTPResponse

app=Sanic(__name__)


@app.get("/")
def hello_world(request):
    return text("hello How are you??")

@app.route("/send", methods=['GET', 'POST'])
def add_new_energy(request):
    service.add_energy_source(validated_data=abstract.AddEnergySource(
        name="Amit",
        address="Lalitpur",
        energy_type="Solar",
        email="rissuuuu@gmail.com",
        avg_production="100",
        payment_duration=1,
        payment_type="monthly"
    ))
    return HTTPResponse("success")



if __name__ == "__main__":
    app.run(auto_reload=True, debug=True, workers=4)