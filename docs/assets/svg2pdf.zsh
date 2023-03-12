#!/bin/zsh

if [ -z $1 ]; then
    cd $(dirname $0)
    list=(*.svg)
fi

for file in $list; do
    cd $(dirname $file)
    inkscape --export-latex $file -o $(basename $file .svg).pdf
done

