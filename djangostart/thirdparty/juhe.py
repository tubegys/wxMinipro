#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = 'ba08262e3504aa5e253e29a1be262ab3'
    api = 'http://apis.juhe.cn/simpleWeather/query'
    params = 'city=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print("url: ", url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print("json data: ", json_data)
    result = json_data.get('result')
    print("result: ", result)

    realtime_response = dict()
    realtime_response['temperature'] = result['realtime'].get('temperature')
    realtime_response['humidity'] = result['realtime'].get('humidity')
    realtime_response['info'] = result['realtime'].get('info')
    realtime_response['wid'] = result['realtime'].get('wid')
    realtime_response['direct'] = result['realtime'].get('direct')
    realtime_response['power'] = result['realtime'].get('power')
    realtime_response['aqi'] = result['realtime'].get('aqi')

    return realtime_response


if __name__ == '__main__':
    data = weather('上海')
