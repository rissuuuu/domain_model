from pydantic.networks import HttpUrl
from sanic import Sanic
from sanic.response import text, json
from service_layer import handler
from service_layer import abstract
from sanic.response import HTTPResponse
from service_layer import unit_of_work
import asyncio

app = Sanic(__name__)


@app.get("/")
async def hello_world(request):
    return text("hello How are you??")


@app.route("/send", methods=['GET', 'POST'])
async def add_new_energy(request):
    await handler.add_energy_source(validated_data=abstract.AddEnergySource(
        name="Amit",
        address="Lalitpur",
        energy_type="Solar",
        email="rissuuuu@gmail.com",
        avg_production="100",
        payment_duration=1,
        payment_type="monthly"
    ), uow=unit_of_work.EnergyUonitOfWork)
    return HTTPResponse("success")


@app.route("/update", methods=['GET', 'POST'])
async def update_energy(request):
    await handler.update_energy_source(id_=1, validated_data=abstract.UpdateEnergySource(
        name="Rishav"
    ), uow=unit_of_work.UpdateEnergyUonitOfWork)
    return HTTPResponse("success")

if __name__ == "__main__":
    asyncio.run(app(auto_reload=True, debug=True, workers=4))
