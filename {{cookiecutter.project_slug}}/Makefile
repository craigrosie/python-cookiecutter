compile: compile-production compile-develop

compile-production:
	pip-compile requirements.in -r

compile-develop:
	pip-compile dev-requirements.in -rU

develop:
	pip-sync requirements.txt dev-requirements.txt

production:
	pip-sync requirements.txt

outdated:
	pip list -o

test:
	py.test --flake8 --cov .

install:
	pip install -e .

dbuild:
	docker build -t {{cookiecutter.docker_image_name}} .

dclean:
	docker rm -f $(shell docker ps -q -f status=exited) 2> /dev/null || true

drun: dclean
	docker-compose up

