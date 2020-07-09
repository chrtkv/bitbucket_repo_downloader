# bitbucket_downloader

[![Github Actions Status](../../workflows/Docker/badge.svg)](../../actions)

Download all repositories from the Bitbucket account

## Requirements

* GNU Make >= 4
* Docker >= 19

## Using

Use it with [hexlet exercise kit](https://github.com/Hexlet/hexlet-exercise-kit)

## Development

* clone this repo
* copy *bitbucket.config.example.env* into *bitbucket.config.env* and set your config 
* `make dev_build dev_prepare` for first time
* `make dev_clone` or `make dev_rebase` for run code in a container from local machine
