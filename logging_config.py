import logging

def setup_logging():
    logging.basicConfig(
        filename="chatbot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

setup_logging()
