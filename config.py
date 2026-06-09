import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import streamlit as st
    GEMINI_API_KEY    = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY", ""))
    ANTHROPIC_API_KEY = st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY", ""))
except Exception:
    GEMINI_API_KEY    = os.getenv("GEMINI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

GEMINI_MODEL    = "gemini-2.5-flash-image"
OUTPUT_DIR      = os.path.join(os.path.dirname(__file__), "output")
IMAGE_FORMAT    = "png"
DEFAULT_ASPECT  = "3:4"
BATCH_SIZE      = 4
RANDOM_SEED     = None
ACTIVE_PROVIDER = "pollinations"