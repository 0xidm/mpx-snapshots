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

fantom-mpx-erc20:
	python3 ./src/scripts/mlp.py fantom-mpx-erc20 | jq > data/fantom-mpx-results.json

fantom-staked-mlp:
	python3 ./src/scripts/mlp.py fantom-staked-mlp | jq > data/fantom-staked-mlp-results.json

fantom-staked-mpx:
	python3 ./src/scripts/mlp.py fantom-staked-mpx | jq > data/fantom-staked-mpx-results.json

fantom-equalizer-lp:
	python3 ./src/scripts/mlp.py fantom-equalizer-wftm-mpx | jq > data/fantom-equalizer-wftm-mpx-results.json

fantom-equalizer-gauge:
	python3 ./src/scripts/mlp.py fantom-equalizer-gauge | jq > data/fantom-equalizer-gauge-results.json
