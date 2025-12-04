@namespace
class SpriteKind:
    rizz = SpriteKind.create()
    sigma = SpriteKind.create()
    Boss = SpriteKind.create()
    miniboss = SpriteKind.create()
    t2enemy = SpriteKind.create()
    t3enemy = SpriteKind.create()
    Finale_Ultima_Boss_Phase_1 = SpriteKind.create()
    Finale_Ultima_Boss_Phase_2 = SpriteKind.create()

def on_overlap_tile(sprite10, location7):
    tiles.set_current_tilemap(tilemap("""
        level6
        """))
    tiles.place_on_tile(obsidian, tiles.get_tile_location(1, 128))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile43
        """),
    on_overlap_tile)

def on_on_score():
    info.set_life(175)
info.on_score(600, on_on_score)

def on_on_overlap(sprite25, otherSprite):
    sprites.destroy(projectile)
    sprites.change_data_number_by(otherSprite, "HP", -13)
    if sprites.read_data_number(otherSprite, "HP") <= 0:
        sprites.destroy(otherSprite)
        info.change_score_by(15)
        info.change_life_by(3)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.t3enemy, on_on_overlap)

def on_up_pressed():
    animation.run_image_animation(obsidian,
        [img("""
                . . . . . f f c c f f . . . . .
                . . . . f b c b b c b f . . . .
                . . . f a a a a a a a a f . . .
                . . f b a a a a a a a a b f . .
                . . f a a a a a a a a a a f . .
                . f a a a a a a a a a a a a f .
                . f b a a a a a a a a a a b f .
                . f b b a a a a a a a a b b f .
                . f b b b b b b b b b b b b f .
                f a b b b b b b b b b b b b a f
                f a a b b b b b b b b b b a a f
                . f a a b b b b b b b b a a f .
                . . 1 1 a f f f f f f a 1 1 . .
                . . 1 f b f b f b f b b f 1 . .
                . . . f f b f b f b f f f . . .
                . . . . . f b f b f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . f f c c f f . . . . .
                . . . . f b c b b c b f . . . .
                . . . f a a a a a a a a f . . .
                . . f a a a a a a a a a b f . .
                . . f a a a a a a a a a a f . .
                . f b a a a a a a a a a a b f .
                . f b b a a a a a a a a b b f .
                . f b b b b b b b b b b b b f .
                f b b b b b b b b b b b b b f .
                f a a b b b b b b b b b a a f .
                f f a a b b b b b b a a a f . .
                . f a a a f f f f f f f f b . .
                . f a f a f b f b f f 1 1 f . .
                . f a f f b f b f b f f f . . .
                . . f . . f b f b f f . . . . .
                """),
            img("""
                . . . . . f f c c f f . . . . .
                . . . . f b c b b c b f . . . .
                . . . f a a a a a a a a f . . .
                . . f b a a a a a a a a b f . .
                . . f a a a a a a a a a a f . .
                . f a a a a a a a a a a a a f .
                . f b a a a a a a a a a a b f .
                . f b b a a a a a a a a b b f .
                . f b b b b b b b b b b b b f .
                f a b b b b b b b b b b b b a f
                f a a b b b b b b b b b b a a f
                . f a a b b b b b b b b a a f .
                . . 1 1 a f f f f f f a 1 1 . .
                . . 1 f b f b f b f b b f 1 . .
                . . . f f b f b f b f f f . . .
                . . . . . f b f b f f . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . f f c c f f . . . . .
                . . . . f b c b b c b f . . . .
                . . . f a a a a a a a a f . . .
                . . f b a a a a a a a a a f . .
                . . f a a a a a a a a a a f . .
                . f b a a a a a a a a a a b f .
                . f b b a a a a a a a a b b f .
                . f b b b b b b b b b b b b f .
                . f b b b b b b b b b b b b b f
                . f a a b b b b b b b b b a a f
                . . f a a a b b b b b b a a f f
                . . b f f f f f f f f a a a f .
                . . f 1 1 f f b f b f a f a f .
                . . . f f f b f b f b f f a f .
                . . . . . f f b f b f . . f . .
                """),
            img("""
                . . . . . f f c c f f . . . . .
                . . . . f b c b b c b f . . . .
                . . . f a a a a a a a a f . . .
                . . f b a a a a a a a a b f . .
                . . f a a a a a a a a a a f . .
                . f a a a a a a a a a a a a f .
                . f b a a a a a a a a a a b f .
                . f b b a a a a a a a a b b f .
                . f b b b b b b b b b b b b f .
                f a b b b b b b b b b b b b a f
                f a a b b b b b b b b b b a a f
                . f a a b b b b b b b b a a f .
                . . 1 1 a f f f f f f a 1 1 . .
                . . 1 f b f b f b f b b f 1 . .
                . . . f f b f b f b f f f . . .
                . . . . . f b f b f f . . . . .
                """)],
        600,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile2(sprite, location):
    sprites.destroy(sprite)
scene.on_overlap_tile(SpriteKind.t2enemy,
    assets.tile("""
        myTile22
        """),
    on_overlap_tile2)

def on_on_score2():
    info.set_life(275)
    controller.move_sprite(obsidian, 100, 100)
info.on_score(1300, on_on_score2)

def on_on_created(sprite5):
    sprites.set_data_number(sprite5, "HP", 1000)
sprites.on_created(SpriteKind.Boss, on_on_created)

def on_overlap_tile3(sprite9, location6):
    sprites.destroy(sprite9)
scene.on_overlap_tile(SpriteKind.t2enemy,
    sprites.swamp.swamp_tile16,
    on_overlap_tile3)

def on_on_overlap2(sprite255, otherSprite6):
    sprites.destroy(projectile)
    sprites.change_data_number_by(otherSprite6, "HP", -15)
    if sprites.read_data_number(otherSprite6, "HP") <= 0:
        sprites.destroy(otherSprite6)
        info.change_score_by(5)
        info.change_life_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_b_pressed():
    global LostSoul
    if LostSoul == True:
        
        def on_after():
            global chargeblast
            chargeblast = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . f f . . . . . f f f . . . . .
                    f f f . f f f f f f f f f a a .
                    f f f f f f f f f f f f f f a a
                    a f f f f f f f f a f f f f f a
                    a a a a a a a a a a a a a a a a
                    a a a a a a a a a a a a a a a a
                    a f f f f f f f f a f f f f f a
                    f f f f f f f f f f f f f f a a
                    f f f . f f f f f f f f f a a .
                    . f f . . . . . f f f . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                80,
                0)
        timer.after(500, on_after)
        
        pause(100)
        if info.score() >= 1500:
            if LostSoul == True:
                
                def on_after2():
                    global chargeblast
                    chargeblast = sprites.create_projectile_from_sprite(img("""
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . f f . . . . . f f f . . . . .
                            f f f . f f f f f f f f f a a .
                            f f f f f f f f f f f f f f a a
                            a f f f f f f f f a f f f f f a
                            a a a a a a a a a a a a a a a a
                            a a a a a a a a a a a a a a a a
                            a f f f f f f f f a f f f f f a
                            f f f f f f f f f f f f f f a a
                            f f f . f f f f f f f f f a a .
                            . f f . . . . . f f f . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            """),
                        obsidian,
                        80,
                        0)
                timer.after(500, on_after2)
                
                pause(100)
        LostSoul = False
        
        def on_after3():
            global LostSoul
            LostSoul = True
        timer.after(10000, on_after3)
        
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap3(sprite27, otherSprite2):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-50)
        
        def on_after4():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after4)
        
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Finale_Ultima_Boss_Phase_2,
    on_on_overlap3)

def on_on_overlap4(sprite254, otherSprite5):
    sprites.destroy(sprite254)
    sprites.change_data_number_by(otherSprite5, "HP", -10)
    if sprites.read_data_number(otherSprite5, "HP") <= 0:
        sprites.destroy(otherSprite5)
        info.change_score_by(1000)
        if info.life() < 50:
            info.change_life_by(25)
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.Finale_Ultima_Boss_Phase_2,
    on_on_overlap4)

def on_on_score3():
    info.set_life(225)
    controller.move_sprite(obsidian, 95, 95)
info.on_score(1000, on_on_score3)

def on_overlap_tile4(sprite15, location10):
    tiles.set_current_tilemap(tilemap("""
        level6
        """))
    tiles.place_on_tile(obsidian, tiles.get_tile_location(123, 253))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile11
        """),
    on_overlap_tile4)

