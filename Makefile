build:
		docker build -t hexdownloader:latest .

run:
	docker run -it --rm --name hexdownloader \
		-v $(CURDIR):/repos \
		-v $(HOME)/.ssh:/downloader/.ssh:ro \
		--env-file ./config.env \
		hexdownloader:latest /bin/bash
