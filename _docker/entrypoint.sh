set -e

python setup.py install
python src/web/page.py &
