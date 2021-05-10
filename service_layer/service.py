from service_layer.abstract import AddEnergySource
from service_layer.handlers import add_energy_source
from domain.command import AddEnergySource
from adapters.repository import EnergySourceRepo


def add_energy_source(validated_data: AddEnergySource) -> None:
    energysource = add_energy_source(AddEnergySource(
        name=validated_data.name,
        address=validated_data.address,
        energy_type=validated_data.energy_type,
        email=validated_data.email,
        avg_production=validated_data.avg_production,
        payment_duration=validated_data.payment_duration,
        payment_type=validated_data.payment_type
    ))

    repo = EnergySourceRepo()
    repo.add(energysource)
