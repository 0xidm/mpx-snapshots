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

fantom: fantom-mpx-erc20 fantom-staked-mlp fantom-staked-mpx fantom-equalizer-lp fantom-equalizer-gauge-1 fantom-equalizer-gauge-2 fantom-fvm-gauge fantom-fvm-lp fantom-mpx-erc20-current
	@echo ok

fantom-mpx-erc20:
	./bin/snapshot.py fantom-mpx-erc20 | jq > data/fantom-mpx.json

fantom-staked-mlp:
	./bin/snapshot.py fantom-staked-mlp | jq > data/fantom-staked-mlp.json

fantom-staked-mpx:
	./bin/snapshot.py fantom-staked-mpx | jq > data/fantom-staked-mpx.json

fantom-equalizer-lp:
	./bin/snapshot.py fantom-equalizer-wftm-mpx | jq > data/fantom-equalizer-wftm-mpx.json

fantom-equalizer-gauge-1:
	./bin/snapshot.py fantom-equalizer-gauge-1 | jq > data/fantom-equalizer-gauge-1.json

fantom-equalizer-gauge-2:
	./bin/snapshot.py fantom-equalizer-gauge-2 | jq > data/fantom-equalizer-gauge-2.json

fantom-fvm-lp:
	./bin/snapshot.py fantom-fvm-lp | jq > data/fantom-fvm-lp.json

fantom-fvm-gauge:
	./bin/snapshot.py fantom-fvm-gauge | jq > data/fantom-fvm-gauge.json

fantom-mpx-erc20-current:
	./bin/snapshot.py fantom-mpx-erc20-current | jq > data/fantom-mpx-current.json

###
# Binance

bsc: bsc-mpx-erc20 bsc-thena-lp bsc-thena-gauge
	@echo ok

bsc-thena-lp:
	./bin/snapshot.py bsc-thena-lp | jq > data/bsc-thena-lp.json

bsc-thena-gauge:
	./bin/snapshot.py bsc-thena-gauge | jq > data/bsc-thena-gauge.json

bsc-mpx-erc20:
	./bin/snapshot.py bsc-mpx-erc20 | jq > data/bsc-mpx-erc20.json
