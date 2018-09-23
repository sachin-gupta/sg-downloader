init:
	pip install -r requirements.txt

docs:
    cd docs
	make clean > ../log/Sphinx_Clean.log
	make html > ../log/Sphinx_Html.log
	cd ..
test:
	nosetests tests
