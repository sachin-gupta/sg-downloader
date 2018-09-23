init:
	pip install -r requirements.txt

docs:
    cd docs
	rmdir /S /Q _build
	make clean
	make html
	cd ..

test:
	nosetests tests

pack:
    rmdir /S /Q dist
	rmdirs /S /Q sg_downloader.egg-info
    python setup.py sdist
