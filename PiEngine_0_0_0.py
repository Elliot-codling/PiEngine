#game engine
#GAME ENGINE CREATED BY ELLIOT CODLING


class player():
    def left(player_screenx, player_screenx_2, player_x, player_x_2, vel):
        #stop the players screen x coord if it gets too close to the left border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx > left_border:
            player_screenx -= vel
            player_screenx_2 -= vel
            player_x -= vel
            player_x_2 -= vel

        return player_screenx, player_x, player_screenx_2, player_x_2

    def right(player_screenx, player_screenx_2, player_x, player_x_2, vel):
        #stop the players screen x coord if it gets too close to the right border
        #return the values of the player's x coord and the players screen x coord 
        if player_screenx < right_border:
            player_screenx += vel
            player_screenx_2 += vel
            player_x += vel
            player_x_2 += vel

        return player_screenx, player_x, player_screenx_2, player_x_2

    def up(player_screeny, player_screeny_2, player_y, player_y_2, vel):
        #stop the player screen y coord if it gets too close to the top border
        #return the values of the players x coord and the players screen x coord
        if player_screeny > top_border:
            player_screeny -= vel
            player_screeny_2 -= vel
            player_y -= vel
            player_y_2 -= vel

        return player_screeny, player_y, player_screeny_2, player_y_2

    def down(player_screeny, player_screeny_2, player_y, player_y_2, vel):
        #stop the player screen y coord if it gets too close to the bottom border
        #return the values of the players x coord and the players screen x coord
        if player_screeny < bottom_border:
            player_screeny += vel
            player_screeny_2 += vel
            player_y += vel
            player_y_2 += vel

        return player_screeny, player_y, player_screeny_2, player_y_2

    #define the left border of the screen to stop moving
    def left_border(x):
        global left_border
        left_border = x

    #define the right border of the screen to stop moving
    def right_border(x):
        global right_border
        right_border = x

    #define the up border of the screen to stop moving
    def top_border(x):
        global top_border
        top_border = x

    #define the bottom border of the screen to stop moving
    def bottom_border(x):
        global bottom_border
        bottom_border = x

