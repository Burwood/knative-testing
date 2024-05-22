import os
import time

from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    sleep_time = os.environ.get('SLEEP_TIME')
    pod_name = os.environ.get('MY_POD_NAME')
    pod_ip = os.environ.get('MY_POD_IP')
    app.logger.info(f"started {pod_name} with IP {pod_ip}")
    time.sleep(int(sleep_time))
    app.logger.info(f"ended {pod_name} with IP {[pod_ip]}")
    return 'Hello {}! Sleep Time {} \n'.format(target, sleep_time)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
