from domain.model import EnergySource, energysource_factory
from domain.command import AddEnergySource


def add_energy_source(cmd: AddEnergySource) -> EnergySource:
    return energysource_factory(
        name=cmd.name,
        address=cmd.address,
        energy_type=cmd.energy_type,
        email=cmd.email,
        avg_production=cmd.avg_production,
        payment_duration=cmd.payment_duration,
        payment_type=cmd.payment_type
    )
