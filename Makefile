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

staked-mlp:
	@python3 ./src/scripts/mlp.py staked-mlp | jq > data/fantom-staked-mlp-results.json

staked-mpx:
	@python3 ./src/scripts/mlp.py staked-mpx | jq > data/fantom-staked-mpx-results.json
