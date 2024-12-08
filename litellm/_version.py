import importlib_metadata

try:
    version = importlib_metadata.version("litellm")
except Exception:
    version = "0.0.0"
