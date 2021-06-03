import os
from pathlib import Path
import pytest
import json

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker

here = Path(__file__).parent.resolve()

EMPTY_TRACKER = Tracker.from_dict(json.load(open(here / "./data/empty_tracker.json")))

DID_VALID_IXO_VALID = Tracker.from_dict(
    json.load(open(here / "./data/did_valid_ixo_valid.json"))
    )

DID_NOTVALID_IXO_VALID = Tracker.from_dict(
    json.load(open(here / "./data/did_notvalid_ixo_valid.json"))
    )

DID_VALID_IXO_NOTVALID = Tracker.from_dict(
    json.load(open(here / "./data/did_valid_ixo_notvalid.json"))
    )

VOTING_BOND_EMPTY_TRACKER = Tracker.from_dict(
    json.load(open(here / "./data/voting_bond_empty_tracker.json"))
)

VOTING_BOND_INVALID_CHAIN_VALID_BOND = Tracker.from_dict(
    json.load(open(here/ "./data/voting_bond_invalid_chain_valid_bond.json"))
)

VOTING_BOND_VALID_CHAIN_INVALID_BOND = Tracker.from_dict(
    json.load(open(here/ "./data/voting_bond_valid_chain_invalid_bond.json"))
)

VOTING_BOND_VALID_CHAIN_VALID_BOND = Tracker.from_dict(
    json.load(open(here/ "./data/voting_bond_valid_chain_valid_bond.json"))
)

@pytest.fixture
def dispatcher():
    return CollectingDispatcher()


@pytest.fixture
def domain():
    return dict()