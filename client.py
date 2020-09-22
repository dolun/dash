# import json
# import urllib.request as urllib
import requests
import time
import datetime


HOST, PORT, EXT = '127.0.0.1', 8050, 'm1/'
# get the url as a string
url = f'http://{HOST}:{PORT}/{EXT}'


def get_data_to_dict(_url):
    # open url
    data = {"con1": 40, "con2": time.asctime(),
            "con3": '99+66', "con4": 40, "password": "1234"}
    r = requests.get(url=_url, params=data)
    return r.json()
    """
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.Request(_url, data=params,
                                headers={'content-type': 'application/json'})
    print('req:',req)
    oper_url = urllib.urlopen(url)
    data = oper_url.read()
    return json.loads(data)
    if(oper_url.getcode()==200):
        # get data and convert it to dictionary
        data = oper_url.read()
        return json.loads(data)
    else:
       print("Error receiving data", oper_url.getcode())
       return None
    """


if __name__ == '__main__':
    # while True:
    # get the data from the API as a dictionary
    d = get_data_to_dict(url)
    # if exists, recreate the window
    if d is not None:
        # window_from_api = from_dict(d)
        # window_from_api.update_frame()
        # cv2.imshow('Client Window', window_from_api.frame)
        print("data received", d)
    # exit the program by pressing 'q' key
    # if cv2.waitKey(1) & 0xff == ord('q'):
    #     break
