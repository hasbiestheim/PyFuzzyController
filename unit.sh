#!/bin/bash
../ctags.sh
python -m unittest discover -v