def on_a_pressed():
    global projectile, shards
    if shards == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            110,
            0)
        shards = False
        
        def on_after5():
            global shards
            shards = True
        timer.after(250, on_after5)
        
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap5(sprite256, otherSprite7):
    sprites.destroy(sprite256)
    sprites.change_data_number_by(otherSprite7, "HP", -10)
    if sprites.read_data_number(otherSprite7, "HP") <= 0:
        sprites.destroy(otherSprite7)
        info.change_score_by(1000)
        if info.life() < 50:
            info.change_life_by(25)
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.Finale_Ultima_Boss_Phase_1,
    on_on_overlap5)

def on_overlap_tile5(sprite3, location2):
    sprites.destroy(sprite3)
scene.on_overlap_tile(SpriteKind.enemy,
    assets.tile("""
        myTile22
        """),
    on_overlap_tile5)

def on_on_score4():
    info.set_life(325)
    controller.move_sprite(obsidian, 110, 110)
info.on_score(1700, on_on_score4)

def on_left_pressed():
    animation.run_image_animation(obsidian,
        [img("""
                . . . f b c f f f f . . . . . .
                . . f c a b c b f b f f . . . .
                . . f a b a b c a a b b f . . .
                . . f b c b c a a a a a b f . .
                . . f a a a a a a a a a b f . .
                . f a a f f b b b b a a b f . .
                . f a a f f f f f b a a b f . .
                . f a f f f a f f b a a b f . .
                . . f f 1 1 a f f b a a b f . .
                . . . f 1 1 1 1 f b a a b f f .
                . . . f f f f f f f b a a b f .
                . . . f c c c f 1 1 f b b f . .
                . . . f c c c f 1 1 f f f . . .
                . . f f b f b f b f f f . . . .
                . . f f f b f b f b f f . . . .
                . . . . f f b f b f . . . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . f b c f f f f . . . . . .
                . . f c c b c b f b f f . . . .
                . . f c b c b c b a b b f . . .
                . . f b c b c a a a a a b f . .
                . f a a a a a a a a a a b f . .
                . f a a f f b b b b a a b f . .
                . f a a f f f f f b a a b f . .
                . . f f f f a f f b a a b f f .
                . . . f 1 1 a f f b a a a b f .
                . . . f 1 1 1 1 f b a a a b f .
                . . . f f f f f 1 1 b b b f . .
                . . . f c c c f 1 1 f f f . . .
                . . f c c c c c f f c c f . . .
                . . f b f b f b f b f f . . . .
                . . . f b f b f b f f . . . . .
                """),
            img("""
                . . . f b c f f f f . . . . . .
                . . f c a b c b f b f f . . . .
                . . f a b a b c a a b b f . . .
                . . f b c b c a a a a a b f . .
                . . f a a a a a a a a a b f . .
                . f a a f f b b b b a a b f . .
                . f a a f f f f f b a a b f . .
                . f a f f f a f f b a a b f . .
                . . f f 1 1 a f f b a a b f . .
                . . . f 1 1 1 1 f b a a b f f .
                . . . f f f f f f f b a a b f .
                . . . f c c c f 1 1 f b b f . .
                . . . f c c c f 1 1 f f f . . .
                . . f f b f b f b f f f . . . .
                . . f f f b f b f b f f . . . .
                . . . . f f b f b f . . . . . .
                """)],
        600,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_combos_attach_combo():
    if bleh == False:
        animation.run_image_animation(obsidian,
            [img("""
                    . . . . . f f c c f f . . . . .
                    . . . . f a c b b c a f . . . .
                    . . . f a b b a a b b a f . . .
                    . . f c b d c b b c d b c f . .
                    . . f b d b b c c b b d b f . .
                    . f a a f b c f f c b f a a f .
                    . a 1 1 a f a f f f a f 1 1 a .
                    . f a a f f f a f a f f a a f .
                    . f a a f f a f f f a f a a f .
                    . a c c a 1 1 1 1 1 1 a c c a .
                    . c c c f 1 1 f f 1 1 f c c c .
                    . f c c f c b b b b c f c c f .
                    . . f a c b b b b b b c a f . .
                    . . f f c c c a a c c c f f . .
                    . . . f f b f b f b f f f . . .
                    . . . . f f b f b f b f f . . .
                    """),
                img("""
                    . . . . . f f c c f f . . . . .
                    . . . . f a c b b c a f . . . .
                    . . . f a b b a a b b a f . . .
                    . . f c b d c b b c d b c f . .
                    . . f b d b b c c b b d b f . .
                    . f a a f b c f f c b f a a f .
                    . f a a f f f f f f f f a a f .
                    . f c c f f a f f a f f c c f .
                    . f c c f f a f f a f f c c f .
                    f f c c f 1 1 1 1 1 1 f c c f f
                    f c 1 1 f 1 1 f f 1 1 f 1 1 c f
                    . f 1 1 f c b b b b c f 1 1 f .
                    . . f a c b b b b b b c a f . .
                    . . f f c c c a a c c c f f . .
                    . . . f f b f b f b f f f . . .
                    . . . . f f b f b f b f . . . .
                    """)],
            1000,
            False)
        
        def on_after6():
            global projectile, bleh
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                110,
                0)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                -110,
                0)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                110,
                -110)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                110,
                110)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                -110,
                110)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                -110,
                -110)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                0,
                110)
            projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    f b b a b a b f . . . . . . . .
                    a a a b a a a a f . . . . . . .
                    f b b a b a b f . . . . . . . .
                    . f b a a b f . . . . . . . . .
                    . . f f f f . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    """),
                obsidian,
                0,
                -110)
            bleh = True
            info.start_countdown(60)
        timer.after(1, on_after6)
        
controller.combos.attach_combo("a+b", on_combos_attach_combo)

def on_overlap_tile6(sprite6, location4):
    tiles.set_current_tilemap(tilemap("""
        level9
        """))
    tiles.place_on_tile(obsidian, tiles.get_tile_location(81, 97))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
        """),
    on_overlap_tile6)

