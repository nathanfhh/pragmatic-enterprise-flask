# For Distroless image, we need to run gunicorn with this script
import re
import sys
from gunicorn.app.wsgiapp import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())

