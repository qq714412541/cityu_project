from flask import Flask,request, jsonify

app = Flask(__name__)
from service.check import CheckService
from service.logger import LogService
logger = LogService()
import traceback

from test.test_google import google_trends
test = google_trends()


@app.route('/')
def start():
    return 'hello flask'



@app.route('/get_googletrends',methods=['POST'])
def google_trends():
    data = request.get_json()
    logger.info(data)

    response = {}

    status = 200


    try:
        if not CheckService.check_json_key(
            data=data,
            key_dict={
                'taskId': 'str', 'timeStr': 'str',
                'period': 'str'
            }
        ):

            response = {
                'code': 10001
            }
            return jsonify(response), status
        else:
            period = data['period']
            google_trend = test.collect(period)
            response = {

                'code': 1,
                'msg': google_trend,
                'taskid': data['taskid'],
            }
            return jsonify(response), status
    except Exception as err:
        status = 500
        logger.error(traceback.format_exc())




    return jsonify(response), status
