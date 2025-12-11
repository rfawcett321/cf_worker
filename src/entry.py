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
        
        if "/secure/" in path:

            r2_bucket = self.env.alltheflags

            country_path = "gb"

            if len(request_country) == 2:
                country_path = request_country + ".svg"
            else:
                return Response("Object not found", status=404)

            r2_pic = await r2_bucket.get(country_path)

            if r2_pic is None:
                return Response("Object not found", status=404)
            
            content = await r2_pic.arrayBuffer()

            headers={
                "Content-Type": "image/svg+xml"
            }

            return Response(content, headers=headers)

    




    
