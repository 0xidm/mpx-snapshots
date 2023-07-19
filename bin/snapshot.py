#!/usr/bin/env python3

import os
import json
import logging
from pprint import pprint

import click
from web3 import Web3, HTTPProvider
from web3.middleware import simple_cache_middleware, geth_poa_middleware

from chaino.utils import init_logger
from chaino.scheduler.call import CallScheduler
from chaino.rpc import RPC

# Fantom Parameters

fantom_snapshot_block = 64884840
fantom_current_block = 66051446
with open("data/fantom-addresses.json", "r") as f:
    fantom_addresses = json.load(f)

fantom_w3 = Web3(HTTPProvider("https://rpc.ftm.tools"))
fantom_w3.middleware_onion.add(simple_cache_middleware)
fantom_rpc = RPC(fantom_w3, slow_timeout=5, tick_delay=0.1, num_threads=2)

# Binance Parameters

bsc_snapshot_block = 29541500
with open("data/bsc-addresses.json", "r") as f:
    bsc_addresses = json.load(f)

bsc_w3 = Web3(HTTPProvider("https://bsc-dataseed1.binance.org/"))
bsc_w3.middleware_onion.add(simple_cache_middleware)
bsc_w3.middleware_onion.inject(geth_poa_middleware, layer=0)
bsc_rpc = RPC(bsc_w3, slow_timeout=5, tick_delay=0.1, num_threads=2)


@click.group()
def cli():
    pass

###
# Fantom

@cli.command()
def fantom_staked_mpx():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_mpx_erc20():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x66eEd5FF1701E6ed8470DC391F05e27B1d0657eb",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_mlp_erc20():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xd5c313DE2d33bf36014e6c659F13acE112B80a8E",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_staked_mlp():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x49A97680938B4F1f73816d1B70C3Ab801FAd124B",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_staked_mpx():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xa4157E273D88ff16B3d8Df68894e1fd809DbC007",
        function_signature="stakedAmounts(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_equalizer_wftm_mpx():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xdE26e98d868FE02fFfb6DF26E638995124d3Ca13",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_equalizer_gauge_1():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x27F7cf5e918311AAF5E7185b5BcDAc158dFacf53",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_equalizer_gauge_2():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x7778a0B4688321c4E705d4e9F1A072f6F1579Bf8",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_snapshot_block
    ))

@cli.command()
def fantom_fvm_lp():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xF8eed2665FD11a8431fc41b2582fD5E72a1606f0",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_current_block
    ))

@cli.command()
def fantom_fvm_gauge():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0xF89f367E0225fE68c7c28Fad0BaDc7f569987cFe",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_current_block
    ))

@cli.command()
def fantom_mpx_erc20_current():
    pprint(CallScheduler.map_call(
        rpc=fantom_rpc,
        contract_address="0x66eEd5FF1701E6ed8470DC391F05e27B1d0657eb",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in fantom_addresses],
        block_number=fantom_current_block
    ))

###
# Binance

@cli.command()
def bsc_thena_gauge():
    pprint(CallScheduler.map_call(
        rpc=bsc_rpc,
        contract_address="0x0d739cE843d0584aAE800f54685d1fa69cEC1190",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in bsc_addresses],
        block_number=bsc_snapshot_block
    ))

@cli.command()
def bsc_thena_lp():
    pprint(CallScheduler.map_call(
        rpc=bsc_rpc,
        contract_address="0x51BfC6e47c96d2b8c564B0DdD2C44fC03707cdc7",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in bsc_addresses],
        block_number=bsc_snapshot_block
    ))

@cli.command()
def bsc_mpx_erc20():
    pprint(CallScheduler.map_call(
        rpc=bsc_rpc,
        contract_address="0x94C6B279b5df54b335aE51866d6E2A56BF5Ef9b7",
        function_signature="balanceOf(address)(uint256)",
        inputs=[[address] for address in bsc_addresses],
        block_number=bsc_snapshot_block
    ))


if __name__ == '__main__':
    init_logger(level="INFO")
    cli()
