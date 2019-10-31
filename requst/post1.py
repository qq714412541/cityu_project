# -*- coding: utf-8 -*-
import requests, json
COMMON_HEADERS = {
    'Content-Type': 'application/json;charset=utf-8'
}
POST_EXAM_URL = 'http://127.0.0.1:8080/get_googletrends'
task_ID = 'a1111'
APP_KEY = 'e10adc3949ba59abbe56e057f20f883e'
period = '2016-12-14 2017-01-25'

def test_post_exam():
    request = {
        'taskid': task_ID,
        'timestr': 'sad',
        'period': period
    }
    response = requests.post(
        url=POST_EXAM_URL,
        json=request,
        headers=COMMON_HEADERS
    )
    print(response.text)
    print(response)

def test_fundus_image():
    pass
def test_surface_image():
    pass
if __name__ == "__main__":
    test_post_exam()