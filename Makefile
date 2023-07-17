help:
	@echo The following makefile targets are available:
	@echo
	@grep -e '^\w\S\+\:' Makefile | sed 's/://g' | cut -d ' ' -f 1
		
requirements:
	pip install -U pip
	pip install 'git+https://github.com/0xidm/chaino'

clean:
	find . -name '*.pyc' -delete
	rm -rf src/build
	rm -rf src/*.egg-info

all: fantom bsc
	@echo ok

###
# Fantom

fantom: fantom-mpx-erc20 fantom-staked-mlp fantom-staked-mpx fantom-equalizer-lp fantom-equalizer-gauge-1 fantom-equalizer-gauge-2
	@echo ok

fantom-mpx-erc20:
	python3 ./src/scripts/snapshot.py fantom-mpx-erc20 | jq > data/fantom-mpx-results.json

fantom-staked-mlp:
	python3 ./src/scripts/snapshot.py fantom-staked-mlp | jq > data/fantom-staked-mlp-results.json

fantom-staked-mpx:
	python3 ./src/scripts/snapshot.py fantom-staked-mpx | jq > data/fantom-staked-mpx-results.json

fantom-equalizer-lp:
	python3 ./src/scripts/snapshot.py fantom-equalizer-wftm-mpx | jq > data/fantom-equalizer-wftm-mpx-results.json

fantom-equalizer-gauge-1:
	python3 ./src/scripts/snapshot.py fantom-equalizer-gauge-1 | jq > data/fantom-equalizer-gauge-1-results.json

fantom-equalizer-gauge-2:
	python3 ./src/scripts/snapshot.py fantom-equalizer-gauge-2 | jq > data/fantom-equalizer-gauge-2-results.json

###
# Binance

bsc: bsc-mpx-erc20 bsc-thena-lp bsc-thena-gauge
	@echo ok

bsc-thena-lp:
	python3 ./src/scripts/snapshot.py bsc-thena-lp | jq > data/bsc-thena-lp-results.json

bsc-thena-gauge:
	python3 ./src/scripts/snapshot.py bsc-thena-gauge | jq > data/bsc-thena-gauge-results.json

bsc-mpx-erc20:
	python3 ./src/scripts/snapshot.py bsc-mpx-erc20 | jq > data/bsc-mpx-erc20-results.json
