# -*- coding: utf-8 -*-

from datetime import datetime

import pytest


@pytest.fixture()
def earlier_than_now_timestamp():
    """Timestamp."""
    return int(datetime.timestamp(datetime.now())) - 10
