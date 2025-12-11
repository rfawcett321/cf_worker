from workers import Response, WorkerEntrypoint
import json
import datetime
from urllib.parse import urlparse


class Default(WorkerEntrypoint):
    async def fetch(self, request):

        path = urlparse(request.url).path

        request_headers = dict(request.headers)
        request_country = "the moon"

        if path in ["/", "/secure"]:

            request_time = datetime.datetime.now()
            request_user= "bob"


            if request_headers.get("cf-access-authenticated-user-email") != None :
                request_user = request_headers["cf-access-authenticated-user-email"]

            if request_headers.get("cf-ipcountry") != None :
                request_country = request_headers["cf-ipcountry"]
            
            response_payload = request_user + " authenticated at " + str(request_time) + " from " + request_country


            return Response(response_payload)
        
#        if "/secure/" in path and request_country != "the moon":
#
#            return Response("blah")




    
