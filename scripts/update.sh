#!/bin/bash
export lutpath=$HOME/kontocheck/.venv/lib/python3.11/site-packages/kontocheck/data/blz.lut2
#wget https://www.michael-plugge.de/blz.lut -O $lutpath
#wget https://sourceforge.net/projects/kontocheck/files/konto_check-de/6.15/blz.lut2f/download -O $lutpath
# see https://www.joonis.de/de/fintech/kontocheck/
wget https://www.joonis.de/files/4/blz.lut -O $lutpath
head $lutpath | grep "gueltig vom" > ~/kontocheck/src/version.txt
head $lutpath
~/bin/restart.sh
cd ~/kontocheck
source .venv/bin/activate
pip freeze | grep kontocheck > src/version_py.txt
