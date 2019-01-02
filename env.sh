#!/bin/bash

function build(){
    conda create -p $PWD/env -y
    conda activate $PWD/env
    conda install --file requirements.txt -y
    pip install --upgrade watchdog # conda forge only has 8.3...need 9.0
}

function teardown(){
    conda deactivate
    conda env remove -p $PWD/env
}