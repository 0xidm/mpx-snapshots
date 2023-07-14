import os
import logging
import pickle

from chaino.utils import init_logger


def main():
    init_logger(level="INFO")

    block_start = 56889636
    block_end = 65653613

    fields = [
        "block_id",
        "tx_hash",
        "method",
        "from",
        "to",
        "quantity",
    ]
    print(",".join(fields))

    missing_fh = open("/tmp/fantom-missing.txt", "a")

    for index in range(block_start, block_end):
        src_filename = f"/tmp/fantom/fantom-block-{index}.pkl"
        try:
            block = pickle.load(open(src_filename, "rb"))
            for tx in block.transactions:
                tx_dict = {
                    "block_id": tx["blockNumber"],
                    "tx_hash": tx["hash"].hex(),
                    "method": tx["input"][:10],
                    "from": tx["from"],
                    "to": tx["to"],
                    "quantity": tx["value"],
                }
                print(",".join([str(tx_dict[field]) for field in fields]))
        except FileNotFoundError:
            missing_fh.write(f"{index}\n")
            missing_fh.flush()
    
    missing_fh.close()

if __name__ == "__main__":
    main()
