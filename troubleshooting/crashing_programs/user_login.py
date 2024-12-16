import logging

# logging.basicConfig(filename="app.log", level=logging.DEBUG)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    level=logging.DEBUG,
)


def user_login(username, password):
    logging.info(f"Attempting to log in user: {username}")

    # ... (some code for authentication)
    authentication_failed = False

    if authentication_failed:
        logging.error(f"Login failed for user: {username}")
    else:
        logging.info(f"Successfully logged in user: {username}")


user_login("myothet", "password")
