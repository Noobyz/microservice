# Zach Orlosky
# Orloskyz@oregonstate.edu
# CS 361

from flask import Flask, request, jsonify

app = Flask(__name__)

plant_data = {
    'rose': {'other name': 'Rosaceae', 'type': 'perennial', 'sunlight': 'full'},
    'self-heal': {'other name': 'prunella vulgaris', 'type': 'perennial', 'sunlight': 'full'},
    'dandelion': {'other name': 'Taraxacum officinale', 'type': 'perennial', 'sunlight': 'full'},
    'endive': {'other name': 'Cichorium endivia', 'type': 'annual', 'sunlight': 'minimal'}
}

def get_plant_info(name):
    if name in plant_data:
        return plant_data[name]
    else:
        return "Invalid plant name, check spelling!\n"

def get_plant_list():
    return list(plant_data.keys())

@app.route('/api', methods=['POST'])
def handle_request():
    """
    Interpret info field, return JSON response
    """
    data = request.get_json()
    if not data or 'info' not in data:
        return jsonify("error, request not recognized!"), 400

    info = data['info']
    if info == 'get_plant_info':
        name = data.get('name')
        if not name:
            return jsonify("No plant name provided"), 400
        return jsonify(get_plant_info(name))

    elif info == 'get_plant_list':
        return jsonify(get_plant_list())

    elif info == 'exit':
        return jsonify("Good bye!")

    else:
        return jsonify("error, request not recognized!"), 400

if __name__ == '__main__':
    print("Server running, waiting for requests...")
    app.run(port=5555)