def on_on_overlap6(sprite272, otherSprite22):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-5)
        
        def on_after7():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after7)
        
sprites.on_overlap(SpriteKind.player, SpriteKind.t2enemy, on_on_overlap6)

def on_on_overlap7(sprite274, otherSprite24):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-25)
        
        def on_after8():
            global isInvincible
            isInvincible = False
        timer.after(1250, on_after8)
        
sprites.on_overlap(SpriteKind.player, SpriteKind.Boss, on_on_overlap7)

def on_on_overlap8(sprite276, otherSprite26):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-10)
        
        def on_after9():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after9)
        
sprites.on_overlap(SpriteKind.player, SpriteKind.miniboss, on_on_overlap8)

def on_overlap_tile7(sprite4, location3):
    sprites.destroy(sprite4)
scene.on_overlap_tile(SpriteKind.t3enemy,
    sprites.swamp.swamp_tile16,
    on_overlap_tile7)

def on_countdown_end():
    global bleh
    bleh = False
info.on_countdown_end(on_countdown_end)

def on_on_created2(sprite11):
    sprites.set_data_number(sprite11, "HP", 1000)
sprites.on_created(SpriteKind.Finale_Ultima_Boss_Phase_1, on_on_created2)

def on_right_pressed():
    animation.run_image_animation(obsidian,
        [img("""
                . . . . . . f f f f c b f . . .
                . . . . f f b f b c b a c f . .
                . . . f b b a a c b a b a f . .
                . . f b a a a a a c b c b f . .
                . . f b a a a a a a a a a f . .
                . . f b a a b b b b f f a a f .
                . . f b a a b f f f f f a a f .
                . . f b a a b f f a f f f a f .
                . . f b a a b f f a 1 1 f f . .
                . f f b a a b f 1 1 1 1 f . . .
                . f b a a b f f f f f f f . . .
                . . f b b f 1 1 f c c c f . . .
                . . . f f f 1 1 f c c c f . . .
                . . . . f f f b f b f b f f . .
                . . . . f f b f b f b f f f . .
                . . . . . . f b f b f f . . . .
                """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f c b f . . .
                . . . . f f b f b c b c c f . .
                . . . f b b a b c b c b c f . .
                . . f b a a a a a c b c b f . .
                . . f b a a a a a a a a a a f .
                . . f b a a b b b b f f a a f .
                . . f b a a b f f f f f a a f .
                . f f b a a b f f a f f f f . .
                . f b a a a b f f a 1 1 f . . .
                . f b a a a b f 1 1 1 1 f . . .
                . . f b b b 1 1 f f f f f . . .
                . . . f f f 1 1 f c c c f . . .
                . . . f c c f f c c c c c f . .
                . . . . f f b f b f b f b f . .
                . . . . . f f b f b f b f . . .
                """),
            img("""
                . . . . . . f f f f c b f . . .
                . . . . f f b f b c b a c f . .
                . . . f b b a a c b a b a f . .
                . . f b a a a a a c b c b f . .
                . . f b a a a a a a a a a f . .
                . . f b a a b b b b f f a a f .
                . . f b a a b f f f f f a a f .
                . . f b a a b f f a f f f a f .
                . . f b a a b f f a 1 1 f f . .
                . f f b a a b f 1 1 1 1 f . . .
                . f b a a b f f f f f f f . . .
                . . f b b f 1 1 f c c c f . . .
                . . . f f f 1 1 f c c c f . . .
                . . . . f f f b f b f b f f . .
                . . . . f f b f b f b f f f . .
                . . . . . . f b f b f f . . . .
                """)],
        600,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_destroyed(sprite12):
    global you, projectile
    animation.run_movement_animation(you,
        animation.animation_presets(animation.fly_to_center),
        2000,
        False)
    you = sprites.create(img("""
            ................
            ......2..2......
            ....222..2222...
            ...2222...222...
            ...2.2.....22...
            ...2........2...
            ...2fffaafff2...
            ...2ffaffaff2...
            ....fa2222af....
            ....af2ff2fa....
            ....fa2222af....
            ...fffaffafff...
            ...ffffaaffff...
            ...f11111111f...
            ...f11111111f...
            ...ff111111ff...
            .aaff111111ffaaa
            aa.ff111111ff..a
            a.22f111111f22.a
            a.2.f111111f.2.a
            a.2.f111111f.2.a
            a.2..211112f2.aa
            aa.2.221122ffff.
            .aaff222222fffff
            ..ff..2222ffffff
            ..ff..2222111.ff
            ..ff..f22f11f..f
            ..ff..f1f11ff..f
            ..ff..fffffff..f
            ..ff..ffffff...f
            ..ff..f1f1ff...f
            .fff.f11f1ff..ff
            .ff..f1ff1ff..ff
            .ff..11ff111..ff
            .ff..fffffff..ff
            .ff..ffff1ff..ff
            .ff..ff1f1ff..ff
            .22..f11f11f..22
            .2..f11fff1f..22
            .2..f1ffff11...2
            ..2.ffffffff...2
            ....ff....ff....
            ....ff....ff....
            ....f......ff...
            ...22......ff...
            ...2.......ff...
            ...2........22..
            ...2........22..
            """),
        SpriteKind.Finale_Ultima_Boss_Phase_2)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            2 f f f . . . . . . . 2 . . . .
            2 2 f f f . . . . . 2 . 2 . . .
            f 2 2 2 f f f f f 2 . . . 2 . .
            f f f 2 2 f f f f f f . . . 2 .
            f f f f f 2 2 f f f f f f f f 2
            f f f f f 2 2 f f f f f f f f 2
            f f f 2 2 f f f f f f . . . 2 .
            f 2 2 2 f f f f f 2 . . . 2 . .
            2 2 f f f . . . . . 2 . 2 . . .
            2 f f f . . . . . . . 2 . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        you,
        110,
        0)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . 2 . . . . . . . f f f 2
            . . . 2 . 2 . . . . . f f f 2 2
            . . 2 . . . 2 f f f f f 2 2 2 f
            . 2 . . . f f f f f f 2 2 f f f
            2 f f f f f f f f 2 2 f f f f f
            2 f f f f f f f f 2 2 f f f f f
            . 2 . . . f f f f f f 2 2 f f f
            . . 2 . . . 2 f f f f f 2 2 2 f
            . . . 2 . 2 . . . . . f f f 2 2
            . . . . 2 . . . . . . . f f f 2
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        you,
        -110,
        0)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . 2 2 . . . . . . .
            . . . . . . 2 f f 2 . . . . . .
            . . . . . 2 . f f . 2 . . . . .
            . . . . 2 . . f f . . 2 . . . .
            . . . 2 . . . f f . . . 2 . . .
            . . . . 2 . f f f f . 2 . . . .
            . . . . . 2 f f f f 2 . . . . .
            . . . . . f f f f f f . . . . .
            . . . . . f f f f f f . . . . .
            . . . . . f f 2 2 f f . . . . .
            . . . . . f f 2 2 f f . . . . .
            . . . . f f 2 f f 2 f f . . . .
            . . . f f 2 2 f f 2 2 f f . . .
            . . . f f 2 f f f f 2 f f . . .
            . . . f 2 2 f f f f 2 2 f . . .
            . . . 2 2 f f f f f f 2 2 . . .
            """),
        you,
        0,
        110)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . 2 2 f f f f f f 2 2 . . .
            . . . f 2 2 f f f f 2 2 f . . .
            . . . f f 2 f f f f 2 f f . . .
            . . . f f 2 2 f f 2 2 f f . . .
            . . . . f f 2 f f 2 f f . . . .
            . . . . . f f 2 2 f f . . . . .
            . . . . . f f 2 2 f f . . . . .
            . . . . . f f f f f f . . . . .
            . . . . . f f f f f f . . . . .
            . . . . . 2 f f f f 2 . . . . .
            . . . . 2 . f f f f . 2 . . . .
            . . . 2 . . . f f . . . 2 . . .
            . . . . 2 . . f f . . 2 . . . .
            . . . . . 2 . f f . 2 . . . . .
            . . . . . . 2 f f 2 . . . . . .
            . . . . . . . 2 2 . . . . . . .
            """),
        you,
        0,
        -110)
sprites.on_destroyed(SpriteKind.Finale_Ultima_Boss_Phase_1, on_on_destroyed)

def on_on_overlap9(sprite275, otherSprite25):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-5)
        
        def on_after10():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after10)
        
sprites.on_overlap(SpriteKind.player, SpriteKind.t3enemy, on_on_overlap9)

def on_on_score5():
    info.set_life(400)
    controller.move_sprite(obsidian, 130, 130)
info.on_score(2500, on_on_score5)

def on_overlap_tile8(sprite14, location9):
    global you
    scene.set_background_image(img("""
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbffbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbffbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbffbbfbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbffbbffbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbffffbbbfbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbfbbbbfbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfffbbbffbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbfbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbfbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbffbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbbbbffbbbbbbbbbbbffbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbfbbbbbbbbbbfffbbbbbbbbbbbbbbbfffbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbfbbbbffffffbbbbbbbbbbbbbbbbbbbbfffbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbfffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbffffffbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        """))
    tiles.set_current_tilemap(tilemap("""
        level8
        """))
    you = sprites.create(img("""
            ................
            ................
            ................
            ................
            ................
            ................
            .....ffffff.....
            ....ffffffff....
            ....f1ff11ff....
            ....f1ff11ff....
            ....ffffffff....
            ...ffffffffff...
            ...ffffffffff...
            ...f11111111f...
            ...f11111111f...
            ...ff111111ff...
            ...ff111111ff...
            ...ff111111ff...
            ....f111111f....
            ....f111111f....
            ....f111111f....
            .....f1111ff....
            .....ff11ffffff.
            ...fffffffffffff
            ..ff..1fffffffff
            ..ff..11ff111.ff
            ..ff..f1ff11f..f
            ..ff..f1f11ff..f
            ..ff..fffffff..f
            ..ff..ffffff...f
            ..ff..f1f1ff...f
            .fff.f11f1ff..ff
            .ff..f1ff1ff..ff
            .ff..11ff111..ff
            .ff..fffffff..ff
            .ff..ffff1ff..ff
            .ff..ff1f1ff..ff
            .22..f11f11f..22
            .2..f11fff1f..22
            .2..f1ffff11...2
            ..2.ffffffff...2
            ....ff....ff....
            ....ff....ff....
            ....f......ff...
            ...22......ff...
            ...2.......ff...
            ...2........22..
            ...2........22..
            """),
        SpriteKind.Finale_Ultima_Boss_Phase_1)
    tiles.place_on_tile(you, tiles.get_tile_location(9, 3))
    tiles.place_on_tile(obsidian, tiles.get_tile_location(9, 3))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile23
        """),
    on_overlap_tile8)

