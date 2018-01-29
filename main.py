import bottle
import os
import random

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
#     "walls": [    // Advanced Only
#         [2, 2]
#     ],
#     "gold": [     // Advanced Only
#         [5, 5]
#     ]
# }

#SNAKE
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


@bottle.post('//start')
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
        'color': '#00FFFF',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Claire'
    }


@bottle.post('//move')
def move():
    data = bottle.request.json
    snek = data['snakes']
    
    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    
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
        'taunt': 'fuck this shit im out'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '134.87.144.119'), port=os.getenv('PORT', '4000'))