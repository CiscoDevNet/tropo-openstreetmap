# tropo-openstreetmap

A small example showing use of Tropo WebAPI (Python) and OpenStreetMap's Overpass API to translate an SMS address to a set of lattitude longitude coordinates

Requirements:
- Tropo developer account (free): tropo.com
- Tropo application defined (Web/HTTP API) with inbound SMS phone number provisioned
- Internet reachable web server with WSGI environment provisioned (tested on Ubuntu 15.10, Apache 2.4.12, python 2.7.6, libapache2-mod-wsgi 3.4.4)
- Tropo Python help libraries tropo.py, tropo.pyc: https://github.com/tropo/tropo-webapi-python


# How to Run the Code
- Sign-in and create a new application at Tropo.com
- Choose a unique name for the app, and choose 'Web (HTTP) API' as the Type
- Enter a URL pointing to an internet-reachable, WSGI enabled web server and the Tropo-OSM.wsgi script in this project
- Select a Phone Number/Region for the app's SMS phone number and click Create app
- Ensure tropo.py and tropy.pyc from the Tropo Python SDK library and present in the directory with Tropo-OSM.wsgi
- Send an SMS to the Tropo app number, consisting of a valid, full street address
- If all goes well, OpenStreetMap should return the lattitude and longitude corresponding to the address
