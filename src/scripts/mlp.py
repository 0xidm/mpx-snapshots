import os
import json
import logging

from dotenv import load_dotenv
import click
from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware, geth_poa_middleware

from chaino.utils import init_logger
from chaino.scheduler.call import CallScheduler
from chaino.rpc import RPC

# Fantom Parameters

fantom_snapshot_block = 64884840
with open("data/fantom-addresses.json", "r") as f:
    fantom_addresses = json.load(f)

# https://ftm.guru/rpc.html
fantom_w3 = Web3(HTTPProvider("https://1rpc.io/ftm"))
fantom_w3.middleware_onion.add(simple_cache_middleware)
fantom_rpc = RPC(fantom_w3, slow_timeout=60, tick_delay=0.2, num_threads=2)

# Binance Parameters

bsc_snapshot_block = 0
with open("data/bsc-addresses.json", "r") as f:
    bsc_addresses = json.load(f)

bsc_w3 = Web3(HTTPProvider("https://bsc-dataseed1.binance.org/"))
bsc_w3.middleware_onion.add(simple_cache_middleware)
bsc_w3.middleware_onion.inject(geth_poa_middleware, layer=0)
bsc_rpc = RPC(bsc_w3, slow_timeout=60, tick_delay=0.2, num_threads=2)


@click.group()
def cli():
    pass

@cli.command()
def fantom_staked_mpx():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_mpx_erc20():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x66eEd5FF1701E6ed8470DC391F05e27B1d0657eb",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_mlp_erc20():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xd5c313DE2d33bf36014e6c659F13acE112B80a8E",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_staked_mlp():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x49A97680938B4F1f73816d1B70C3Ab801FAd124B",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_staked_mpx():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="stakedAmounts(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_equalizer_wftm_mpx():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xdE26e98d868FE02fFfb6DF26E638995124d3Ca13",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))

@cli.command()
def fantom_equalizer_gauge():
    print(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x27F7cf5e918311AAF5E7185b5BcDAc158dFacf53",
        function_signature="balanceOf(address)(uint256)",
        addresses=addresses,
        block_number=snapshot_block
    ))


if __name__ == '__main__':
    init_logger(level="INFO")
    load_dotenv()
    cli()
