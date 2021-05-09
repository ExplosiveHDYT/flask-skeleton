#ONLY WORKS FOR LINUX BASED SYSTEMS
from os import popen
deploy = popen("echo gunicorn -w 4 -b 0.0.0.0:45454 main:app --reload")