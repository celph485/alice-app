from config import get_logger
from account_helper import get_alice_object_for_user_id

log = get_logger(__name__)

log.info('Hello World...')

alice = get_alice_object_for_user_id()

log.info(alice.get_balance())  # get balance / margin limits
log.info(alice.get_profile())  # get profile
log.info(alice.get_daywise_positions())  # get daywise positions
log.info(alice.get_netwise_positions())  # get netwise positions
log.info(alice.get_holding_positions())  # get holding positions
