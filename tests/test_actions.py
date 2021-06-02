import json
import pytest

from rasa_sdk.executor import CollectingDispatcher, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, SessionStarted

from tests.conftest import EMPTY_TRACKER, DID_VALID_IXO_VALID, DID_NOTVALID_IXO_VALID, DID_VALID_IXO_NOTVALID
from actions import actions_didToAddr


async def test_run_empty_tracker(dispatcher, domain):
    tracker = EMPTY_TRACKER
    action = actions_didToAddr.ActionDIDToAddr()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "Failed to find address"
    assert dispatcher.messages[0]["text"][:22] == expected_text
    assert events == expected_events
    
async def test_run_did_valid_ixo_valid(dispatcher, domain):
    tracker = DID_VALID_IXO_VALID
    action = actions_didToAddr.ActionDIDToAddr()
    events = await action.run(dispatcher, tracker, domain)
    expected_address = "ixo19h3lqj50uhzdrv8mkafnp55nqmz4ghc2sd3m48"
    expected_events = [SlotSet('accountAddress', expected_address)]
    expected_text = "Address for DID did:sov:CYCc2xaJKrp8Yt947Nc6jd : ixo19h3lqj50uhzdrv8mkafnp55nqmz4ghc2sd3m48"
    assert dispatcher.messages[0]["text"]== expected_text
    assert events == expected_events
    
async def test_run_did_notvalid_ixo_valid(dispatcher, domain):
    tracker = DID_NOTVALID_IXO_VALID
    action = actions_didToAddr.ActionDIDToAddr()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "Address for DID did:sov:CYCc2xaJKrp8Yt947Nc6je is not found"
    assert dispatcher.messages[0]["text"][:59] == expected_text
    assert events == expected_events
    
async def test_run_did_valid_ixo_notvalid(dispatcher, domain):
    tracker = DID_VALID_IXO_NOTVALID
    action = actions_didToAddr.ActionDIDToAddr()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "Invalid Ixo Network"
    assert dispatcher.messages[0]["text"] == expected_text
    assert events == expected_events