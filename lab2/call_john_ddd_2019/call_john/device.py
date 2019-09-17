from tdm.lib.device import DddDevice, DeviceAction, DeviceWHQuery, Validity


class CallJohnDevice(DddDevice):

    JOHN = "contact_john"
    LISA = "contact_lisa"
    MARY = "contact_mary"
    ANDY = "contact_andy"

    MOBILE = "mobile"
    WORK = "work"
    HOME = "home"

    PHONE_NUMBERS = {
        JOHN: {
            MOBILE: "0701234567",
            WORK: "0736582934",
            HOME: "031122363"
        },
        LISA: {
            MOBILE: "0709876543",
            WORK: "0763559230",
            HOME: "031749205"
        },
        MARY: {
            MOBILE: "0706574839",
            WORK: "0784736475",
            HOME: "031847528"
            },
        ANDY: None
    }

    CONTACTS = {
        "John": JOHN,
        "Lisa": LISA,
        "Mary": MARY,
        "Andy": ANDY,
    }

    class MakeCall(DeviceAction):
        def perform(self, selected_contact, selected_number):
            contacts = self.device.CONTACTS.get(selected_contact)
            phone = self.device.CONTACTS.get(selected_number)
            return True

    class TellNumber(DeviceWHQuery):
        def perform(self, phone_number_of_contact):
            phone_number = self.device.PHONE_NUMBERS.get(phone_number_of_contact)
            return True

    class PhoneNumberAvailable(Validity):
        def is_valid(self, selected_contact):
            phone_number = self.device.PHONE_NUMBERS.get(selected_contact)
            print(selected_contact)
            print(phone_number)
            if len(phone_number) == 0:
                return True
            else: 
                return False