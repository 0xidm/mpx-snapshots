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

fantom-equalizer-gauge-1:
	python3 ./src/scripts/mlp.py fantom-equalizer-gauge-1 | jq > data/fantom-equalizer-gauge-1-results.json

fantom-equalizer-gauge-2:
	python3 ./src/scripts/mlp.py fantom-equalizer-gauge-2 | jq > data/fantom-equalizer-gauge-2-results.json

bsc-thena-gauge:
	python3 ./src/scripts/mlp.py bsc-thena-gauge | jq > data/bsc-thena-gauge-results.json

fantom: fantom-mpx-erc20 fantom-staked-mlp fantom-staked-mpx fantom-equalizer-lp fantom-equalizer-gauge-1 fantom-equalizer-gauge-2
	@echo ok
