from domain.model import EnergySource, energysource_factory
from domain.command import AddEnergySource, EnergySourceCommand, UpdateEnergyName, UpdateEnergyAddress, UpdateEnergyEmail, UpdateEnergyPayDur, UpdateEnergyPayTyp, UpdateEnergyProd, UpdateEnergyType
from domain.command import UpdateEnergySource

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
    print("Handler")
    if isinstance(cmd, UpdateEnergySource):
        return cmd.energy_source.update({"name": cmd.name,
                                "address": cmd.address,
                                "energy_type": cmd.energy_type,
                                "email": cmd.email,
                                "avg_production": cmd.avg_production,
                                "payment_duration": cmd.payment_duration,
                                "payment_type": cmd.payment_type
                                    })

# # if isinstance(cmd, UpdateEnergyAddress):
#     cmd.energy_source.update({"address": cmd.address})

# # if isinstance(cmd, UpdateEnergyType):
#     cmd.energy_source.update({"energy_type": cmd.energy_type})

# # if isinstance(cmd, UpdateEnergyEmail):
#     cmd.energy_source.update({"email": cmd.email})

# # if isinstance(cmd, UpdateEnergyProd):
#     cmd.energy_source.update({"avg_production": cmd.avg_production})

# # if isinstance(cmd, UpdateEnergyPayDur):
#     cmd.energy_source.update({"payment_duration": cmd.payment_duration})

# # if isinstance(cmd, UpdateEnergyPayTyp):
#     cmd.energy_source.update({"payment_type": cmd.payment_type})

    # return cmd.energy_source