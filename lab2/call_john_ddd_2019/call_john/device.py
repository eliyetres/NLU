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

    class phone_number_of_contact(DeviceWHQuery):
        def perform(self, selected_contact, selected_number):
            phone_number = self.device.PHONE_NUMBERS[selected_contact][selected_number]
            return [phone_number]

    class PhoneNumberAvailable(Validity):
        def is_valid(self, selected_contact):
            phone_number = self.device.PHONE_NUMBERS[selected_contact]
            if phone_number == None:
                return False
            return True

            """ try:
                print("trying ",selected_contact)
                self.device.PHONE_NUMBERS.get(selected_contact)
                           
            except Exception as e:
                print("FAIL!")
                print(e.args)
                return False
            
            return True  """

    """class BasicActionRecognizer(EntityRecognizer):
        def recognize(self, string, unused_language):
            result = []
            words = string.lower().split()
            for contact in self.device.CONTACT_NUMBERS.keys():
                if contact.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact
                    }
                    result.append(recognized_entity)
            return result """
