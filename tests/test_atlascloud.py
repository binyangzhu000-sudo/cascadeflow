"""Tests for Atlas Cloud provider."""

import os
from unittest.mock import patch

import pytest

from cascadeflow.providers import PROVIDER_REGISTRY
from cascadeflow.providers.atlascloud import AtlasCloudProvider


def test_init_with_api_key():
    """Test initialization with explicit API key."""
    provider = AtlasCloudProvider(api_key="atlas-test-key")

    assert provider.api_key == "atlas-test-key"
    assert provider.base_url == "https://api.atlascloud.ai/v1"
    assert provider.name == "atlascloud"


def test_init_from_env():
    """Test initialization from ATLASCLOUD_API_KEY."""
    with patch.dict(os.environ, {"ATLASCLOUD_API_KEY": "atlas-env-key"}, clear=True):
        provider = AtlasCloudProvider()

    assert provider.api_key == "atlas-env-key"
    assert provider.base_url == "https://api.atlascloud.ai/v1"


def test_init_no_api_key():
    """Test initialization fails without Atlas Cloud API key."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="Atlas Cloud API key not found"):
            AtlasCloudProvider()


def test_custom_base_url():
    """Test custom Atlas Cloud-compatible base URL."""
    provider = AtlasCloudProvider(api_key="atlas-test-key", base_url="https://proxy.test/v1")

    assert provider.base_url == "https://proxy.test/v1"


def test_registered_provider():
    """Test Atlas Cloud is registered for cascade agents."""
    assert PROVIDER_REGISTRY["atlascloud"] is AtlasCloudProvider
