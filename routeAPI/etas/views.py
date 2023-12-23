from django.shortcuts import render
from django.http import JsonResponse
import googlemaps
from pytz import timezone
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from etas.models import ETAS
# import maps
API_KEY = 'AIzaSyBK4jB7zPp-GInC4pKMrTmfrllNDWNkLkA'

gmaps = googlemaps.Client(key=API_KEY)
class AppDevClubReviewsView(APIView):
    def get(self, request):
        etas = []
        routes = []
        times = []
        methods = []
        for eta in ETAS.objects.filter():
            etas.append(eta.eta_text)
            methods.append(eta.method_text)
            routes.append(eta.start_text + " -> " + eta.end_text + " @ " + eta.time_text)
        return Response({"eta": etas, "route": routes, "time": times, "method": methods})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        start = request.data['start']
        end = request.data['end']
        # try:
        directions = gmaps.directions(start, end, mode='transit', departure_time=datetime.datetime.now())
        # except:
        #     return Response({"message": "failure"})
        durations = []
        def find_durations(data):
            if isinstance(data, dict):
                if "duration" in data:
                    durations.append(data["duration"])
                for value in data.values():
                    find_durations(value)
            elif isinstance(data, list):
                for item in data:
                    find_durations(item)
                    
        find_durations(directions)
        # if len(durations) == 0:
        #     return Response({"message": "failure"})
        duration = ''
        if len(durations) > 0:
            duration = durations[0]["text"]
        if duration != '':
            new_database_entry = ETAS(eta_text=duration, start_text=start, end_text=end, time_text = datetime.datetime.now(timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S"), method_text='transit')
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})


class CreateWalk(APIView):
    def post(self, request):
        start = request.data['start']
        end = request.data['end']
        # try:
        directions = gmaps.directions(start, end, mode='walking', departure_time=datetime.datetime.now())
        durations = []
        def find_durations(data):
            if isinstance(data, dict):
                if "duration" in data:
                    durations.append(data["duration"])
                for value in data.values():
                    find_durations(value)
            elif isinstance(data, list):
                for item in data:
                    find_durations(item)
                    
        find_durations(directions)
        # if len(durations) == 0:
        #     return Response({"message": "failure"})
        duration = ''
        if len(durations) > 0:
            duration = durations[0]["text"]
        if duration != '':
            new_database_entry = ETAS(eta_text=duration, start_text=start, end_text=end, time_text = datetime.datetime.now(timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S"), method_text='walking')
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})
class CreateBike(APIView):
    def post(self, request):
        start = request.data['start']
        end = request.data['end']
        # try:
        directions = gmaps.directions(start, end, mode='bicycling', departure_time=datetime.datetime.now())
        durations = []
        def find_durations(data):
            if isinstance(data, dict):
                if "duration" in data:
                    durations.append(data["duration"])
                for value in data.values():
                    find_durations(value)
            elif isinstance(data, list):
                for item in data:
                    find_durations(item)
                    
        find_durations(directions)
        # if len(durations) == 0:
        #     return Response({"message": "failure"})
        duration = ''
        if len(durations) > 0:
            duration = durations[0]["text"]
        if duration != '':
            new_database_entry = ETAS(eta_text=duration, start_text=start, end_text=end, time_text = datetime.datetime.now(timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S"), method_text='bicycle')
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})