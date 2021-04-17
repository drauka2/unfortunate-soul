namespace SpriteKind {
    export const introguy = SpriteKind.create()
    export const boss = SpriteKind.create()
    export const bossfire = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.boss, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.player2.changeLifeBy(-1)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, ghost, -100, -100)
    sprites.createProjectileFromSprite(img`
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
        `, ghost, -100, -100).follow(badsoul, 100)
})
sprites.onOverlap(SpriteKind.bossfire, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.bossfire, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprite.startEffect(effects.disintegrate, 200)
    sprite.setPosition(76, 52)
    sprite.setKind(SpriteKind.Player)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, ghost, 100, 100)
    sprites.createProjectileFromSprite(img`
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
        `, ghost, 100, 100).follow(badsoul, 100)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    info.changeScoreBy(1)
    index += randint(0, 100)
    info.changeLifeBy(2)
    otherSprite.destroy()
})
sprites.onDestroyed(SpriteKind.introguy, function (sprite) {
    deathmachine.destroy()
    ghost = sprites.create(img`
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
        `, SpriteKind.Player)
    animation.runImageAnimation(
    ghost,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
    controller.moveSprite(ghost, 150, 150)
    scene.setBackgroundImage(img`
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
        `)
    game.showLongText("Oh, you died...that sucks. Wait, you shouldn't be here! Well I can't just let you go, that would be bad for business...I don't know, uh...collect like, i guess 500 souls, and you  can go back", DialogLayout.Center)
    ghost.setStayInScreen(true)
    info.setLife(10)
})
sprites.onCreated(SpriteKind.Player, function (sprite) {
    effects.clearParticles(sprite)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.introguy, function (sprite, otherSprite) {
    main.destroy(effects.spray, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    sprite.startEffect(effects.disintegrate, 200)
    sprite.setPosition(76, 52)
    sprite.setKind(SpriteKind.Player)
})
let projectile3: Sprite = null
let Boss: Sprite = null
let badsoul: Sprite = null
let ghost: Sprite = null
let projectile: Sprite = null
let main: Sprite = null
let deathmachine: Sprite = null
music.wawawawaa.play()
deathmachine = sprites.create(img`
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
    `, SpriteKind.Enemy)
main = sprites.create(img`
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
    `, SpriteKind.introguy)
deathmachine.setPosition(139, 57)
deathmachine.follow(main, 200)
controller.moveSprite(main)
let index = randint(0, 499)
forever(function () {
    if (index == 500) {
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.runImageAnimation(
        main,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
        pause(5000)
        game.over(true, effects.smiles)
    }
})
game.onUpdateInterval(500, function () {
    if (info.score() == 2000) {
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.runImageAnimation(
        main,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
        pause(5000)
        game.over(true, effects.smiles)
    }
    if (info.life() == 500) {
        game.splash("CONGRATS! you can now go back to your life...but your body is kinda squished...so...you're now a dog.")
        animation.runImageAnimation(
        main,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        500,
        true
        )
        pause(5000)
        game.over(true, effects.smiles)
    }
    badsoul = sprites.create(img`
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
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    badsoul,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    badsoul.follow(ghost, 50)
    badsoul.setPosition(182, randint(-100, 118))
    if (info.score() == 10) {
        badsoul = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        badsoul,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        badsoul.setPosition(randint(100, 200), randint(-100, 1))
        if (info.score() == 20) {
            badsoul = sprites.create(img`
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
                `, SpriteKind.Enemy)
            animation.runImageAnimation(
            badsoul,
            [img`
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
                `,img`
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
                `,img`
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
                `,img`
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
                `],
            100,
            true
            )
            badsoul.setPosition(randint(100, 200), randint(-100, 1))
            badsoul.follow(ghost, randint(0, 50))
        }
    }
})
game.onUpdateInterval(500, function () {
    if (info.score() == 10) {
        scene.setBackgroundImage(img`
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
            `)
    } else if (info.score() == 40) {
        tiles.setTilemap(tilemap`level1`)
    } else if (info.score() == 150) {
        Boss = sprites.create(img`
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
            `, SpriteKind.boss)
        Boss.setPosition(150, 51)
        Boss.setStayInScreen(true)
        Boss.x += Math.constrain(0, 0, 112)
        animation.runImageAnimation(
        sprites.create(img`
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
            `, SpriteKind.boss),
        [img`
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
            `,img`
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
            `],
        500,
        true
        )
        projectile3 = sprites.createProjectileFromSprite(img`
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
            `, Boss, 100, 0)
        projectile3.setKind(SpriteKind.bossfire)
        Boss.setKind(SpriteKind.Player)
        info.player2.setLife(15)
    }
})
game.onUpdateInterval(500, function () {
    if (info.score() == 50 && info.life() == 50) {
        game.splash("would you like to give up? you're not even halfway there")
        if (controller.A.isPressed() == true) {
            game.over(true, effects.hearts)
        } else if (controller.B.isPressed() == true) {
            info.setScore(info.life() + info.score())
        }
    }
})
