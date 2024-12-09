let coin = 0
input.onGesture(Gesture.Shake, function () {
    music.ringTone(698)
    coin = randint(1, 2)
    if (coin == 1) {
        basic.showLeds(`
            . # # # .
            # . # . #
            # # # # #
            # . # . #
            . # # # .
            `)
    }
    if (coin == 2) {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            `)
    }
    basic.pause(200)
    music.stopAllSounds()
})
