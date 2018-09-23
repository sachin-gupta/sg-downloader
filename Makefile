init:
	pip install -r requirements.txt

docs:
    cd docs
	make clean > ../log/Sphinx_Clean.log
	make html > ../log/Sphinx_Html.log
	cd ..

pack:
    python setup.py sdist

test:
	nosetests tests
