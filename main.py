import vk_api
import requests


session = vk_api.VkApi(token='vk1.a.7fauLrHPcoxqNsV-m5bmGvnV-_qlPtJHbinpjnu2PPXOyigNOQFUXIILVPsdZMZ4-s5R7nGXlbKE8pggQCLEDe7QT1bFKoRaqVsn7PHlfjiq9Odvi9qUnp9UAy6GovdX6n_cJ7FbCPWDSUH_lirXiSUYA_EQQQnntkvmiUqxm11KvSBHDZ_0kXAzHtbrXo9SKJalbCTu0pkF7EZON1GWhw')
vk = session.get_api()
def upload_photo_to_group_wall(photo):
    upload_url = vk.photos.getWallUploadServer(group_id=221162187, album_id=292733933)['upload_url']
    request = requests.post(upload_url, files={'file': open(photo, "rb")})
    save_wall_photo = vk.photos.saveWallPhoto(group_id=221162187,
                                              photo=request.json()['photo'],
                                              server=request.json()['server'],
                                              hash=request.json()['hash'])
    saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
    vk.wall.post(owner_id=-221162187, attachments=saved_photo)
    print('Фото успешно загружено')
upload_photo_to_group_wall('файл с фото')