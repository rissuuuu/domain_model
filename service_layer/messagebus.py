from domain import events

class email:
    def send_mail(self,email_id,message):
        #do sth
        pass

def handle(event:events.Evenet):
    for handler in HANDLERS[type(event)]:
        handler(event)


def send_energy_not_produced(event:events.EnergyNotGenerated):
    email.send_mail(
        "rissuuuu@gmail.com",
        "energy you have subscribed is out of generation"
    )





HANDLERS={
    events.EnergyNotGenerated:[send_energy_not_produced],

}