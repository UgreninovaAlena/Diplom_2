# import json
# from pprint import pprint
# from urllib.parse import urlencode
# import requests
#
# from LibAdditionalFunction import find_max_size
# from ResultCreation import Result, catch_error
# from datetime import date
#
# def get_input_data(filename):
#     print('Пожалуйста, проверьте наличие необходимой информации для аутентификации в файле Data.txt')
#
#     with open(filename) as f:
#         result = json.load(f)
#         if result['owner_id'][0] == '0':
#             print('ВНИМАНИЕ! Во входных данных [owner_id] будет приведен к типу [int] для дальнейшей работы.')
#             print('Содержащиеся в начале строки "0" будут удалены.')
#         result['owner_id'] = int(result['owner_id'])
#
#     return result
# class Photo():
#     def __init__(self, id, owner_id, link_photo, likes):
#         self.id = id
#         self.owner_id = owner_id
#         self.link_photo = link_photo
#         self.likes = likes
#
#     def get_photo(self):
#         pass
#
#     def FOR_MY_print_elem(self):
#         print(f'[Photo]ID: {self.id}, OWNER ID {self.owner_id}  [{self.likes}] likes')
#         print(f'{self.link_photo}')
#         print('__________________________')
#
# class VKperson():
#     def __init__(self, VKperson_infolist):
#         self.id = VKperson_infolist['id']
#         self.first_name = VKperson_infolist['first_name']
#         self.last_name = VKperson_infolist['last_name']
#         if 'age' in VKperson_infolist.keys():
#             born_date = list(map(int, VKperson_infolist['bdate'].split('.')))
#             today = date.today()
#             self.age = today.year - born_date[2] - ((today.month, today.day) < (born_date[1], born_date[0]))
#         else:
#             self.age = None
#         self.interest = None
#
#         self.photos = []
#
#     def FOR_MY_print_elem(self):
#         print(f'[VKperson]ID: {self.id}')
#         print(f'{self.firs_name} {self.last_name}')
#         print(f'age: {self.age}, FLAG[{self.interest}]')
#         print('__________________________')
#
#
# class User():
#     def __init__(self, infolist, range_age):
#         self.id = infolist['id']
#         self.firs_name = infolist['first_name']
#         self.last_name = infolist['last_name']
#
#         self.sex = infolist['sex']
#         self.country_code = infolist['country']
#         self.city_code = infolist['city']
#         self.range_age = range_age
#
#         born_date = list(map(int, infolist['bdate'].split('.')))
#         today = date.today()
#         self.age = today.year - born_date[2] - ((today.month, today.day) < (born_date[1], born_date[0]))
#
#         self.VKperson_list = []
#
#     def FOR_MY_print_elem(self):
#         print(f'[User]ID: {self.id}')
#         print(f'{self.firs_name} {self.last_name}')
#         print(f' {self.country_code}, {self.city_code}')
#         print(f' sex: {self.sex}, age: {self.age}')
#         print(f'Range_age = {self.range_age}')
#         print('__________________________')
#
#     def add_VKperson(self, person):
#         self.VKperson_list.append(person)
#
#
# class SearchPeoples():
#     AOuthData = get_input_data("Data.txt")
#
#     def __init__(self):
#         print('Файл для чтения аутентификационных данных пользователя утановлен по умолчанию как Data.txt')
#         input('Пожалуйста, проверьте правильность его заполнения. Нажмите любую клавишу для продолжения.')
#         self.age_from = int(input('Ведите нижнюю границу возраста для поиска: '))
#         self.age_to = int(input('Ведите верхнюю границу возраста для поиска: '))
#
#     def init_user(self):
#         URL_to_get_userinfo = 'https://api.vk.com/method/users.get'
#         parameters_to_get_userinfo = {'fields': 'first_name, last_name, bdate, country, city, sex',
#                                       'user_ids': self.AOuthData['owner_id'],
#                                       'access_token': self.AOuthData['access_token'],
#                                       'v': 5.89
#                                      }
#
#         answer = requests.get(url = URL_to_get_userinfo, params = parameters_to_get_userinfo)
#         JSONanswer = answer.json()
#         result = catch_error(answer, JSONanswer, 'Отправка запроса для получения информации о пользователе')
#         if result.error == 1:
#             return result
#         list_info = JSONanswer['response'][0]
#         self.user = User(list_info, [self.age_from, self.age_to])
#         return result
#
#     def get_people(self, count_set):
#         self.URL_to_search = 'https://api.vk.com/method/users.search'
#         self.user_token = '3400cd3c01500a3f410966907f38f32f2ca0b8a793cd1f62b4aa3c86c81a5826ad7f159d77f29e101002b'
#         self.parametrs_to_search = {
#             'access_token': self.user_token,
#
#             'has_photo' : True,
#             'sex': int(not(self.user.sex)),
#             'age_from': self.age_from,
#             'age_to': self.age_to,
#             'country': self.user.country_code['id'],
#             'city': self.user.city_code['id'],
#             'sort': 0,
#             'count': 3* count_set,
#             'status': 6,
#             'fields': 'photo_id, country, city, sex',
#             'v': 5.89
#         }
#         answer = requests.get(url=self.URL_to_search, params=self.parametrs_to_search)
#         JSONanswer = answer.json()
#         result = catch_error(answer, JSONanswer, 'Отправка запроса для поиска пары')
#         if result.error == 1:
#             return result
#         list_info = JSONanswer['response']['items']
#         for elem in list_info:
#             person = VKperson(elem)
#             self.user.add_VKperson(person)
#         return result
#
#     def get_photos(self):
#         URL_for_get_photos = 'https://api.vk.com/method/photos.get'
#         parameters_for_photos_get = {
#             'lang': 0,
#             'owner_id': '',
#             'album_id': 'profile',
#             'extended': 1,
#             'feed_type': 'photo',
#             'photo_sizes': 1,
#             'count': 1000,
#             'access_token': self.user_token,
#             'v': 5.89
#         }
#         for person in self.user.VKperson_list:
#             parameters_for_photos_get['owner_id'] = person.id
#
#             answer = requests.get(url = URL_for_get_photos, params = parameters_for_photos_get)
#             JSONanswer = answer.json()
#             result = catch_error(answer, JSONanswer, 'Отправка запроса для получения ссылок для фотографий')
#             if result.error == 1:
#                 return result
#
#             person.list_photos = []
#             list_photos = JSONanswer['response']['items']
#
#             for photo in list_photos:
#                 copy = find_max_size(photo['sizes'])
#                 person.photos.append(Photo(photo['id'], person.id, photo['likes']['count'], copy['url']))
#         return result
#
#            #     likes = photo["likes"]["count"]
#             #     link = photo['url']
#             #
#             #     link_size = find_max_size(photo['sizes'])
#             #     name = f'{str(photo["likes"]["count"])}.jpg'
#             #     if name in list_names.keys():
#             #       list_names[name] = list_names[name] + 1
#             #       name = f'{str(photo["likes"]["count"])}' + f'_{list_names[name]}.jpg'
#             #     else:
#             #       list_names[name] = 1
#             #
#             #     loginfo = {"name": name, "size": link_size['type']}
#             #     photo_name = os.path.join(self.adres_for_save, loginfo["name"])
#             #     elem = {'name': name, 'adres': photo_name}
#             #     self.downloads.append(elem)
#             #
#             #
#             #     name = f'{str(photo["likes"]["count"])}.jpg'
#             #     if name in list_names.keys():
#             #       list_names[name] = list_names[name] + 1
#             #       name = f'{str(photo["likes"]["count"])}' + f'_{list_names[name]}.jpg'
#             #     else:
#             #       list_names[name] = 1
#             #
#             #     with open(photo_name, 'wb') as save_photo:
#             #         data = requests.get(link_size['url'])
#             #         save_photo.write(data.content)
#             #

