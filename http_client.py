import http.client
import json


class HttpClient:
    def __init__(self, tcp_ip, tcp_port):
        self.ip = tcp_ip
        self.port = int(tcp_port)

    def http_api_get(self, url):
        conn = http.client.HTTPConnection(self.ip, self.port)
        conn.request("GET", url)
        # conn.set_debuglevel(2)
        r1 = conn.getresponse()
        data1 = r1.read().decode('utf-8')  # This will return entire content.
        jdata = None
        try:
            jdata = json.loads(data1)
        except:
            pass
        print('\nGET data is: {}\nget_status_status is: {}\nget_status reason is: {}\n'.format(jdata, r1.status,
                                                                                      r1.reason))
        conn.close()
        return jdata, r1

    def http_api_post(self, url, data):
        conn = http.client.HTTPConnection(self.ip, self.port)

        print("\nPOST request data is: {}".format(data))
        conn.request("POST", url, body=json.dumps(data).encode('utf-8'),
                     headers={"Content-Type": "application/json"})
        # conn.set_debuglevel(2)
        r1 = conn.getresponse()
        data1 = r1.read().decode('utf-8')  # This will return entire content.
        jdata = None
        try:
            jdata = json.loads(data1)
        except:
            pass
        print('\nPost response data is: {}\npost_status_status is: {}\npost_status reason is: {}\n'.format(jdata,
                                                                                                           r1.status,
                                                                                                           r1.reason))
        conn.close()
        return jdata, r1