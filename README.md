# bitbucket_repo_downloader

Download all repositories from the Bitbucket account

## Requirements

* GNU Make >= 4
* Docker >= 19
* Docker-compose >= 1.25

## Development

1. Copy *docker-compose.config.example.yml* and paste as *docker-compose.config.yml*.
2. In *docker-compose.config.example.yml* set your configuration.
3. Run in terminal `make run` for a download all repositories with courses, exercises and challenges.
4. Run in terminal `make update_run` for pull updates from repositories to your machine.