def on_on_overlap10(sprite257, otherSprite8):
    sprites.destroy(projectile)
    sprites.change_data_number_by(otherSprite8, "HP", -14)
    if sprites.read_data_number(otherSprite8, "HP") <= 0:
        sprites.destroy(otherSprite8)
        info.change_life_by(2)
        info.change_score_by(10)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.t2enemy, on_on_overlap10)

def on_on_overlap11(sprite252, otherSprite3):
    sprites.change_data_number_by(otherSprite3, "HP", -10)
    sprites.destroy(projectile)
    if sprites.read_data_number(otherSprite3, "HP") <= 0:
        sprites.destroy(otherSprite3)
        info.change_score_by(500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss, on_on_overlap11)

def on_down_pressed():
    animation.run_image_animation(obsidian,
        [img("""
                . . . . . f f c c f f . . . . .
                . . . . f a c b b c a f . . . .
                . . . f a b b a a b b a f . . .
                . . f c b d c b b c d b c f . .
                . . f b d b b c c b b d b f . .
                . f a a f b c f f c b f a a f .
                . f a a f f f f f f f f a a f .
                . f c c f f a f f a f f c c f .
                . f c c f f a f f a f f c c f .
                f f c c f 1 1 1 1 1 1 f c c f f
                f c 1 1 f 1 1 f f 1 1 f 1 1 c f
                . f 1 1 f c b b b b c f 1 1 f .
                . . f a c b b b b b b c a f . .
                . . f f c c c a a c c c f f . .
                . . . f f b f b f b f f f . . .
                . . . . f f b f b f b f . . . .
                """),
            img("""
                . . . . . . . f f . . . . . . .
                . . . . . f f b b f f . . . . .
                . . . . f c b a a b c f . . . .
                . . . f c 1 c b b c 1 c f . . .
                . . f c 1 c b c c b c 1 c f . .
                . f a a f b c f f c b f a a f .
                . f a a f f f f f f f f a a f .
                . f b a f f f f f f f f a b f .
                f f b b f f a f f a f f b b f f
                f b b b f f a 1 1 a f f b b b f
                . f b b f 1 1 f f 1 1 f b b f .
                . . f 1 1 1 f b b b c f f f . .
                . . f f 1 1 f b b b b c 1 f . .
                . . . f f f b b c b c c f f . .
                . . . f f f b f b f b f f . . .
                . . . . f f f b f b f b f . . .
                """),
            img("""
                . . . . . f f c c f f . . . . .
                . . . . f a c b b c a f . . . .
                . . . f a b b a a b b a f . . .
                . . f c b d c b b c d b c f . .
                . . f b d b b c c b b d b f . .
                . f a a f b c f f c b f a a f .
                . f a a f f f f f f f f a a f .
                . f c c f f a f f a f f c c f .
                . f c c f f a f f a f f c c f .
                f f c c f 1 1 1 1 1 1 f c c f f
                f c 1 1 f 1 1 f f 1 1 f 1 1 c f
                . f 1 1 f c b b b b c f 1 1 f .
                . . f a c b b b b b b c a f . .
                . . f f c c c a a c c c f f . .
                . . . f f b f b f b f f f . . .
                . . . . f f b f b f b f . . . .
                """),
            img("""
                . . . . . . . f f . . . . . . .
                . . . . . f f b b f f . . . . .
                . . . . f c b a a b c f . . . .
                . . . f c 1 c b b c 1 c f . . .
                . . f c 1 c b c c b c 1 c f . .
                . f a a f b c f f c b f a a f .
                . f a a f f f f f f f f a a f .
                . f b a f f f f f f f f a b f .
                f f b b f f a f f a f f b b f f
                f b b b f f a 1 1 a f f b b b f
                . f b b f 1 1 f f 1 1 f b b f .
                . . f f f c b b b f 1 1 1 f . .
                . . f 1 c b b b b f 1 1 f f . .
                . . f f c c b c b b f f f . . .
                . . . f f b f b f b f f f . . .
                . . . f b f b f b f f f . . . .
                """),
            img("""
                . . . . . f f c c f f . . . . .
                . . . . f a c b b c a f . . . .
                . . . f a b b a a b b a f . . .
                . . f c b d c b b c d b c f . .
                . . f b d b b c c b b d b f . .
                . f a a f b c f f c b f a a f .
                . f a a f f f f f f f f a a f .
                . f c c f f a f f a f f c c f .
                . f c c f f a f f a f f c c f .
                f f c c f 1 1 1 1 1 1 f c c f f
                f c 1 1 f 1 1 f f 1 1 f 1 1 c f
                . f 1 1 f c b b b b c f 1 1 f .
                . . f a c b b b b b b c a f . .
                . . f f c c c a a c c c f f . .
                . . . f f b f b f b f f f . . .
                . . . . f f b f b f b f . . . .
                """)],
        600,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile9(sprite8, location5):
    sprites.destroy(sprite8)
scene.on_overlap_tile(SpriteKind.enemy,
    sprites.swamp.swamp_tile16,
    on_overlap_tile9)

def on_on_overlap12(sprite277, otherSprite27):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-50)
        
        def on_after11():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after11)
        
