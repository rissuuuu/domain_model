from domain import events

class email:
    def send_mail(email_id,message):
        print(f"Event generated {email_id} and {message}")

def handle(event:events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


def send_energy_produced(event:events.EnergySourceCreated):
    email.send_mail(
        "rissuuuu@gmail.com",
        "Rissuuuu created a energy source"
    )

def update_energy_produced(event:events.EnergySourceUpdated):
    email.send_mail(
        "rissuuuu@gmail.com",
        "Rissuuuu updated a energy source"
    )



HANDLERS={
    events.EnergySourceCreated:[send_energy_produced],
    events.EnergySourceUpdated:[update_energy_produced]
}