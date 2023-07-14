help:
	@echo The following makefile targets are available:
	@echo
	@grep -e '^\w\S\+\:' Makefile | sed 's/://g' | cut -d ' ' -f 1
		
requirements:
	pip install -U pip
	pip install -e ../chaino/src

clean:
	find . -name '*.pyc' -delete
	rm -rf src/build
	rm -rf src/*.egg-info

run:
	./src/scripts/mlp.py query-mlqdr-balance-of --filename ./var/mlqdr-result.json

fantom-blocks:
	@python3 ./src/scripts/fantom-blocks.py

fantom-import:
	@python3 ./src/scripts/fantom-import.py

fantom-txs-csv:
	@python3 ./src/scripts/fantom-txs-csv.py | gzip > var/fantom-txs.csv.gz

fantom-staked-mlp:
	@python3 ./src/scripts/mlp.py staked-mlp | jq > var/fantom-staked-mlp-results.json

fantom-staked-mpx:
	@python3 ./src/scripts/mlp.py staked-mpx | jq > var/fantom-staked-mpx-results.json
