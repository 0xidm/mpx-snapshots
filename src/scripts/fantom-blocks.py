import os
import logging

from dotenv import load_dotenv
from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware

from chaino.utils import init_logger
from chaino.scheduler.block import BlockScheduler
from chaino.rpc import RPC


def create_scheduler():
    block_scheduler = BlockScheduler(project_name="fantom", state_path="/tmp/fantom")

    _w3 = Web3(HTTPProvider("https://rpc.ankr.com/fantom"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3, slow_timeout=60, num_threads=2))

    _w3 = Web3(HTTPProvider("https://rpc.ftm.tools"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3, slow_timeout=60, num_threads=8))

    _w3 = Web3(HTTPProvider("https://ftm.sakurarpc.io"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3, slow_timeout=60, num_threads=2))

    _w3 = Web3(HTTPProvider("https://fantom-mainnet.public.blastapi.io"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3))

    _w3 = Web3(HTTPProvider("https://fantom.blockpi.network/v1/rpc/public"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3))

    _w3 = Web3(HTTPProvider("https://endpoints.omniatech.io/v1/fantom/mainnet/public"))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3, slow_timeout=60, num_threads=2))

    _w3 = Web3(HTTPProvider(os.getenv("FANTOM_WEB3_PROVIDER_URI")))
    _w3.middleware_onion.add(simple_cache_middleware)
    block_scheduler.add_rpc(RPC(_w3))

    return block_scheduler

def scrape_range(block_scheduler):
    block_start = 54647659
    block_end = 65653613

    logging.getLogger("chaino").info("Adding tasks")
    for block_identifier in range(block_start, block_end):
        block_scheduler.add_task(block_identifier=block_identifier)

    logging.getLogger("chaino").info("Starting scheduler")
    block_scheduler.start()

def main():
    init_logger(level="INFO")
    block_scheduler = create_scheduler()
    scrape_range(block_scheduler)


if __name__ == "__main__":
    load_dotenv()
    main()
