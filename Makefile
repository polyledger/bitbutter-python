.PHONY: tests coverage

tests:
	nosetests tests --nocapture --nologcapture

coverage:
	nosetests --with-coverage --cover-package=bitbutter tests
	coverage html --include='bitbutter*'

release:
	python setup.py sdist bdist_wheel upload
