#! /usr/bin/env make

# Run the Python
output.yaml: 995.txt
	python ParseSentences.py 995.txt output.yaml 

# Clean
.Phony: clean
clean: rm -f output.yaml