import json
from pprint import pprint
from urllib.parse import urlencode
import requests

from Iteratirs import GetlinkForPhotos, ListIteration
from LibAdditionalFunction import find_max_size, get_input_data
from Logger import get_log_to_file
from ResultCreation import Result, catch_error
from datetime import date

AOuthData = get_input_data("Data.txt")
def autorize():
    URL_for_autorize = 'https://oauth.vk.com/authorize'
    ID = 7656145
    parameters_for_autorize = {
        'client_id': ID,
        'display': 'popup',
        'scope': 'photos, status',
        'response_type': 'token',
        'v': 5.89
            }
    answer = requests.get(url = URL_for_autorize, params = parameters_for_autorize)
    print('?'.join((URL_for_autorize, urlencode(parameters_for_autorize))))
    print(answer.status_code)

# print('?'.join(
#     (URL_for_autorize, urlencode(param))
# ))
#



class User():
    def init_user(self, infodict):
        self.id = infodict['id']
        self.firs_name = infodict['first_name']
        self.last_name = infodict['last_name']

        self.sex = infodict['sex']
        self.country_code = infodict['country']
        self.city_code = infodict['city']

        born_date = list(map(int, infodict['bdate'].split('.')))
        today = date.today()
        self.age = today.year - born_date[2] - ((today.month, today.day) < (born_date[1], born_date[0]))

        self.VKperson_list = []

        print('init user')
        print('Файл для чтения аутентификационных данных пользователя утановлен по умолчанию как Data.txt')
        input('Пожалуйста, проверьте правильность его заполнения. Нажмите любую клавишу для продолжения.')
        self.age_from = int(input('Ведите нижнюю границу возраста для поиска: '))
        self.age_to = int(input('Ведите верхнюю границу возраста для поиска: '))

    @get_log_to_file('log.txt')
    def get_infouser(self, AOuthData):
        URL_to_get_userinfo = 'https://api.vk.com/method/users.get'
        parameters_to_get_userinfo = {'fields': 'first_name, last_name, bdate, country, city, sex',
                                      'user_ids': AOuthData['owner_id'],
                                      'access_token': AOuthData['access_token'],
                                      'v': 5.89
                                      }

        answer = requests.get(url=URL_to_get_userinfo, params=parameters_to_get_userinfo)
        JSONanswer = answer.json()
        result = catch_error(answer, JSONanswer, 'Отправка запроса для получения информации о пользователе')
        if result.error == 1:
            return result
        list_info = JSONanswer['response'][0]
        self.user = self.init_user(list_info)
        return result

    def FOR_MY_print_elem(self):
        print(f'[User]ID: {self.id}')
        print(f'{self.firs_name} {self.last_name}')
        print(f' {self.country_code}, {self.city_code}')
        print(f' sex: {self.sex}, age: {self.age}')
        print(f'Range_age = [{self.age_from}, {self.age_to}]')
        print('__________________________')


