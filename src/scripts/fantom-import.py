import os
import logging

from chaino.nested_filestore import NestedFilestore
from chaino.utils import init_logger


def main():
    init_logger(level="INFO")

    filestore = NestedFilestore("/Volumes/tmp/fantom", [4, 3, 2])

    block_start = 56889636
    block_end = 65653613

    for index in range(block_start, block_end):
        src_filename = f"/tmp/fantom/fantom-block-{index}.pkl"
        dst_filename = None
        if os.path.exists(src_filename):
            dst_filename = filestore.put(src_filename, index)
            if not dst_filename:
                logging.getLogger("chaino").error(f"Failed to put {src_filename} as {dst_filename}")
        else:
            logging.getLogger("chaino").error(f"File not found: {src_filename}")


if __name__ == "__main__":
    main()
