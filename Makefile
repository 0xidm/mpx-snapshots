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

fantom:
	python3 ./src/scripts/fantom-blocks.py

fantom-import:
	python3 ./src/scripts/fantom-import.py
