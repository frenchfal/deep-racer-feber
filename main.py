from reward import reward_function;

def main():
    params = {
      "track_width": 60,
      "distance_from_center": 12,
      "is_left_of_center": True,
    }

    reward_function(params)


if __name__ == '__main__':
    main()
