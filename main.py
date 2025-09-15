@namespace
class SpriteKind:
    introguy = SpriteKind.create()
    boss = SpriteKind.create()
    bossfire = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.player2.change_life_by(-1)
sprites.on_overlap(SpriteKind.boss, SpriteKind.projectile, on_on_overlap)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . 2 3 2 . . .
            . . . . . . . . . 2 2 . 2 2 . .
            . . . . . . . . . . 2 2 2 . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        ghost,
        -100,
        -100)
    sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . 2 3 2 . . .
            . . . . . . . . . 2 2 . 2 2 . .
            . . . . . . . . . . 2 2 2 . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        ghost,
        -100,
        -100).follow(badsoul, 100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    sprite2.destroy()
sprites.on_overlap(SpriteKind.bossfire, SpriteKind.projectile, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    sprite3.start_effect(effects.disintegrate, 200)
    sprite3.set_position(76, 52)
    sprite3.set_kind(SpriteKind.player)
sprites.on_overlap(SpriteKind.player, SpriteKind.bossfire, on_on_overlap3)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . 2 3 2 . . .
            . . . . . . . . . 2 2 . 2 2 . .
            . . . . . . . . . . 2 2 2 . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        ghost,
        100,
        100)
    sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . 2 3 2 . . .
            . . . . . . . . . 2 2 . 2 2 . .
            . . . . . . . . . . 2 2 2 . . .
            . . . . . . . . . . . 2 . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        ghost,
        100,
        100).follow(badsoul, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap4(sprite4, otherSprite4):
    global index
    sprite4.destroy(effects.fire, 500)
    info.change_score_by(1)
    index += randint(0, 100)
    info.change_life_by(2)
    otherSprite4.destroy()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap4)

def on_on_destroyed(sprite5):
    global ghost
    deathmachine.destroy()
    ghost = sprites.create(img("""
            ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
            """),
        SpriteKind.player)
    animation.run_image_animation(ghost,
        [img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111ffff.....
                ......fffcdb1bc111cf....
                ....fc111cbfbf1b1b1f....
                ....f1b1b1ffffbfbfbf....
                ....fbfbfffffff.........
                .........fffff..........
                ..........fff...........
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """),
            img("""
                ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .....ffff111111bf.......
                ....fc111cdb1bdfff......
                ....f1b1bcbfbfc111cf....
                ....fbfbfbffff1b1b1f....
                .........fffffffbfbf....
                ..........fffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
                """)],
        200,
        True)
    controller.move_sprite(ghost, 150, 150)
    scene.set_background_image(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """))
    game.show_long_text("Oh, you died...that sucks. Wait, you shouldn't be here! Well I can't just let you go, that would be bad for business...I don't know, uh...collect like, i guess 500 souls, and you  can go back",
        DialogLayout.CENTER)
    ghost.set_stay_in_screen(True)
    info.set_life(10)
sprites.on_destroyed(SpriteKind.introguy, on_on_destroyed)

def on_on_created(sprite6):
    effects.clear_particles(sprite6)
sprites.on_created(SpriteKind.player, on_on_created)

def on_on_overlap5(sprite7, otherSprite5):
    main.destroy(effects.spray, 500)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.introguy, on_on_overlap5)

def on_on_overlap6(sprite8, otherSprite6):
    info.change_life_by(-1)
    sprite8.start_effect(effects.disintegrate, 200)
    sprite8.set_position(76, 52)
    sprite8.set_kind(SpriteKind.player)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap6)

projectile3: Sprite = None
Boss: Sprite = None
badsoul: Sprite = None
ghost: Sprite = None
projectile: Sprite = None
main: Sprite = None
deathmachine: Sprite = None
music.wawawawaa.play()
deathmachine = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . 3 3 3 3 3 3 3 3 . .
        . . . . . 3 c 3 3 3 3 3 3 d 3 .
        . . . . 3 c c 3 3 3 3 3 3 d c 3
        . . d 3 d c c 3 d d d d d d c c
        . d 3 3 d c b a a a a a a a 3 c
        . 3 3 3 d b a a b b b a b b a 3
        . 3 3 3 3 3 a b b b b a b b b a
        . 3 3 3 3 a 3 3 3 3 3 a 3 3 3 a
        . 3 d d 3 a f a a a f a a a a a
        . d d 3 a a a f a a f a a a a a
        . a a a a a a a f f f a a a a a
        . a a a a f f f a a a a f f f f
        . . . a f f f f f a a f f f f f
        . . . . f f f f . . . . f f f .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.enemy)
