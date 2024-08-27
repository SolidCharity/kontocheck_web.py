#!/bin/bash
#wget https://www.michael-plugge.de/blz.lut -O ~/pyenv/lib/python3.5/site-packages/kontocheck/data/blz.lut2
export lutpath=$HOME/kontocheck/.venv/lib/python3.11/site-packages/kontocheck/data/blz.lut2
#wget https://sourceforge.net/projects/kontocheck/files/konto_check-de/6.15/blz.lut2f/download -O $lutpath
# see https://www.joonis.de/de/fintech/kontocheck/
wget https://www.joonis.de/files/4/blz.lut -O $lutpath
head $lutpath | grep "gueltig vom" > ~/kontocheck/src/version.txt
head $lutpath
~/bin/restart.sh
