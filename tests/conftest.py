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

@pytest.fixture
def dispatcher():
    return CollectingDispatcher()


@pytest.fixture
def domain():
    return dict()