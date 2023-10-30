import vk_api
import requests


session = vk_api.VkApi(token='token')
vk = session.get_api()
def upload_photo_to_group_wall(photo):
    upload_url = vk.photos.getWallUploadServer(group_id='d', album_id='d')['upload_url']
    request = requests.post(upload_url, files={'file': open(photo, "rb")})
    save_wall_photo = vk.photos.saveWallPhoto(group_id=221162187,
                                              photo=request.json()['photo'],
                                              server=request.json()['server'],
                                              hash=request.json()['hash'])
    saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
    vk.wall.post(owner_id=-'ds', attachments=saved_photo)
    print('Фото успешно загружено')
upload_photo_to_group_wall('файл с фото')