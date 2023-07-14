import os
import json
import logging

from dotenv import load_dotenv
import click
from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware

from chaino.utils import init_logger
from chaino.scheduler.call import CallScheduler
from chaino.rpc import RPC


snapshot_block = 64884840
with open("data/fantom-addresses.json", "r") as f:
    addresses = json.load(f)

# https://ftm.guru/rpc.html
_w3 = Web3(HTTPProvider("https://1rpc.io/ftm"))
_w3.middleware_onion.add(simple_cache_middleware)
rpc = RPC(_w3, slow_timeout=60, tick_delay=0.2, num_threads=2)


@click.group()
def cli():
    pass

@cli.command()
def staked_mpx():
    print(map_call(
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def mpx_erc20():
    print(map_call(
        contract_address="0x66eEd5FF1701E6ed8470DC391F05e27B1d0657eb",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def mlp_erc20():
    print(map_call(
        contract_address="0xd5c313DE2d33bf36014e6c659F13acE112B80a8E",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def staked_mlp():
    print(map_call(
        contract_address="0x49A97680938B4F1f73816d1B70C3Ab801FAd124B",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def staked_mpx():
    print(map_call(
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="stakedAmounts(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

def map_call(contract_address, function_signature, addresses, block_number=None):
    call_scheduler = CallScheduler(
        project_name=contract_address,
        state_path="/tmp/fantom-call"
    )
    call_scheduler.add_rpc(rpc)

    for address in addresses:
        call_scheduler.add_task(
            contract_address=contract_address,
            function=function_signature,
            input_value=[address],
            block_number=block_number,
        )

    return call_scheduler.start()

if __name__ == '__main__':
    init_logger(level="INFO")
    load_dotenv()
    cli()
