# calculate
def get_distance_from_edge(track_width, distance_from_center, is_on_near_side):
  return track_width / 2 + (-1 if is_on_near_side else 1) * distance_from_center


def reward_function(params):
  import math

  # Read input variables
  ## Track positioning
  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  is_left_of_center = params['is_left_of_center']

  distance_from_left_edge = get_distance_from_edge(
    track_width,
    distance_from_center,
    is_left_of_center
  )

  distance_from_right_edge = get_distance_from_edge(
    track_width,
    distance_from_center,
    not(is_left_of_center)
  )

  print(distance_from_left_edge, distance_from_right_edge)

  ## Track direction
    # waypoints = params['waypoints']
    # closest_waypoints = params['closest_waypoints']
    # heading = params['heading']

    # Initialize the reward with typical value
    # reward = 1.0
  #
    # # Calculate the direction of the center line based on the closest waypoints
    # next_point = waypoints[closest_waypoints[1]]
    # prev_point = waypoints[closest_waypoints[0]]
  #
    # # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    # track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # # Convert to degree
    # track_direction = math.degrees(track_direction)
  #
    # return reward