sprites.on_overlap(SpriteKind.player,
    SpriteKind.Finale_Ultima_Boss_Phase_1,
    on_on_overlap12)

def on_on_score6():
    info.set_life(100)
    controller.move_sprite(obsidian, 90, 90)
info.on_score(200, on_on_score6)

def on_on_score7():
    info.set_life(375)
    controller.move_sprite(obsidian, 120, 120)
info.on_score(2100, on_on_score7)

def on_overlap_tile10(sprite13, location8):
    sprites.destroy(sprite13)
scene.on_overlap_tile(SpriteKind.t3enemy,
    assets.tile("""
        myTile22
        """),
    on_overlap_tile10)

def on_on_created3(sprite7):
    sprites.set_data_number(sprite7, "HP", 500)
sprites.on_created(SpriteKind.miniboss, on_on_created3)

def on_on_overlap13(sprite253, otherSprite4):
    sprites.change_data_number_by(otherSprite4, "HP", -12)
    sprites.destroy(projectile)
    if sprites.read_data_number(otherSprite4, "HP") <= 0:
        sprites.destroy(otherSprite4)
        info.change_score_by(200)
        if info.life() < 50:
            info.change_life_by(25)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.miniboss, on_on_overlap13)

def on_on_overlap14(sprite273, otherSprite23):
    global isInvincible
    if isInvincible == False:
        isInvincible = True
        info.change_life_by(-5)
        
        def on_after12():
            global isInvincible
            isInvincible = False
        timer.after(1000, on_after12)
        
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap14)

