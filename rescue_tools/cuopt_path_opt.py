import requests


# Function to calculate emergency weights
def emergency_to_weight(emergency_level, base_penalty=3600, max_penalty=7200):
    """
    Convert emergency level to a weight in seconds.
    
    :param emergency_level: Integer from 1 to 5, where 5 is most urgent
    :param base_penalty: Base penalty in seconds (default 1 hour)
    :param max_penalty: Maximum penalty in seconds (default 2 hours)
    :return: Weight in seconds
    """
    if emergency_level < 1 or emergency_level > 5:
        raise ValueError("Emergency level must be between 1 and 5")
    
    # Invert the emergency level so that higher emergencies get lower weights
    inverted_level = 6 - emergency_level
    
    # Calculate weight: lower emergency levels get higher penalties
    weight = base_penalty + (inverted_level - 1) * (max_penalty - base_penalty) / 4
    
    return int(weight)

# Prepare cost matrix for cuOpt
def create_cost_matrix(coordinates):
    """
    Create a cost matrix assuming direct distances between all points
    
    :param coordinates: List of coordinates [longitude, latitude]
    :return: Cost matrix in cuOpt format
    """
    num_points = len(coordinates)
    cost_matrix = [[0 for _ in range(num_points)] for _ in range(num_points)]
    
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                # Assuming Euclidean distance as cost (you could use Haversine or other distance metrics)
                cost = ((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2) ** 0.5
                cost_matrix[i][j] = cost  
    return cost_matrix


def create_geojson_from_response(response_body, coordinates):
    features = []
    # Create a mapping of task IDs to coordinates
    task_id_to_coords = {f"Task-{i}": coord for i, coord in enumerate(coordinates[1:], start=1)}
    task_id_to_coords["Depot"] = coordinates[0]  # Add depot coordinates

    for vehicle_id, vehicle_data in response_body['response']['solver_infeasible_response']['vehicle_data'].items():
        route_coordinates = []
        for task in vehicle_data['task_id']:
            if task in task_id_to_coords:
                route_coordinates.append(task_id_to_coords[task])
            elif task == 'Break':
                continue  # Skip breaks as they don't have a location

        if route_coordinates:
            feature = {
                "type": "Feature",
                "properties": {
                    "vehicle_id": vehicle_id,
                    "tasks": vehicle_data['task_id'],
                    "arrival_times": vehicle_data['arrival_stamp'],
                    "route_indices": vehicle_data['route'],
                    "task_types": vehicle_data['type']
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": route_coordinates
                }
            }
            features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return geojson



def get_osrm_route(coordinates):
    """
    Get the OSRM route for a list of coordinates.
    """
    coords_str = ';'.join([f"{lon},{lat}" for lon, lat in coordinates])
    url = f"http://router.project-osrm.org/route/v1/driving/{coords_str}?overview=full&geometries=geojson"
    response = requests.get(url)
    return response.json()

def create_geojson_from_cuopt_and_osrm(cuopt_response, coordinates):
    features = []

    # Create a mapping of task IDs to coordinates
    task_id_to_coords = {f"Task-{i}": coord for i, coord in enumerate(coordinates[1:], start=1)}
    task_id_to_coords["Depot"] = coordinates[0]  # Add depot coordinates

    for vehicle_id, vehicle_data in cuopt_response['response']['solver_infeasible_response']['vehicle_data'].items():
        route_coordinates = []
        for task in vehicle_data['task_id']:
            if task in task_id_to_coords:
                route_coordinates.append(task_id_to_coords[task])
            elif task == 'Break':
                continue  # Skip breaks as they don't have a location

        if route_coordinates:
            # Get OSRM route
            osrm_route = get_osrm_route(route_coordinates)
            
            feature = {
                "type": "Feature",
                "properties": {
                    "vehicle_id": vehicle_id,
                    "tasks": vehicle_data['task_id'],
                    "arrival_times": vehicle_data['arrival_stamp'],
                    "route_indices": vehicle_data['route'],
                    "task_types": vehicle_data['type'],
                    "distance": osrm_route['routes'][0]['distance'],
                    "duration": osrm_route['routes'][0]['duration']
                },
                "geometry": osrm_route['routes'][0]['geometry']
            }
            features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return geojson


def generate_cuopt_config(coordinates, cost_matrix, num_vehicles, vehicle_capacity, time_limit, 
                          starting_point_coordinates, ending_point_coordinates, cost_weight, travel_time_weight, 
                          route_size_variance_weight, min_vehicles, max_cost, max_time, fixed_cost):
    
  
    # coordinates = [starting_point_coordinates] + coordinates + [ending_point_coordinates]

    #print(coordinates)

    # Task setup for cuOpt
    task_data = {
        "task_locations": list(range(1, len(coordinates))),
        "task_ids": [f"Task-{i}" for i in range(1, len(coordinates))],
        "demand": [[1 for _ in range(1, len(coordinates))] for _ in range(num_vehicles)],
        "task_time_windows": [[0, time_limit] for _ in range(1, len(coordinates))],
        "service_times": [0 for _ in range(1, len(coordinates))]
    }

   
    #Fleet setup for cuOpt
    fleet_data = {
            "vehicle_locations":  [[0, 1] for _ in range(num_vehicles)],
            "vehicle_ids": [f"veh-{i+1}" for i in range(num_vehicles)],
            "capacities": [[vehicle_capacity for _ in range(num_vehicles)] for _ in range(num_vehicles)],  
            "vehicle_time_windows": [[0, time_limit] for _ in range(num_vehicles)],
            "vehicle_break_time_windows": [[[1, 2] for _ in range(num_vehicles)]],
            "vehicle_break_durations": [[1 for _ in range(num_vehicles)]],
            "vehicle_break_locations": [0, 1],
            "vehicle_types": [1 for _ in range(num_vehicles)],
            "vehicle_order_match": [{"order_ids": [i], "vehicle_id": i} for i in range(num_vehicles)],
            "skip_first_trips": [False for _ in range(num_vehicles)],
            "drop_return_trips": [True for _ in range(num_vehicles)],
            "min_vehicles": min_vehicles,
            "vehicle_max_costs": [max_cost for _ in range(num_vehicles)],
            "vehicle_max_times": [max_time for _ in range(num_vehicles)],
            "vehicle_fixed_costs": [fixed_cost for _ in range(num_vehicles)]
        }


    
    # Combine the data into a single request for cuOpt
    cuopt_request = {
        "action": "cuOpt_OptimizedRouting",
        "data": {
            "cost_waypoint_graph_data": None,
            "travel_time_waypoint_graph_data": None,
            "cost_matrix_data": {
                "data": {str(i+1): cost_matrix for i in range(num_vehicles)}
            },
            "travel_time_matrix_data": {
                "data": {str(i+1): cost_matrix for i in range(num_vehicles)}
            },
            "task_data": task_data,
            "fleet_data": fleet_data,
            "solver_config": {
                "time_limit": time_limit,
                "objectives": {
                    "cost": cost_weight,
                    "travel_time": travel_time_weight,
                    "variance_route_size": route_size_variance_weight,
                    "variance_route_service_time": 0,
                    "prize": 0,
                    "vehicle_fixed_cost": 0
                },
                "verbose_mode": False,
                "error_logging": True
            }
        },
        "parameters": {},
        "client_version": "custom"
    }
  
    return cuopt_request
