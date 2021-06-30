import json
import pytest

from rasa_sdk.executor import CollectingDispatcher, Tracker
from rasa_sdk.events import SlotSet, ActionExecuted, SessionStarted

from tests.conftest import (
    EMPTY_TRACKER,
    DID_VALID_IXO_VALID,
    DID_NOTVALID_IXO_VALID,
    DID_VALID_IXO_NOTVALID,
    VOTING_BOND_EMPTY_TRACKER,
    VOTING_BOND_INVALID_CHAIN_VALID_BOND,
    VOTING_BOND_VALID_CHAIN_INVALID_BOND,
    VOTING_BOND_VALID_CHAIN_VALID_BOND
)
from custom_actions import (
    actions_didToAddr,
    actions_voting_bond
)


async def test_run_empty_tracker(dispatcher, domain):
    tracker = EMPTY_TRACKER
    action = actions_didToAddr.ActionDIDToAddr()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "This identity None was"
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
    expected_text = "The network was not found"
    assert dispatcher.messages[0]["text"] == expected_text
    assert events == expected_events
    
async def test_run_voting_empty_tracker(dispatcher, domain):
    tracker = VOTING_BOND_EMPTY_TRACKER
    action = actions_voting_bond.ActionVotingBond()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "This bond_state for None was not found"
    assert dispatcher.messages[0]["text"][:38] == expected_text
    assert events == expected_events
    
async def test_run_voting_chain_valid_bond_valid(dispatcher, domain):
    tracker = VOTING_BOND_VALID_CHAIN_VALID_BOND
    action = actions_voting_bond.ActionVotingBond()
    events = await action.run(dispatcher, tracker, domain)
    expected_state = "OPEN"
    expected_events = [SlotSet('bond_state', expected_state)]
    expected_text = "Bond State for Bond DID did:ixo:49BSStn5nAwrfZwvGT6HFa : OPEN"
    assert dispatcher.messages[0]["text"]== expected_text
    assert events == expected_events
    
async def test_run_voting_chain_valid_bond_notvalid(dispatcher, domain):
    tracker = VOTING_BOND_VALID_CHAIN_INVALID_BOND
    action = actions_voting_bond.ActionVotingBond()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "State for Bond DID:  did:ixo:49BSStn5nAwrfZwvGT6HFb is not found"
    assert dispatcher.messages[0]["text"] == expected_text
    assert events == expected_events
    
async def test_run_voting_chain_notvalid_bond_valid(dispatcher, domain):
    tracker = VOTING_BOND_INVALID_CHAIN_VALID_BOND
    action = actions_voting_bond.ActionVotingBond()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = None
    expected_text = "The network was not found"
    assert dispatcher.messages[0]["text"] == expected_text
    assert events == expected_events