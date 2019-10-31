from flask import Flask,request, jsonify
app = Flask(__name__)
from service.check import CheckService
from service.logger import LogService
logger = LogService()
import traceback,json
from route.test_google import google_trends
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
                'taskid': 'str', 'timestr': 'str',
                'period': 'str'
            }
        ):

            response = {
                'code': 10001
            }
            return jsonify(response), status
        else:
            period = data['period']
            google_trend = test.collect(period,data['timestr'])
            #trends = google_trend.to_json(orient='index', force_ascii=False)
            #trends = json.dumps(google_trend, ensure_ascii=False)
            #trends = google_trend.tolist()
            response = {
                'code': 1,
                'msg': google_trend ,
                'taskid': data['taskid'],
            }
            return jsonify(response), status
    except Exception as err:
        status = 500
        logger.error(traceback.format_exc())


    return jsonify(response), status

@app.route('/get_media',methods=['POST'])
def media():
    data = request.get_json()
    logger.info(data)
    response = {}
    status = 200
    try:
        if not CheckService.check_json_key(
            data=data,
            key_dict={
                'taskid': 'str', 'timestr': 'str',
                'period': 'str'
            }
        ):

            response = {
                'code': 10001
            }
            return jsonify(response), status
        else:
            period = data['period']
            '''google_trend = test.collect(period,data['timestr'])
            #trends = google_trend.to_json(orient='index', force_ascii=False)
            #trends = json.dumps(google_trend, ensure_ascii=False)
            #trends = google_trend.tolist()'''
            response = {
                'code': 1,
                'msg': 'node' ,
                'taskid': data['taskid'],
            }
            return jsonify(response), status
    except Exception as err:
        status = 500
        logger.error(traceback.format_exc())


    return jsonify(response), status


@app.route('/runmodel',methods=['POST'])
def run():
    data = request.get_json()
    logger.info(data)
    response = {}
    status = 200
    try:
        if not CheckService.check_json_key(
            data=data,
            key_dict={
                'taskid': 'str', 'timestr': 'str',
                'period': 'str'
            }
        ):

            response = {
                'code': 10001
            }
            return jsonify(response), status
        else:
            '''period = data['period']
            google_trend = test.collect(period,data['timestr'])
            #trends = google_trend.to_json(orient='index', force_ascii=False)
            #trends = json.dumps(google_trend, ensure_ascii=False)
            #trends = google_trend.tolist()'''

            #trends =
            #media =

            #path = model.

            response = {
                'code': 1,
                'img_path': 'path' ,
                'taskid': data['taskid'],
            }
            return jsonify(response), status
    except Exception as err:
        status = 500
        logger.error(traceback.format_exc())


    return jsonify(response), status