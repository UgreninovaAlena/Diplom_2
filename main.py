from pprint import pprint
from urllib.parse import urlencode

import requests

import ForDatabase as db
import ForVK as VK
from ResultCreation import Result


#
# db.BASE.metadata.create_all(db.engine)
# session = db.session
# users = session.query(db.Photos).all()
# print(users)

#
# URL_for_autorize = 'https://oauth.vk.com/authorize'
# ID = 7656145
# param = {
#     'client_id': ID,
#     'display': 'popup',
#     'scope': 'photos, status',
#     'response_type': 'token',
#     'v': 5.89
# }
# print('?'.join(
#     (URL_for_autorize, urlencode(param))
# ))
#
# object = VK.SearchPeoples()
# result = object.init_user()
# result.print_result()
#
# result = object.get_people(1)
# result.print_result()
#
# result= object.get_photos()
# for elem in object.user.VKperson_list:
#     print(elem.first_name)
#     print(elem.photos)
#     for fot in elem.photos:
#         fot.FOR_MY_print_elem()
#     print('__________')
# result.print_result()



object = VK.SearchPeoples()
object.get_()



# # VK.autorize()
# URL_for_autorize = 'https://oauth.vk.com/authorize'
# ID = 7656145
# param = {
#     'client_id': ID,
#     'display': 'popup',
#     'scope': 'photos, status',
#     'response_type': 'token',
#     'v': 5.89
# }
# url = '?'.join(
#     (URL_for_autorize, urlencode(param))
# )
# ans = requests.get(url)
# print(url)
