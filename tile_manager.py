from tile import Tile


class TileManager:

    def __init__(self):
        self.tiles = []
        self.actual_pos_y = 300
        self.actual_pos_x = -275
        self.end_pos_x = 275
        self.space_between = 4
        self.tile_width = 50
        self.tile_height = 20
        self.create_tile_board()

    def create_tile(self, position):
        tile = Tile()
        tile.setposition(position)
        tile.showturtle()
        self.tiles.append(tile)

    def create_tile_board(self):
        for pos_y in range(4):
            self.create_tile((self.actual_pos_x, self.actual_pos_y))
            for pos_x in range(10):
                # print(self.actual_pos_x, self.actual_pos_y)
                self.actual_pos_x += self.space_between + self.tile_width
                self.create_tile((self.actual_pos_x, self.actual_pos_y))
            self.actual_pos_y -= self.space_between + self.tile_height
            self.actual_pos_x = -275

    def remove_tile(self, tile):
        tile.hideturtle()
        tile.reset()
        self.tiles.remove(tile)
