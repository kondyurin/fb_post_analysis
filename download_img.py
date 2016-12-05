from urllib.parse import urlparse
from os.path import splitext, basename
import requests
from settings import access_token

page_id = '509679185734909' #id группы FB
post_limit = 10 #кол-во загружаемых постов

def download_photo():
    url = "https://graph.facebook.com/v2.8/{}/feed?fields=updated_time,created_time,message,from,attachments,likes&limit={}&access_token={}".format(page_id, post_limit, access_token)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        print('not 200 OK')
    
    list_src_page = []
    list_message_id = []

    for image in data['data']:
        row = image.get('attachments', {})
        message_id = image.get('id', '')
        for img in row.get('data', []):
            img_type = img.get("type")
            print(img_type)
            if img_type == "photo":
                src_page = img.get('media', {}).get('image', {}).get('src')

                if src_page:
                    list_src_page.append(src_page)
                    list_message_id.append(message_id)
                    result = dict(zip(list_src_page, list_message_id))
                    for key, value in result.items():
                        print('{} {}'.format(key, value))

                    # print(src_page)
                    # disassembled = urlparse(src_page)
                    # filename, file_ext = splitext(basename(disassembled.path))
                    # result = filename + file_ext
                    # response = requests.get(src_page)
                    # if response.status_code == 200:
                    #     with open(result, 'wb') as imgfile:
                    #         imgfile.write(response.content)

            elif img_type == "album":
                subattachments_page = img.get('subattachments', {}).get('data', [])
                for subimg in subattachments_page:
                    src_page = subimg.get('media', {}).get('image', {}).get('src')
                    if src_page:
                        list_src_page.append(src_page)
                        list_message_id.append(message_id)
                        result = dict(zip(list_src_page, list_message_id))
                        for key, value in result.items():
                            print('{} {}'.format(key, value))
                        # print(src_page)
                        # disassembled = urlparse(src_page)
                        # filename, file_ext = splitext(basename(disassembled.path))
                        # result = filename + file_ext
                        # response = requests.get(src_page)

                        # if response.status_code == 200:
                        #     with open(result, 'wb') as imgfile:
                        #         imgfile.write(response.content)

            elif img_type == "share":
                continue
            #     media_page = img.get('media', {})
            #     image_page = media_page.get('image', {})
            #     src_page = image_page.get('src')
            #     print('src_page: ', src_page)

            #     if src_page:
            #         disassembled = urlparse(src_page)
            #         filename, file_ext = splitext(basename(disassembled.path))
            #         result = filename + file_ext
            #         response = requests.get(src_page)
            #         if response.status_code == 200:
            #             with open(result, 'wb') as imgfile:
            #                 imgfile.write(response.content)
            # print(result)

download_photo() 