def on_on_score8():
    info.set_life(500)
    controller.move_sprite(obsidian, 150, 150)
info.on_score(3100, on_on_score8)

def on_on_created4(sprite2):
    sprites.set_data_number(sprite2, "HP", 2000)
sprites.on_created(SpriteKind.Finale_Ultima_Boss_Phase_2, on_on_created4)

def on_overlap_tile11(sprite16, location11):
    tiles.set_current_tilemap(tilemap("""
        level7
        """))
    tiles.place_on_tile(obsidian, tiles.get_tile_location(1, 40))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile30
        """),
    on_overlap_tile11)

helioite: Sprite = None
ruby: Sprite = None
opal: Sprite = None
you: Sprite = None
chargeblast: Sprite = None
projectile: Sprite = None
LostSoul = False
shards = False
isInvincible = False
bleh = False
obsidian: Sprite = None
scene.camera_follow_sprite(obsidian)
tiles.set_current_tilemap(tilemap("""
    level6
    """))
scene.set_background_image(img("""
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    """))
obsidian = sprites.create(img("""
        . . . . . f f c c f f . . . . .
        . . . . f a c b b c a f . . . .
        . . . f a b b a a b b a f . . .
        . . f c b d c b b c d b c f . .
        . . f b d b b c c b b d b f . .
        . f a a f b c f f c b f a a f .
        . f a a f f f f f f f f a a f .
        . f c c f f a f f a f f c c f .
        . f c c f f a f f a f f c c f .
        f f c c f 1 1 1 1 1 1 f c c f f
        f c 1 1 f 1 1 f f 1 1 f 1 1 c f
        . f 1 1 f c b b b b c f 1 1 f .
        . . f a c b b b b b b c a f . .
        . . f f c c c a a c c c f f . .
        . . . f f b f b f b f f f . . .
        . . . . f f b f b f b f . . . .
        """),
    SpriteKind.player)
scene.camera_follow_sprite(obsidian)
mySprite = sprites.create(img("""
        . . . . . . e e e e . . . . . .
        . . . . e e e 4 4 e e f . . . .
        . . . f e 4 4 4 4 4 4 e f . . .
        . . f e 4 e e e e e e 4 e f . .
        . . f e e 5 4 4 4 4 5 e e f . .
        . . f e 4 e 5 e e 5 e 4 e f . .
        . . f f e f f 5 5 f f e f f . .
        . f f e f 4 4 f f 4 4 f e f f .
        . f e e f f 2 f f 2 f f e e f .
        . . f e e f f f f f f e e f . .
        . . . f e 4 f f f f 4 e f . . .
        e e e e 4 e 4 e e 4 e 4 e e e e
        e 2 4 2 f 4 e e e e 4 f 2 4 2 e
        e 2 4 f 4 f e e e e f 4 f 4 2 e
        2 2 2 . . 4 f e e f 4 . . 2 2 2
        . 2 . . . f f . . f f . . . 2 .
        """),
    SpriteKind.miniboss)
meh = sprites.create(img("""
        . . 2 . . . 5 5 5 5 . . . 2 . .
        . . 2 2 2 5 5 4 4 5 5 2 2 2 . .
        . . . 2 5 4 4 4 4 4 4 5 2 . . .
        . . f 5 4 5 5 5 5 5 5 4 5 f . .
        . . f 5 5 c 4 4 4 4 c 5 5 f . .
        . . f 5 4 5 c 5 5 c 5 4 5 f . .
        . . f f 5 f f c c f f e f f . .
        . f f 5 f 5 5 f f 5 5 f 5 f f .
        . f 5 5 f f c f f c f f 5 5 f .
        . . f 5 5 f f f f f f 5 5 f . .
        . . . f 5 4 1 f f 1 4 5 f . . .
        5 5 5 5 4 e 4 1 1 4 e 4 5 5 5 5
        5 1 4 1 f 4 5 5 5 5 4 f 1 4 1 5
        5 1 4 f 4 f 5 5 5 5 f 4 f 4 1 5
        1 1 1 . . 4 f 5 5 f 4 . . 1 1 1
        . 1 . . . f f . . f f . . . 1 .
        """),
    SpriteKind.miniboss)
myEnemy = sprites.create(img("""
        . . . . . . d d d d . . . . . .
        . . . . d d d b b d d f . . . .
        . . . f d b b b b b b d f . . .
        . . f d b d d d d d d b d f . .
        . . f d d f b b b b f d d f . .
        . . f d b d f d d f d b d f . .
        . . f f d 1 1 f f 1 1 d f f . .
        . f f d 1 6 6 1 1 6 6 1 d f f .
        . f d d 1 1 b 1 1 b 1 1 d d f .
        . . f d d 1 1 1 1 1 1 d d f . .
        . . . f d b 1 1 1 1 b d f . . .
        d d d d b d b d d b d b d d d d
        d 9 b 9 f b d d d d b f 9 b 9 d
        d 9 b f b f d d d d f b f b 9 d
        9 9 9 . . b f d d f b . . 9 9 9
        . 9 . . . f f . . f f . . . 9 .
        """),
    SpriteKind.miniboss)
erm = sprites.create(img("""
        . . . . . . 1 1 1 1 . . . . . .
        . . . . 1 1 1 6 6 1 1 9 . . . .
        . . . 9 1 6 6 6 6 6 6 1 9 . . .
        . . 9 1 6 1 1 1 1 1 1 6 1 9 . .
        . . 9 1 1 9 6 6 6 6 9 1 1 9 . .
        . . 9 1 6 1 9 1 1 9 1 6 1 9 . .
        . . 9 9 1 f f 9 9 f f 1 9 9 . .
        . 9 9 1 f 8 8 f f 8 8 f 1 9 9 .
        . 9 1 1 f f 1 f f 1 f f 1 1 9 .
        . . 9 1 1 f f f f f f 1 1 9 . .
        . . . 9 1 6 f 8 8 f 6 1 9 . . .
        1 1 1 1 6 1 6 1 1 6 1 6 1 1 1 1
        1 f 8 9 9 6 1 1 1 1 6 9 9 8 f 1
        1 f 8 9 6 9 1 1 1 1 9 6 9 8 f 1
        f f f . . 6 9 1 1 9 6 . . f f f
        . f . . . 9 9 . . 9 9 . . . f .
        """),
    SpriteKind.miniboss)
bleh = False
isInvincible = False
shards = True
tiles.place_on_tile(myEnemy, tiles.get_tile_location(1, 129))
tiles.place_on_tile(obsidian, tiles.get_tile_location(127, 127))
tiles.place_on_tile(mySprite, tiles.get_tile_location(127, 4))
tiles.place_on_tile(meh, tiles.get_tile_location(123, 253))
tiles.place_on_tile(erm, tiles.get_tile_location(253, 115))
controller.move_sprite(obsidian, 85, 85)
LostSoul = True
info.set_life(50)
info.change_score_by(3095)

def on_update_interval():
    global opal
    opal = sprites.create(img("""
            ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11133111f.......
            ......fd11333311df......
            ......fd11133111df......
            ......fdd311113ddf......
            ......fbdb3dd3bdbf......
            ......fcdc3113cdcf......
            .......fb311113bf.......
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
        SpriteKind.t2enemy)
    sprites.set_data_number(opal, "HP", 75)
    tiles.place_on_random_tile(opal, assets.tile("""
        myTile8
        """))
    
    def on_after13():
        sprites.destroy(opal)
    timer.after(20000, on_after13)
    
