#!/bin/bash

cat aoty15.html | pup '.product_details json{}' | jq '[.[1:][] | {album: .text, artist: .children[0].text}]'
