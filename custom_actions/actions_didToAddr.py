import requests
from rasa_sdk import Tracker, Action
from rasa_sdk.types import DomainDict
from typing import Dict, Text, Any, List
from rasa_sdk.events import SlotSet, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

class ActionDIDToAddr(Action):
    def name(self) -> Text:

        return "action_did_to_addr"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """The custom action will take the ixoNetwork and DID from the chatbot slots and
            sets the accountAddress slot associated with DID in that network if exists
        """
        
        ixoNetwork = tracker.get_slot('ixoNetwork')
        DID = tracker.get_slot('DID')
        accountAddress = None
        status = None
        if ixoNetwork and DID:
            URL = f'https://{ixoNetwork}.ixo.world/didToAddr/{DID}'
            
            with requests.session() as sess:
                try:
                    response = sess.get(URL)
                    status = response.status_code
                    if status == 200:
                        accountAddress = response.json().get('result')
                        dispatcher.utter_message(f'Address for DID {DID} : {accountAddress}')
                        return [SlotSet('accountAddress', accountAddress)]
                    else:
                        dispatcher.utter_message(f'Address for DID {DID} is not found')
                except:
                    dispatcher.utter_message("Invalid Ixo Network")
        else:       
            dispatcher.utter_message(f'Failed to find address because ixoNetwork is {ixoNetwork} and DID is {DID}')
