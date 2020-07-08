build:
	docker build -t hexdownloader:latest .

run:
	docker run -it --rm --name hexdownloader \
		-v $(CURDIR):/downloader/repos \
		-v $(HOME)/.ssh:/downloader/.ssh:ro \
		--env-file ./.env \
		hexdownloader:latest

update_run:
	docker run -it --rm --name hexdownloader \
		-v $(CURDIR):/downloader/repos \
		-v $(HOME)/.ssh:/downloader/.ssh:ro \
		--env-file ./.env \
		hexdownloader:latest --update

