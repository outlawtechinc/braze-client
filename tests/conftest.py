from __future__ import absolute_import

import pytest

from braze.client import BrazeClient


@pytest.fixture
def braze_client():
    return BrazeClient(api_key="API_KEY", use_auth_header=True)


@pytest.fixture(autouse=True)
def no_sleep(mocker, braze_client):
    """Disables actual sleeps, but keeps retry wait logic. Zippy tests!"""
    return mocker.patch.object(
        braze_client._post_request_with_retries.retry, "sleep", return_value=None
    )
