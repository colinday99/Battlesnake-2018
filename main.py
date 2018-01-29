import bottle
import os
import random

### Do not edit method headers

#This is the data that will be provided by the game on each turn

# DATA OBJECT
# {
#     "game": "hairy-cheese",
#     "mode": "advanced",
#     "turn": 4,
#     "height": 20,
#     "width": 30,
#     "snakes": [
#         <Snake Object>, <Snake Object>, ...
#     ],
#     "food": [
#         [1, 2], [9, 3], ...
#     ],
# }

#SNAKE OBJECT
# {
#     "id": "1234-567890-123456-7890",
#     "name": "Well Documented Snake",
#     "status": "alive",
#     "message": "Moved north",
#     "taunt": "Let's rock!",
#     "age": 56,
#     "health": 83,
#     "coords": [ [1, 1], [1, 2], [2, 2] ],
#     "kills": 4,
#     "food": 12,
#     "gold": 2
# }

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

# Called at the start of a game
@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Claire'
    }

#Called before each move
@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    
    ## Code to check the direction our snake is moving, can be replicated into a 
    ## method/def to see what direction every snake on the board is moving in.
    ## Essentially narrows down the potential directions so the snake will never run into itself.
    ## Currently working on checking if walls or food are immediately next to the head, to further 
    ## narrow down actions.
    
    # Checks if the coordinates are on the same row
    #if self_coords[0][0] == self_coords[1][0]:
    #    if self_coords[0][1] < self_coords[1][1]: #checks if it's to the right
    #        directions = ['up', 'down', 'left']
    #    elif self_coords[0][1] > self_coords[1][1]: #checks if it's to the left
    #        directions = ['up', 'down', 'right']
        
    # Checks if the coordinates are on the same column
    #elif self_coords[0][1] == self_coords[1][1]:
    #    if self_coords[0][0] < self_coords[1][0]:
    #        directions = ['down', 'left', 'right']
    #    elif self_coords[0][0] > self_coords[1][0]:
    #        directions = ['up', 'left', 'right']
    
    return {
        'move': random.choice(directions),
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
