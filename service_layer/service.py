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


def update_energy_source(id_: int, validated_data: abstract.UpdateEnergySource) -> None:
    repo = EnergySourceRepo()
    energysource=repo.get(id_)
    print("RESPONSE FROM REPO",energysource,type(energysource),validated_data)



    energy_source=handlers.update_energy_source(
        command.UpdateEnergySource(
            energy_source=energysource,
            name=validated_data.name if validated_data.name else energysource.name,
            address=validated_data.address if validated_data.address else energysource.address ,
            energy_type=validated_data.energy_type if validated_data.energy_type else energysource.energy_type,
            email=validated_data.email if validated_data.email else energysource.email ,
            avg_production=validated_data.avg_production if validated_data.avg_production else energysource.avg_production ,
            payment_duration=validated_data.payment_duration if validated_data.payment_duration else energysource.payment_duration ,
            payment_type=validated_data.payment_type if validated_data.payment_type else energysource.payment_type
        )
    )
    print("Service",energy_source)
    repo.update(id_,energy_source)
    