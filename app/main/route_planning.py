
import googlemaps
from datetime import datetime, timedelta

gmaps = googlemaps.Client(key='AIzaSyBainUCQKRqOgSDsXOtYqpQDo4gv4fRwQE')


waypoints = ("Nairobi", "Athi river")
"""
results = gmaps.directions(origin = "Juja", destination = "Mombasa", waypoints = waypoints, optimize_waypoints = True,departure_time=datetime.now() + timedelta(hours=24))

#PLOTTING ROUTES ON GOOGLE MAPS
#locations = ["Juja", "Nairobi", "Nanyuki", "Embu","Kitui"]
marker_points = []
waypoints = []

#extract the location points from the previous directions function

for leg in results[0]["legs"]:
    leg_start_loc = leg["start_location"]
    marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
    for step in leg["steps"]:
        end_loc = step["end_location"]
        waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
        
last_stop = results[0]["legs"][-1]["end_location"]
marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')
        
markers = [ "color:blue|size:mid|label:" + chr(65+i) + "|" + r for i, r in enumerate(marker_points)]

result_map = gmaps.static_map(center = waypoints[0], scale=2, zoom=7, size=[640, 640], format="jpg", maptype="roadmap", markers=markers,path="color:0x0000ff|weight:2|" + "|".join(waypoints))
"""
def map_generator(start, stop, *list_waypoints, hours=24):
    waypoints=[i for i in list_waypoints]
    results = gmaps.directions(origin=start, destination=stop, waypoints=waypoints, optimize_waypoints = True, departure_time=datetime.now() + timedelta(hours=hours))
    
    marker_points = []
    waypoints = []
    for leg in results[0]["legs"]:
        leg_start_loc = leg["start_location"]
        marker_points.append(f'{leg_start_loc["lat"]},{leg_start_loc["lng"]}')
        for step in leg["steps"]:
            end_loc = step["end_location"]
            waypoints.append(f'{end_loc["lat"]},{end_loc["lng"]}')
    
    last_stop = results[0]["legs"][-1]["end_location"]
    marker_points.append(f'{last_stop["lat"]},{last_stop["lng"]}')
    
    markers = [ "color:blue|size:small|label:" + chr(65+i) + "|" + r for i, r in enumerate(marker_points)]
    
    result_map = gmaps.static_map(center = waypoints[0], scale=2, zoom=7, size=[640, 640], format="jpg", maptype="roadmap", markers=markers,path="color:0x0000ff|weight:2|" + "|".join(waypoints))
    
    return result_map

rslt_mp = map_generator('juja', 'kitui', *waypoints)




def generate_plots(result_map, map_name=" route_map", no_of_r=1):
    ext=".jpg"
    with open(map_name + ext, "wb") as img:
        for chunk in result_map:
            img.write(chunk)
            
generate_plots(rslt_mp)

import os
import re



    
#locate file folder
def file_loc(folder):
    """takes the folder returns a string of it's location"""
    basedir=os.path.dirname(__file__)
    file_folder=os.path.join(basedir,folder)
    if not file_folder.endswith('/'):
        return file_folder + "/"
    else:
        return file_folder

#list file paths
def files_path(file_dir_name):
    """Takes directory and lists the file paths."""
    f_=os.listdir(file_dir_name)
    files_list=[]
    files_names=[]
    for i in f_:
        file_path=os.path.join(file_dir_name,i)
        name=os.path.splitext(i)[0]
        files_list.append(file_path)
        files_names.append(name)
    file_n=list(zip(files_list,files_names))
    return file_n

#print(files_path(f))