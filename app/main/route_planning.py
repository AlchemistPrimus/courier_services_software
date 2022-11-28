
import googlemaps
from datetime import datetime, timedelta
import os
import re
gmaps = googlemaps.Client(key='AIzaSyBainUCQKRqOgSDsXOtYqpQDo4gv4fRwQE')
#locating parent directory
#WILL BE USED TO SAVE IMAGES   
#locate a directory and add file to it
def folder_loc(folder):
    """takes a folder name(this folder is in parent directory) and return string representation of its location"""
    basedir=os.path.dirname(__file__)
    parent=os.path.dirname(basedir)
    file_folder=os.path.join(parent,folder)
    if not file_folder.endswith('/'):
        return file_folder + "/map_images/"
    else:
        return file_folder
    


#FIND FILES
#list file paths
def find_file(file_dir_name):
    """Takes directory name and returns a list of zip of directory name and file name in that directory."""
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


def generate_plots(result_map, map_name):
    ext=".jpg"
    f_loc=folder_loc('static')
    with open(f_loc + map_name + ext, "wb") as img:
        for chunk in result_map:
            img.write(chunk)
            