main = sprites.create(img("""
        . . . . 5 5 5 5 . . . . .
        . . 5 5 5 5 5 5 5 5 . . .
        . 5 5 5 5 5 5 2 5 5 5 . .
        5 5 5 5 5 5 2 2 5 5 5 2 8
        5 5 5 2 5 5 5 5 5 5 5 2 .
        2 2 2 5 5 5 3 3 5 5 2 2 .
        5 5 5 5 5 3 3 5 5 2 2 5 .
        5 5 5 b 8 3 3 8 b 5 5 5 .
        . f 3 1 8 3 3 8 1 3 f . .
        . f 3 3 3 3 3 3 3 3 f . .
        . f f f 3 3 3 3 f f f . .
        f 3 f b 7 7 7 7 b 8 3 f .
        3 3 8 7 7 7 7 7 7 8 3 3 .
        3 3 8 6 6 6 6 6 6 8 3 3 .
        . . . 8 8 8 8 8 8 . . . .
        . . . 8 8 . . 8 8 . . . .
        """),
    SpriteKind.introguy)
deathmachine.set_position(139, 57)
deathmachine.follow(main, 200)
controller.move_sprite(main)
index = randint(0, 499)

def on_forever():
    if index == 500:
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.run_image_animation(main,
            [img("""
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . . f f
                    . . f 4 5 5 f f 5 5 6 f . f 5 f
                    . . . f 6 6 6 6 6 6 4 4 f 5 5 f
                    . . . f 4 5 5 5 5 5 5 4 4 5 f .
                    . . . f 5 5 5 5 5 4 5 5 f f . .
                    . . . f 5 f f f 5 f f 5 f . . .
                    . . . f f . . f f . . f f . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 4 4 5 f .
                    . . . f 5 5 5 5 5 5 5 f f f . .
                    . . . f 5 4 5 f f f 5 f . . . .
                    . . . f f f f f . . f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 f 5 5 f .
                    . . . f 5 5 5 5 5 5 5 4 5 f . .
                    . . . . f 5 4 5 f 5 f f f . . .
                    . . . . . f f f f f f f . . . .
                    """)],
            500,
            True)
        pause(5000)
        game.over(True, effects.smiles)
forever(on_forever)

