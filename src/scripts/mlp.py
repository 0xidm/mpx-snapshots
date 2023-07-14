import os
import json
import logging

from dotenv import load_dotenv

from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware

from chaino.utils import init_logger
from chaino.scheduler.call import CallScheduler
from chaino.rpc import RPC


# https://ftm.guru/rpc.html
_w3 = Web3(HTTPProvider("https://1rpc.io/ftm"))
_w3.middleware_onion.add(simple_cache_middleware)
rpc = RPC(_w3, slow_timeout=60, tick_delay=0.25, num_threads=1)


def get_balances(contract_address, addresses, block_number=None):
    call_scheduler = CallScheduler(
        project_name=contract_address,
        state_path="/tmp/fantom-call"
    )
    call_scheduler.add_rpc(rpc)

    for address in addresses:
        call_scheduler.add_task(
            contract_address=contract_address,
            function="balanceOf(address)(uint256)",
            input_value=[address],
            block_number=block_number,
        )

    call_scheduler.start()

def main():
    init_logger(level="INFO")
    snapshot_block = 55592181
    with open("var/fantom-addresses.json", "r") as f:
        addresses = json.load(f)

    # MPX ERC20
    # get_balances(
    #     contract_address="0x66eEd5FF1701E6ed8470DC391F05e27B1d0657eb",
    #     addresses=addresses,
    #     block_number=snapshot_block
    # )

    # MLP ERC20
    get_balances(
        contract_address="0xd5c313DE2d33bf36014e6c659F13acE112B80a8E",
        addresses=addresses,
        block_number=snapshot_block
    )


if __name__ == '__main__':
    load_dotenv()
    main()
