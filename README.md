# bitbucket_repo_downloader

Download all repositories from the Bitbucket account

## Requirements

Docker.

## Configure

1. Rename `.env.example` to `.env`

2. Fill `.env` file:

- **bitbucket_username** — your Bitbucket username (not email)
- **bitbucket_app_password** — application password [generated](https://bitbucket.org/account/settings/app-passwords/) for this script. You shouldn't use your actual password.

3. `make build`

## Usage

`make run` — download all repositories with courses, exercises and challenges

`make update_run` — pull updates from repositories to your machine
