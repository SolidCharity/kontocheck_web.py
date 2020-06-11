#!/bin/bash
cd ~
source pyenv/bin/activate
cd doms/kontocheck.py.solidcharity.com/kontocheck/
python3 kontocheck_web.py
deactivate
