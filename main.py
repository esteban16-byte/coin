coin = 0

def on_gesture_shake():
    global coin
    music.ring_tone(698)
    coin = randint(1, 2)
    if coin == 1:
        basic.show_leds("""
            . # # # .
            # . # . #
            # # # # #
            # . # . #
            . # # # .
            """)
    if coin == 2:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            """)
    basic.pause(200)
    music.stop_all_sounds()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