def on_update_interval():
    global badsoul
    if info.score() == 2000:
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.run_image_animation(main,
            [img("""
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . . f f
                    . . f 4 5 5 f f 5 5 6 f . f 5 f
                    . . . f 6 6 6 6 6 6 4 4 f 5 5 f
                    . . . f 4 5 5 5 5 5 5 4 4 5 f .
                    . . . f 5 5 5 5 5 4 5 5 f f . .
                    . . . f 5 f f f 5 f f 5 f . . .
                    . . . f f . . f f . . f f . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 4 4 5 f .
                    . . . f 5 5 5 5 5 5 5 f f f . .
                    . . . f 5 4 5 f f f 5 f . . . .
                    . . . f f f f f . . f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 f 5 5 f .
                    . . . f 5 5 5 5 5 5 5 4 5 f . .
                    . . . . f 5 4 5 f 5 f f f . . .
                    . . . . . f f f f f f f . . . .
                    """)],
            500,
            True)
        pause(5000)
        game.over(True, effects.smiles)
    if info.life() == 500:
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.run_image_animation(main,
            [img("""
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . . f f
                    . . f 4 5 5 f f 5 5 6 f . f 5 f
                    . . . f 6 6 6 6 6 6 4 4 f 5 5 f
                    . . . f 4 5 5 5 5 5 5 4 4 5 f .
                    . . . f 5 5 5 5 5 4 5 5 f f . .
                    . . . f 5 f f f 5 f f 5 f . . .
                    . . . f f . . f f . . f f . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 4 4 5 f .
                    . . . f 5 5 5 5 5 5 5 f f f . .
                    . . . f 5 4 5 f f f 5 f . . . .
                    . . . f f f f f . . f f . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . 4 4 4 . . . . 4 4 4 . . . .
                    . 4 5 5 5 e . . e 5 5 5 4 . . .
                    4 5 5 5 5 5 e e 5 5 5 5 5 4 . .
                    4 5 5 4 4 5 5 5 5 4 4 5 5 4 . .
                    e 5 4 4 5 5 5 5 5 5 4 4 5 e . .
                    . e e 5 5 5 5 5 5 5 5 e e . . .
                    . . e 5 f 5 5 5 5 f 5 e . . . .
                    . . f 5 5 5 4 4 5 5 5 f . f f .
                    . . . 4 5 5 f f 5 5 6 f f 5 f .
                    . . . f 6 6 6 6 6 6 4 f 5 5 f .
                    . . . f 5 5 5 5 5 5 5 4 5 f . .
                    . . . . f 5 4 5 f 5 f f f . . .
                    . . . . . f f f f f f f . . . .
                    """)],
            500,
            True)
        pause(5000)
        game.over(True, effects.smiles)
    badsoul = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . 4 4 4 4 . . . . . .
            . . . . 4 4 4 5 5 4 4 4 . . . .
            . . . 3 3 3 3 4 4 4 4 4 4 . . .
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
            . . . 4 2 2 2 2 2 2 2 2 4 . . .
            . . . . 4 4 2 2 2 2 4 4 . . . .
            . . . . . . 4 4 4 4 . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    animation.run_image_animation(badsoul,
        [img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 f f f 2 2 f f f 5 4 . .
                . 4 3 3 f 2 f 2 2 f 2 f 5 4 4 .
                . 4 3 3 f f f 2 4 f f f 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 2 4 3 3 3 4 . . . .
                . . . 4 2 2 3 3 3 3 3 3 3 . . .
                . . 4 2 f f f 3 3 f f f 3 4 . .
                . . 4 2 f 2 f 2 2 f 2 f 3 4 . .
                . 4 2 2 f f f 2 2 f f f 3 4 4 .
                . 4 2 2 2 4 4 4 2 2 2 2 4 5 4 .
                . 4 2 2 4 4 4 4 4 2 2 2 4 5 4 .
                . 4 2 2 4 4 4 4 4 2 2 2 4 4 4 .
                . . 4 2 4 4 4 4 4 2 1 1 4 4 . .
                . . 4 2 2 4 4 4 4 5 1 1 4 4 . .
                . . . 4 4 2 4 4 5 5 5 4 4 . . .
                . . . . 4 4 4 4 4 4 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . 4 4 f f f 4 2 f f f 2 4 . .
                . . 4 2 f 2 f 4 4 f 2 f 2 4 . .
                . 4 4 4 f f f 4 4 f f f 3 2 4 .
                . 4 4 4 4 4 4 4 4 2 2 3 3 4 4 .
                . 4 4 5 4 4 4 4 2 2 2 3 3 3 4 .
                . 4 4 5 5 2 2 2 2 2 3 3 3 3 4 .
                . . 4 5 1 1 2 2 2 3 3 3 3 3 . .
                . . 4 4 1 1 2 2 2 3 3 3 3 4 . .
                . . . 4 4 4 4 4 4 3 3 3 3 . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 4 4 4 4 4 . . . .
                . . . 4 4 5 5 5 4 4 2 4 4 . . .
                . . 4 4 f f f 4 4 f f f 2 4 . .
                . . 4 4 f 2 f 4 4 f 2 f 2 4 . .
                . 4 4 4 f f f 4 4 f f f 2 2 4 .
                . 4 5 4 2 2 2 4 4 4 4 4 2 2 4 .
                . 4 5 4 2 2 2 2 4 4 4 2 2 2 4 .
                . 4 4 3 3 3 2 2 2 2 2 2 2 2 4 .
                . . 4 3 3 3 3 2 2 2 3 3 2 4 . .
                . . 4 3 3 3 3 3 3 3 3 2 2 4 . .
                . . . 3 3 3 3 3 3 3 2 2 4 . . .
                . . . . 4 3 3 3 4 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """)],
        100,
        True)
    badsoul.follow(ghost, 50)
    badsoul.set_position(182, randint(-100, 118))
    if info.score() == 10:
        badsoul = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . 4 4 4 5 5 4 4 4 . . . .
                . . . 3 3 3 3 4 4 4 4 4 4 . . .
                . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                . . . 4 2 2 2 2 2 2 2 2 4 . . .
                . . . . 4 4 2 2 2 2 4 4 . . . .
                . . . . . . 4 4 4 4 . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            SpriteKind.enemy)
        animation.run_image_animation(badsoul,
            [img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . 4 4 4 5 5 4 4 4 . . . .
                    . . . 3 3 3 3 4 4 4 4 4 4 . . .
                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                    . . 3 3 f f f 2 2 f f f 5 4 . .
                    . 4 3 3 f 2 f 2 2 f 2 f 5 4 4 .
                    . 4 3 3 f f f 2 4 f f f 5 4 4 .
                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                    . . . 4 2 2 2 2 2 2 2 2 4 . . .
                    . . . . 4 4 2 2 2 2 4 4 . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . 4 4 2 4 3 3 3 4 . . . .
                    . . . 4 2 2 3 3 3 3 3 3 3 . . .
                    . . 4 2 f f f 3 3 f f f 3 4 . .
                    . . 4 2 f 2 f 2 2 f 2 f 3 4 . .
                    . 4 2 2 f f f 2 2 f f f 3 4 4 .
                    . 4 2 2 2 4 4 4 2 2 2 2 4 5 4 .
                    . 4 2 2 4 4 4 4 4 2 2 2 4 5 4 .
                    . 4 2 2 4 4 4 4 4 2 2 2 4 4 4 .
                    . . 4 2 4 4 4 4 4 2 1 1 4 4 . .
                    . . 4 2 2 4 4 4 4 5 1 1 4 4 . .
                    . . . 4 4 2 4 4 5 5 5 4 4 . . .
                    . . . . 4 4 4 4 4 4 4 4 . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . 4 4 2 2 2 2 4 4 . . . .
                    . . . 4 2 2 2 2 2 2 2 2 4 . . .
                    . . 4 4 f f f 4 2 f f f 2 4 . .
                    . . 4 2 f 2 f 4 4 f 2 f 2 4 . .
                    . 4 4 4 f f f 4 4 f f f 3 2 4 .
                    . 4 4 4 4 4 4 4 4 2 2 3 3 4 4 .
                    . 4 4 5 4 4 4 4 2 2 2 3 3 3 4 .
                    . 4 4 5 5 2 2 2 2 2 3 3 3 3 4 .
                    . . 4 5 1 1 2 2 2 3 3 3 3 3 . .
                    . . 4 4 1 1 2 2 2 3 3 3 3 4 . .
                    . . . 4 4 4 4 4 4 3 3 3 3 . . .
                    . . . . 4 4 4 5 5 4 4 4 . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . 4 4 4 4 4 4 4 4 . . . .
                    . . . 4 4 5 5 5 4 4 2 4 4 . . .
                    . . 4 4 f f f 4 4 f f f 2 4 . .
                    . . 4 4 f 2 f 4 4 f 2 f 2 4 . .
                    . 4 4 4 f f f 4 4 f f f 2 2 4 .
                    . 4 5 4 2 2 2 4 4 4 4 4 2 2 4 .
                    . 4 5 4 2 2 2 2 4 4 4 2 2 2 4 .
                    . 4 4 3 3 3 2 2 2 2 2 2 2 2 4 .
                    . . 4 3 3 3 3 2 2 2 3 3 2 4 . .
                    . . 4 3 3 3 3 3 3 3 3 2 2 4 . .
                    . . . 3 3 3 3 3 3 3 2 2 4 . . .
                    . . . . 4 3 3 3 4 2 4 4 . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    """)],
            100,
            True)
        badsoul.set_position(randint(100, 200), randint(-100, 1))
        if info.score() == 20:
            badsoul = sprites.create(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . 4 4 4 5 5 4 4 4 . . . .
                    . . . 3 3 3 3 4 4 4 4 4 4 . . .
                    . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                    . . 3 3 3 3 3 2 2 2 1 1 5 4 . .
                    . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 .
                    . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 .
                    . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                    . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                    . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                    . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                    . . . 4 2 2 2 2 2 2 2 2 4 . . .
                    . . . . 4 4 2 2 2 2 4 4 . . . .
                    . . . . . . 4 4 4 4 . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                SpriteKind.enemy)
            animation.run_image_animation(badsoul,
                [img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . 4 4 4 5 5 4 4 4 . . . .
                        . . . 3 3 3 3 4 4 4 4 4 4 . . .
                        . . 4 3 3 3 3 2 2 2 1 1 4 4 . .
                        . . 3 3 f f f 2 2 f f f 5 4 . .
                        . 4 3 3 f 2 f 2 2 f 2 f 5 4 4 .
                        . 4 3 3 f f f 2 4 f f f 5 4 4 .
                        . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 .
                        . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 .
                        . . 4 2 3 3 2 4 4 4 4 4 2 4 . .
                        . . 4 2 2 3 2 2 4 4 4 2 4 4 . .
                        . . . 4 2 2 2 2 2 2 2 2 4 . . .
                        . . . . 4 4 2 2 2 2 4 4 . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . . . . . . . . . . . . .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . 4 4 2 4 3 3 3 4 . . . .
                        . . . 4 2 2 3 3 3 3 3 3 3 . . .
                        . . 4 2 f f f 3 3 f f f 3 4 . .
                        . . 4 2 f 2 f 2 2 f 2 f 3 4 . .
                        . 4 2 2 f f f 2 2 f f f 3 4 4 .
                        . 4 2 2 2 4 4 4 2 2 2 2 4 5 4 .
                        . 4 2 2 4 4 4 4 4 2 2 2 4 5 4 .
                        . 4 2 2 4 4 4 4 4 2 2 2 4 4 4 .
                        . . 4 2 4 4 4 4 4 2 1 1 4 4 . .
                        . . 4 2 2 4 4 4 4 5 1 1 4 4 . .
                        . . . 4 4 2 4 4 5 5 5 4 4 . . .
                        . . . . 4 4 4 4 4 4 4 4 . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . . . . . . . . . . . . .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . 4 4 2 2 2 2 4 4 . . . .
                        . . . 4 2 2 2 2 2 2 2 2 4 . . .
                        . . 4 4 f f f 4 2 f f f 2 4 . .
                        . . 4 2 f 2 f 4 4 f 2 f 2 4 . .
                        . 4 4 4 f f f 4 4 f f f 3 2 4 .
                        . 4 4 4 4 4 4 4 4 2 2 3 3 4 4 .
                        . 4 4 5 4 4 4 4 2 2 2 3 3 3 4 .
                        . 4 4 5 5 2 2 2 2 2 3 3 3 3 4 .
                        . . 4 5 1 1 2 2 2 3 3 3 3 3 . .
                        . . 4 4 1 1 2 2 2 3 3 3 3 4 . .
                        . . . 4 4 4 4 4 4 3 3 3 3 . . .
                        . . . . 4 4 4 5 5 4 4 4 . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . . . . . . . . . . . . .
                        """),
                    img("""
                        . . . . . . . . . . . . . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . 4 4 4 4 4 4 4 4 . . . .
                        . . . 4 4 5 5 5 4 4 2 4 4 . . .
                        . . 4 4 f f f 4 4 f f f 2 4 . .
                        . . 4 4 f 2 f 4 4 f 2 f 2 4 . .
                        . 4 4 4 f f f 4 4 f f f 2 2 4 .
                        . 4 5 4 2 2 2 4 4 4 4 4 2 2 4 .
                        . 4 5 4 2 2 2 2 4 4 4 2 2 2 4 .
                        . 4 4 3 3 3 2 2 2 2 2 2 2 2 4 .
                        . . 4 3 3 3 3 2 2 2 3 3 2 4 . .
                        . . 4 3 3 3 3 3 3 3 3 2 2 4 . .
                        . . . 3 3 3 3 3 3 3 2 2 4 . . .
                        . . . . 4 3 3 3 4 2 4 4 . . . .
                        . . . . . . 4 4 4 4 . . . . . .
                        . . . . . . . . . . . . . . . .
                        """)],
                100,
                True)
            badsoul.set_position(randint(100, 200), randint(-100, 1))
            badsoul.follow(ghost, randint(0, 50))
game.on_update_interval(500, on_update_interval)

def on_update_interval2():
    global Boss, projectile3
    if info.score() == 10:
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222ff
            22fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222222222
            22222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222222
            222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222222
            2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222222
            2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222ffffffffffffffffffffffffffffffffffffffffffffffff222222222222222222222
            2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222fffffffffffffffffffffffffffffffffffffffffffffff2222222222222222222222
            2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffffff22222222222222222222222
            2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffffff22222222222222222222222
            2222222fffffffffffffffffffffffffffffffff222ffffffffffffffffffffffffffffffffffffffff222222222fffffffffffffffffffffffffffffffffffffffffffff22555555555555522222222
            2222222ffffffffffffffffffffffffffffff2222222fffffffffffffffffffffffffffffffffffffff2222222222ffffffffffffffffffffffffffffffffffffffff555555555555555555552222222
            2222222ffffffffffffffffffffffffffff222222222fffffffffffffffffffffffffffffffffffffff2222222222fffffffffffffffffffffffffffffffffffff555555555555555555555555222222
            2222222ffffffffffffffffffffffffff222222222222ffffffffffffffffffffffffffffffffffffff22222222222fffffffffffff55555555555555555555555555555555555555555555555222222
            2222222fffffffffffffffffffffffff2222222222222fffffffffffffffffffffffffffffffffffff222222222222f55555555555555555555555555555555555555555555555555555555555222222
            2222222ffffffffffffffffffffffff22222222222222ffffffffffffffffffffffffffffffffffff2222222222222f55555555555555555555555555555555555555555555555555555555555222222
            2222222fffffffffff5ffffffffffff22222222222222ffffffffffffffffffffffffffffffffffff2222222222222555555555555555555555555555555555555555555555555555555555555222222
            2222222fffff55555555fffffffffff22222222222222ffffffffffffffffffffffff22fffffffff22222222222222555555555555555555555555555555555555555555555555555555555555222222
            2222222ff55555555555fffffffffff222222222222222ffffffffffffffffffffff2222222ffff222222222222222555555555555555555555555555555555555555555555555555555555555222222
            22222225555555555555ffffffffff2222222222222222fffffffffffffffffffff2222222222ff222222222222222555555555555555555555555555555555555555555555555555555555555222222
            22222225555555555555ffffffffff2222222222222222fffffffffffffffffffff222222222222222222222222222555555555555555555555555555555555555555555555555555555555555222222
            222222255555555555555fffffffff2222222222222222fffffffffffffffffffff222222222222222222222222222555555555555555555555555555555555555555555555555555555555555222222
            222225555555555555555fffffffff2222222222222222ffffffffffffffffffff2222222222222222222222222225555555555555555555555555555555555555555555555555555555555555222222
            222255555555555555555ffffff2222222222222222222ffffffffffffffffffff2222222222222222222222222225555555555555555555555555555555555555555555555555555555555555222222
            2222555555555555555552222222222222222222222222ff222fffffffffffffff2222222222222222222222222225555555555555555555555555555555555555555555555555555555555555222222
            2225555555555555555552222222222222222222222222ff2222ffffffffffffff2222222222222222222222222225555555555555555555555555555555555555555555555555555555555555222222
            22255555555555555555522222222222222222222222222222222fffffffffffff2222222222222222222222222255555555555555555555555555555555555555555555555555555555555555522222
            225555555555555555555222222222222222222222222222222222ffffffffffff2222222222222222222222222255555555555555555555555555555555555555555555555555555555555555522222
            225555555555555555555222222222222222222222222222222222fffffffffff22222222222222222222222222255555555555555555555555555555555555555555555555555555555555555522222
            255555555555555555555222222222222222222222222222222222fffffffffff22222222222222222222222222555555555555555555555555555555555555555555555555555555555555555522222
            255555555555555555555222222222222222222222222222222222fffffffffff22222222222222222222222225555555555555555555555555555555555555555555555555555555555555555552222
            255555555555555555555222222222222555552222222222222222fffffffffff22222222222222222222222255555555555555555555555555555555555555555555555555555555555555555552222
            555555555555555555555522222222222555555522222222222222fffffffffff22222222222222222222222555555555555555555555555555555555555555555555555555555555555555555555555
            555555555555555555555522222222225555555522222222222222ffffffffff222222222222222255555555555555555555555555555555555555555555555555555555555555555555555555555555
            555555555555555555555552222222555555555552222222222222222222222f222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555222255555555555522222222222222222222222222222222222255555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555522222222222222222222222222222222222255555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555522222222222222222222222222222222222555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555522222222222222222222222222222222222555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555222222222222222222222222222222222555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555522222222222222222222222222222555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555222222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555552222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555222222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555522222222222222222222225555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555522222222222222222255555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555222222555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
            """))
    elif info.score() == 40:
        tiles.set_tilemap(tilemap("""
            level1
            """))
    elif info.score() == 150:
        Boss = sprites.create(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            SpriteKind.boss)
        Boss.set_position(150, 51)
        Boss.set_stay_in_screen(True)
        Boss.x += Math.constrain(0, 0, 112)
        animation.run_image_animation(sprites.create(img("""
                    ................................
                    ..........1...........1.........
                    .........111.........111........
                    .........111.........111........
                    .........111.........111........
                    .........111.........111........
                    ........11111111111111111.......
                    .......1111111111111111111......
                    ......111111111111111111111.....
                    .....11111111111111111111111....
                    ....1111122222111111222221111...
                    ....1111122522111111225221111...
                    ....1111122222111111222221111...
                    ....1111111111111111111111111...
                    ....1111111111111111111111111...
                    ....1111111111111111111111111...
                    ....1111111111111111111111111...
                    ....1111111111111111111111111...
                    ....1111111222222222111111111...
                    ....1111111222222222111111111...
                    ....1111111122212221111111111...
                    .....11111111211121111111111....
                    ......111111111111111111111.....
                    .......1111111111111111111......
                    ........1111111111111111........
                    .........11111111111111.........
                    ..........111111111111..........
                    ...........111111111............
                    ................................
                    ................................
                    ................................
                    ................................
                    """),
                SpriteKind.boss),
            [img("""
                    .......1................1.......
                    ......111..............111......
                    ......111..............111......
                    ......111..............111......
                    ......111..............111......
                    ......11111111111111111111......
                    .....1111111111111111111111.....
                    ....111111111111111111111111....
                    ...11111111111111111111111111...
                    ..1111112222111111112222111111..
                    ..1111112252111111112252111111..
                    ..1111112222111111112222111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111111111111111111111111..
                    ..1111111122222222222111111111..
                    ..1111111222222222222211111111..
                    ...11111255555555555552111111...
                    ....111112222222222222111111....
                    .....1111111111111111111111.....
                    ......11111111111111111111......
                    .......111111111111111111.......
                    ........1111111111111111........
                    .........11111111111111.........
                    ................................
                    ................................
                    ................................
                    ................................
                    """),
                img("""
                    ................................
                    ................................
                    .....11111......................
                    .....111111..............11111..
                    .....11111...............111111.
                    .....1111111111111111111111111..
                    ....1111111111111111111111......
                    ...111111111111111111111111.....
                    ..11111111111111111111111111....
                    .1111112222111111112222111111...
                    .1111112522111111112522111111...
                    .1111112222111111112222111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111111111111111111111111...
                    .1111111155555555555111111111...
                    .1111111555555555555511111111...
                    ..11111555555555555555111111....
                    ...111115555555555555111111.....
                    ....1111111111111111111111......
                    .....11111111111111111111.......
                    ......111111111111111111........
                    .......1111111111111111.........
                    ........11111111111111..........
                    ................................
                    ................................
                    ................................
                    ................................
                    """)],
            500,
            True)
        projectile3 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            Boss,
            100,
            0)
        projectile3.set_kind(SpriteKind.bossfire)
        Boss.set_kind(SpriteKind.player)
        info.player2.set_life(15)
game.on_update_interval(500, on_update_interval2)

def on_update_interval3():
    if info.score() == 50 and info.life() == 50:
        game.splash("would you like to give up? you're not even halfway there")
        if controller.A.is_pressed() == True:
            game.over(True, effects.hearts)
        elif controller.B.is_pressed() == True:
            info.set_score(info.life() + info.score())
game.on_update_interval(500, on_update_interval3)
