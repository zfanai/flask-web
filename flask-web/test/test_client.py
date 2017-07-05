#encoding:utf8

import json
import urllib2,urllib

context={}

def http_post(req_url, args, **opt):
    show_header=opt.get('show_header', False)
    show_data = opt.get('show_data', False)
    pass
    #data = urllib.urlencode({
    #    'flag': 'apply_monitor', 'user_name': 'test15'
    #})
    if args:
        data = urllib.urlencode(args)
    else:
        data=None
    req = urllib2.Request(req_url, data, {'Cookie':context.get('cookie')})
    rsp = urllib2.urlopen(req)
    rv = rsp.read()
    if show_header:
        print 'header:', rsp.headers
    if show_data:
        print 'data:', rv
    return rv

if __name__=='__main__':
    http_post('http://192.168.30.26:8081/xxx', None, show_header=True, show_data=True)