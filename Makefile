BIN := ~/.local/bin/hexdownloader


build:
		docker build -t hexdownloader:latest .

run:
	docker run -it --rm --name hexdownloader \
		-v $(CURDIR):/repos \
		--env-file ./config.env \
		hexdownloader:latest /bin/bash
