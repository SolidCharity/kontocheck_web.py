#!/bin/bash
#wget https://www.michael-plugge.de/blz.lut -O ~/pyenv/lib/python3.5/site-packages/kontocheck/data/blz.lut2
wget https://sourceforge.net/projects/kontocheck/files/konto_check-de/6.15/blz.lut2f/download -O ~/pyenv/lib/python3.7/site-packages/kontocheck/data/blz.lut2
head ~/pyenv/lib/python3.7/site-packages/kontocheck/data/blz.lut2 | grep "gueltig vom" > ~/kontocheck/src/version.txt
head ~/pyenv/lib/python3.7/site-packages/kontocheck/data/blz.lut2
~/bin/restart.sh
