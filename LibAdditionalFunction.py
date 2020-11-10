import json

def find_max_size(photo_size_list):
    photo_size_max = 0
    result_data = {}
    for photo in photo_size_list:
        pixel_count = photo['height'] * photo['width']
        if pixel_count > photo_size_max:
            photo_size_max = pixel_count
            result_data = photo
    return result_data


def get_input_data(filename):
    with open(filename) as f:
        result = json.load(f)
        if result['owner_id'][0] == '0':
            print('ВНИМАНИЕ! Во входных данных [owner_id] будет приведен к типу [int] для дальнейшей работы.')
            print('Содержащиеся в начале строки "0" будут удалены.')
        result['owner_id'] = int(result['owner_id'])

        if result['app_id'][0] == '0':
            print('ВНИМАНИЕ! Во входных данных [app_id] будет приведен к типу [int] для дальнейшей работы.')
            print('Содержащиеся в начале строки "0" будут удалены.')
        result['app_id'] = int(result['app_id'])

    return result