import os
import logging

from dotenv import load_dotenv
load_dotenv()

from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware

from chaino.block_scheduler import BlockScheduler


def main():
    _w3 = Web3(HTTPProvider(os.getenv("FANTOM_WEB3_PROVIDER_URI")))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler = BlockScheduler(_w3, chain="fantom", tick_delay=0.05, num_threads=12)

    block_start = 56889636
    block_end = block_start + 1_000_000
    # block_end = 65653613

    logging.getLogger("chaino").info("Adding tasks")
    for block_identifier in range(block_start, block_end):
        block_scheduler.add_task(block_identifier=block_identifier)

    logging.getLogger("chaino").info("Starting scheduler")
    block_scheduler.start()


if __name__ == "__main__":
    main()
