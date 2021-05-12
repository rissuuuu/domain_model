from service_layer import abstract
from service_layer import handlers
from domain import command
from adapters.repository import EnergySourceRepo


def add_energy_source(validated_data: abstract.AddEnergySource) -> None:
    energysource = handlers.add_energy_source(command.AddEnergySource(
        name=validated_data.name,
        address=validated_data.address,
        energy_type=validated_data.energy_type,
        email=validated_data.email,
        avg_production=validated_data.avg_production,
        payment_duration=validated_data.payment_duration,
        payment_type=validated_data.payment_type
    ))
    print(energysource)
    repo = EnergySourceRepo()
    repo.add(energysource)
