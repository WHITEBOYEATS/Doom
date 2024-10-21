from sprite_object import *


class UniqueSprite(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/unique_sprites/trash_can/0.png', pos=(3, 3), scale=0.6, shift=0.38, animation_time=180, health=5):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.animation_destruction = self.get_images(self.path + '/shot')
        self.animation_reaction = self.get_images(self.path + '/reaction')

        self.health = health
        self.original_health = self.health
        self.frame_counter = 0

        self.ray_cast_value = False       
        self.alive = True

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos
        if next_pos not in self.game.object_handler.npc_positions:
            self.x += 10

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()

    def check_sprite_hit(self):
        if self.ray_cast_value and self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.player.shot = False
                self.health -= 1
                # self.movement()


    
    def animate_reaction(self):
        # using brakets makes it start on that frame ie: if I put self.animation_reaction[1] it would go to the first frame in that animation
        self.image = self.animation_reaction[self.health]

            
    def animate_destrution(self):
        if self.game.global_trigger and self.frame_counter < len(self.animation_destruction) - 1:
            self.animation_destruction.rotate(-1)
            self.image = self.animation_destruction[0]
            self.frame_counter += 1
            self.alive = False

    def run_logic(self):
        if self.original_health == self.health:
            if self.health > 0:
                self.ray_cast_value = self.ray_cast_player_npc()
                self.check_sprite_hit()

            else:
                self.animate_destrution()
        else:
            if self.health > 0:
                self.animate_reaction()
                self.ray_cast_value = self.ray_cast_player_npc()
                self.check_sprite_hit()
            else:
                self.animate_destrution()



    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True
        
        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0
        
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth
        
        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
    
    
    
    