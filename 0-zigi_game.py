import time

def ziggi_game(str):
    whitespace = 0
    direction = 1
    while True:
        try:
            space_str = ' ' * whitespace
            print(space_str + "*" * 10 + space_str[::-1])
            time.sleep(0.2)
            whitespace += direction
            if whitespace == 20:
                direction = -1
            elif whitespace == 0:
                direction = 1
        except KeyboardInterrupt:
            print("\nGame Over.")
            break

ziggi_game('start')
