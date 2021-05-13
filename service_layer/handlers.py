from domain.model import EnergySource, energysource_factory
from domain.command import AddEnergySource, EnergySourceCommand, UpdateEnergyName, UpdateEnergyAddress, UpdateEnergyEmail, UpdateEnergyPayDur, UpdateEnergyPayTyp, UpdateEnergyProd, UpdateEnergyType


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


def update_energy_source(cmd: EnergySourceCommand) -> EnergySource:
    if isinstance(cmd, UpdateEnergyName):
        return cmd.energy_source.update({"name": cmd.name})

    if isinstance(cmd, UpdateEnergyAddress):
        return cmd.energy_source.update({"address": cmd.address})

    if isinstance(cmd, UpdateEnergyType):
        return cmd.energy_source.update({"energy_type": cmd.energy_type})

    if isinstance(cmd, UpdateEnergyEmail):
        return cmd.energy_source.update({"email": cmd.email})

    if isinstance(cmd, UpdateEnergyProd):
        return cmd.energy_source.update({"avg_production": cmd.avg_production})

    if isinstance(cmd, UpdateEnergyPayDur):
        return cmd.energy_source.update({"payment_duration": cmd.payment_duration})

    if isinstance(cmd, UpdateEnergyPayTyp):
        return cmd.energy_source.update({"payment_type": cmd.payment_type})
