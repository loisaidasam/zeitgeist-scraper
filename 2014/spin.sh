#!/bin/bash

curl -s http://www.brooklynvegan.com/archives/2014/12/spins_top_50_al_1.html | pup '#more text{}' | grep -v '^\s*$' | tail -n 50
