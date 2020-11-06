#! /usr/bin/env make

# Run the Python
output.yaml: 995.txt 996.txt 997.txt 998.txt 999.txt
	python Parsesentences.py output.yaml

# Clean
clean: rm -f output.yml