game.on_update_interval(15000, on_update_interval)

def on_forever():
    global projectile
    if info.score() >= 1000:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            110,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            0,
            110)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            -110,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            0,
            -110)
        pause(10000)
    if info.score() >= 500:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . f b a a b f . . . . . . . . .
                f b b a b a b f . . . . . . . .
                a a a b a a a a f . . . . . . .
                f b b a b a b f . . . . . . . .
                . f b a a b f . . . . . . . . .
                . . f f f f . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                """),
            obsidian,
            -110,
            0)
        pause(10000)
forever(on_forever)

def on_forever2():
    if not (spriteutils.is_destroyed(ruby)):
        if spriteutils.distance_between(obsidian, ruby) > 125:
            ruby.follow(None)
        else:
            ruby.follow(obsidian, 80)
forever(on_forever2)

def on_forever3():
    if not (spriteutils.is_destroyed(mySprite)):
        if spriteutils.distance_between(obsidian, mySprite) > 300:
            mySprite.follow(None)
        else:
            mySprite.follow(obsidian, 100)
    pause(100)
    if not (spriteutils.is_destroyed(mySprite)):
        if spriteutils.distance_between(obsidian, mySprite) > 300:
            mySprite.follow(None)
        else:
            mySprite.follow(obsidian, 90)
forever(on_forever3)

def on_forever4():
    if not (spriteutils.is_destroyed(opal)):
        if spriteutils.distance_between(obsidian, opal) > 125:
            opal.follow(None)
        else:
            opal.follow(obsidian, 80)
forever(on_forever4)

def on_forever5():
    if not (spriteutils.is_destroyed(myEnemy)):
        if spriteutils.distance_between(obsidian, myEnemy) > 300:
            myEnemy.follow(None)
        else:
            myEnemy.follow(obsidian, 100)
forever(on_forever5)

def on_forever6():
    if not (spriteutils.is_destroyed(erm)):
        if spriteutils.distance_between(obsidian, erm) > 125:
            erm.follow(None)
        else:
            erm.follow(obsidian, 100)
forever(on_forever6)

def on_forever7():
    if not (spriteutils.is_destroyed(meh)):
        if spriteutils.distance_between(obsidian, meh) > 300:
            meh.follow(None)
        else:
            meh.follow(obsidian, 95)
forever(on_forever7)

def on_forever8():
    if not (spriteutils.is_destroyed(helioite)):
        if spriteutils.distance_between(obsidian, helioite) > 125:
            helioite.follow(None)
        else:
            helioite.follow(obsidian, 80)
forever(on_forever8)

def on_update_interval2():
    global helioite
    helioite = sprites.create(img("""
            ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb151151bf.......
            .......f15155151f.......
            ......fd11555511df......
            ......fd15155151df......
            ......fddd5115dddf......
            ......fbdb5dd5bdbf......
            ......fcdc5115cdcf......
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
        SpriteKind.t3enemy)
    sprites.set_data_number(helioite, "HP", 100)
    tiles.place_on_random_tile(helioite, assets.tile("""
        myTile8
        """))
    
    def on_after14():
        sprites.destroy(helioite)
    timer.after(20000, on_after14)
    
game.on_update_interval(20000, on_update_interval2)

def on_update_interval3():
    global ruby
    ruby = sprites.create(img("""
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
        SpriteKind.enemy)
    sprites.set_data_number(ruby, "HP", 50)
    tiles.place_on_random_tile(ruby, assets.tile("""
        myTile8
        """))
    
    def on_after15():
        sprites.destroy(ruby)
    timer.after(20000, on_after15)
    
game.on_update_interval(10000, on_update_interval3)
