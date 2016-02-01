def application(environ, start_response):
    status = '200 OK'
    
    import sys
    import os
    import urllib
    import urllib2
    import json
    import logging
    import requests

    sys.path.append(os.path.dirname(__file__))
    from tropo import Tropo

    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)
    
    logging.basicConfig(filename=os.path.dirname(__file__)+'/app.log',level=logging.DEBUG) 
    
    j = json.loads(request_body)
    initialText = j['session']['initialText']

    res = requests.get("http://nominatim.openstreetmap.org/search?format=json&"+urllib.urlencode({"q": initialText}))

    cont = res.content
    cont = cont[1:-1]
    
    j = json.loads(cont)

    lat = j['lat']
    lon = j['lon']

    t = Tropo()	
    t.say("Lattitude: "+lat)
    t.say("Longitude: "+lon)

    output = t.RenderJson()

    response_headers = [('Content-type', 'application/json'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
