@CURRENT_USER="$(shell id -u):$(shell id -g)"

build:
	docker-compose build

#как запускать от текущего пользователя?
#run:
#	CURRENT_USER=$(CURRENT_USER) docker-compose \
#		-f docker-compose.yml -f docker-compose.config.yml \
#		run hexdownloader

run:
	docker-compose \
		-f docker-compose.yml -f docker-compose.config.yml \
		run hexdownloader

run_update:
	docker-compose \
		-f docker-compose.yml -f docker-compose.config.yml \
		run hexdownloader --update

