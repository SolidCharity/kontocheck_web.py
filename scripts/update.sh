#!/bin/bash
wget https://www.michael-plugge.de/blz.lut -O ~/pyenv/lib/python3.5/site-packages/kontocheck/data/blz.lut2
head ~/pyenv/lib/python3.5/site-packages/kontocheck/data/blz.lut2 | grep "gueltig vom" > ~/kontocheck/version.txt
head ~/pyenv/lib/python3.5/site-packages/kontocheck/data/blz.lut2
./restart.sh
