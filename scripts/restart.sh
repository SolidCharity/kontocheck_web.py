#!/bin/bash
export domain=`ls ~/doms`
mkdir -p ~/doms/$domain/app-ssl/tmp
touch ~/doms/$domain/app-ssl/tmp/restart.txt
