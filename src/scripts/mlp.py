#!/usr/bin/env python3

import os
import json

import web3
import click

from dotenv import load_dotenv
from chaino.spider import ChainoSpider


@click.group()
def cli():
    pass

@cli.command(help="Query mLQDR balanceOf amount")
@click.option('--filename', required=True)
def query_mlqdr_balance_of(filename):
    block_number_snapshot = 55592181

    spider = ChainoSpider(
        results_json_filename=filename,
        chain='fantom',
        exit_early=False,
        resume=False,
    )

    with open(os.path.join(os.environ['DATA_PATH'], 'mlqdr-addresses.json'), 'r') as f:
        addresses = json.load(f)

    # contract ABIs
    with open(os.environ['ABI_FILENAME'], 'r') as f:
        abis = json.load(f)

    # mLQDR ERC-20
    contract = spider.w3.eth.contract(
        address=web3.Web3.to_checksum_address('0xca3c69622e22524ff2b6cc24ee7e654bbf91578a'),
        abi=json.dumps([abis["erc20_balance_of"]])
    )

    spider.add_parallel_tasks(
        num_tasks=3,
        task_name_fmt="mlqdr_balance_of_{}",
        method_lambda=lambda address: contract.functions.balanceOf(address),
        addresses=addresses,
        block_identifier=block_number_snapshot,
    )

    spider.run()


@cli.command(help="Query mLQDR balanceOf amount")
@click.option('--filename', required=True)
def query_mlqdr_balance_of(filename):
    block_number_snapshot = 55592181

    spider = ChainoSpider(
        results_json_filename=filename,
        chain='fantom',
        exit_early=False,
        resume=False,
    )

    with open(os.path.join(os.environ['DATA_PATH'], 'mlqdr-addresses.json'), 'r') as f:
        addresses = json.load(f)

    # contract ABIs
    with open(os.environ['ABI_FILENAME'], 'r') as f:
        abis = json.load(f)

    # mLQDR ERC-20
    contract = spider.w3.eth.contract(
        address=web3.Web3.to_checksum_address('0xca3c69622e22524ff2b6cc24ee7e654bbf91578a'),
        abi=json.dumps([abis["erc20_balance_of"]])
    )

    spider.add_parallel_tasks(
        num_tasks=3,
        task_name_fmt="mlqdr_balance_of_{}",
        method_lambda=lambda address: contract.functions.balanceOf(address),
        addresses=addresses,
        block_identifier=block_number_snapshot,
    )

    spider.run()


if __name__ == '__main__':
    load_dotenv()
    cli()
