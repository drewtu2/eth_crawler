test:
	python -m unittest discover tests "*_test.py"

clean:
	-rm *.pyc logs/*
	-rm -rf __pycache__
