#!/bin/bash
kill `ps xaf | grep pyenv | grep -v grep | awk '{print $1}'`
