import os
from openai import AzureOpenAI

def create_azure_openai_client():
    """
    Create an AzureOpenAI client using environment variables:
    - AZURE_OPENAI_API_KEY
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_DEPLOYMENT (optional, for downstream usage)
    - AZURE_OPENAI_API_VERSION (default: '2024-02-01')
    """
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-01")
    if not api_key or not endpoint:
        raise ValueError("AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT must be set in environment variables.")
    return AzureOpenAI(api_key=api_key, azure_endpoint=endpoint, api_version=api_version)
