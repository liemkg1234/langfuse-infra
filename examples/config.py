from config.env import LogLevel, settings
from langfuse import Langfuse

# Config
tracer = Langfuse(
    host=settings.LANGFUSE_HOST,
    public_key=settings.LANGFUSE_PUBLIC_KEY,
    secret_key=settings.LANGFUSE_SECRET_KEY,
    # Environment
    environment=settings.ENV,
    # Debug
    debug=True if settings.LOG_LEVEL == LogLevel.DEBUG else False,
)
