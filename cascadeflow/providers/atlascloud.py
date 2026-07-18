"""Atlas Cloud provider implementation.

Atlas Cloud exposes an OpenAI-compatible chat completions API, so the provider
reuses the OpenAI provider implementation with Atlas-specific defaults.

Environment Variables:
    ATLASCLOUD_API_KEY: Your Atlas Cloud API key

Models:
    - qwen/qwen3.5-flash: Fast default chat model
    - deepseek-ai/deepseek-v4-pro: Reasoning-capable chat model
"""

import os
from typing import Optional

from .openai import OpenAIProvider


class AtlasCloudProvider(OpenAIProvider):
    """Atlas Cloud provider using the OpenAI-compatible API."""

    BASE_URL = "https://api.atlascloud.ai/v1"

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        **kwargs,
    ):
        """
        Initialize Atlas Cloud provider.

        Args:
            api_key: Atlas Cloud API key (defaults to ATLASCLOUD_API_KEY env var)
            base_url: Custom base URL (defaults to Atlas Cloud API)
            **kwargs: Additional OpenAI provider options
        """
        atlascloud_api_key = api_key or os.getenv("ATLASCLOUD_API_KEY")

        if not atlascloud_api_key:
            raise ValueError(
                "Atlas Cloud API key not found. "
                "Set ATLASCLOUD_API_KEY environment variable or pass api_key parameter."
            )

        super().__init__(api_key=atlascloud_api_key, **kwargs)
        self.base_url = base_url or self.BASE_URL

    @property
    def name(self) -> str:
        """Provider name."""
        return "atlascloud"
