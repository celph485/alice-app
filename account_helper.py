from config import get_logger
from config import USER_ID
from config import PASSWORD
from config import TWO_FA_CODE
from config import CLIENT_SECRET
from alice_blue import *

log = get_logger(__name__)


def __get_access_token_for_user_id():
    return AliceBlue.login_and_get_access_token(
        username=USER_ID,
        password=PASSWORD,
        twoFA=TWO_FA_CODE,
        api_secret=CLIENT_SECRET
    )


def get_alice_object_for_user_id():
    access_token = __get_access_token_for_user_id()
    return AliceBlue(username=USER_ID, password=PASSWORD, access_token=access_token)