class VKperson():
    def init_VKperson(self, VKperson_infolist):
        self.id = VKperson_infolist['id']
        self.first_name = VKperson_infolist['first_name']
        self.last_name = VKperson_infolist['last_name']
        if 'age' in VKperson_infolist.keys():
            born_date = list(map(int, VKperson_infolist['bdate'].split('.')))
            today = date.today()
            self.age = today.year - born_date[2] - ((today.month, today.day) < (born_date[1], born_date[0]))
        else:
            self.age = None
        self.interest = None

        self.list_photos = []

    @get_log_to_file('log.txt')
    def get_people(self, user, count_set, AOuthData):
        self.URL_to_search = 'https://api.vk.com/method/users.search'
        # self.user_token = '8a622c76171459cf0264bd54fc8deeb3c13d948228025351943fb739f4626262819e50404746d56f96287'
        self.parametrs_to_search = {
            'user_ids': AOuthData['app_id'],
            'access_token': AOuthData['app_access_token'],
            'has_photo' : True,
            'sex': int(not(user.sex)),
            'age_from': user.age_from,
            'age_to': user.age_to,
            'country': user.country_code['id'],
            'city': user.city_code['id'],
            'sort': 0,
            'count': 3* count_set,
            'status': 6,
            'fields': 'photo_id, country, city, sex',
            'v': 5.89
        }
        answer = requests.get(url=self.URL_to_search, params=self.parametrs_to_search)
        JSONanswer = answer.json()
        result = catch_error(answer, JSONanswer, 'Отправка запроса для поиска пары')
        if result.error == 1:
            return result
        list_info = JSONanswer['response']['items']

        for elem in ListIteration(list_info):
            person = VKperson()
            person.init_VKperson(elem)
            user.VKperson_list.append(person)

        # for elem in list_info:
        #     person = VKperson()
        #     person.init_VKperson(elem)
        #     user.VKperson_list.append(person)
        return result

    def FOR_MY_print_elem(self):
        print(f'[VKperson]ID: {self.id}')
        print(f'{self.first_name} {self.last_name}')
        print(f'age: {self.age}, FLAG[{self.interest}]')
        print('__________________________')


class Photo():
    def init_photo(self, Photos_infolist):
        self.id = Photos_infolist['id']
        self.owner_id = Photos_infolist['owner_id']
        self.link_photo = Photos_infolist['link']['url']
        self.likes = Photos_infolist['likes']

    @get_log_to_file('log.txt')
    def get_photoslink(self, VKperson):
        URL_for_get_photos = 'https://api.vk.com/method/photos.get'
        parameters_for_photos_get = {
            'lang': 0,
            'owner_id': '',
            'album_id': 'profile',
            'extended': 1,
            'feed_type': 'photo',
            'photo_sizes': 1,
            'count': 1000,
            'access_token': AOuthData['access_token'],
            'v': 5.89
        }
        parameters_for_photos_get['owner_id'] = VKperson.id

        answer = requests.get(url = URL_for_get_photos, params = parameters_for_photos_get)
        JSONanswer = answer.json()
        result = catch_error(answer, JSONanswer, 'Отправка запроса для получения ссылок для фотографий')
        if result.error == 1:
            return result

        list_photos_link = JSONanswer['response']['items']

        for x in GetlinkForPhotos(list_photos_link, VKperson.id):
            elem_for_phoyolinks_array = Photo()
            elem_for_phoyolinks_array.init_photo(x)
            VKperson.list_photos.append(elem_for_phoyolinks_array)

        return result

    def get_photo(self):
        pass

    def FOR_MY_print_elem(self):
        print(f'[Photo]ID: {self.id}, OWNER ID {self.owner_id}  [{self.likes}] likes')
        print(f'{self.link_photo}')
        print('__________________________')


class SearchPeoples():
    AOuthData = get_input_data("Data.txt")

    def get_(self):
        user = User()

        result = user.get_infouser(self.AOuthData)
        result.print_result()
        user.FOR_MY_print_elem()

        VKpersons = VKperson()
        result = VKpersons.get_people(user, 1, self.AOuthData)
        result.print_result()
        print(len(user.VKperson_list))
        for person in user.VKperson_list:
            person.FOR_MY_print_elem()

        for person in user.VKperson_list:
            photos = Photo()
            result = photos.get_photoslink(person)
            result.print_result()

            for photo in person.list_photos:
                photo.FOR_MY_print_elem()


