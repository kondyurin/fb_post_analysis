from urllib.parse import urlparse
from os.path import splitext, basename
import requests

def download_photo():
    url = "https://graph.facebook.com/v2.8/509679185734909/feed?fields=message,from,attachments,comments{message,comments},likes&access_token=308758979483229%7C227308c4dceeb3bd9c35d8e7ffa25b59"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
    else:
        print('not 200 OK')
    
    for image in data['data']:
        row = image.get('attachments', {})

        for img in row.get('data', []):
            img_type = img.get("type")
            print('img_type: ', img_type, type(img) is dict)

            if img_type == "photo":
                media_page = img.get('media', {})
                image_page = media_page.get('image', {})
                src_page = image_page.get('src')
                print('src_page: ', src_page)

                if src_page:
                    disassembled = urlparse(src_page)
                    filename, file_ext = splitext(basename(disassembled.path))
                    result = filename + file_ext
                    response = requests.get(src_page)
                    if response.status_code == 200:
                        with open(result, 'wb') as imgfile:
                            imgfile.write(response.content)

            elif img_type == "album":
                subattachments_page = img.get('subattachments', {})
                data_page = subattachments_page.get('data', [])
                for subimg in data_page:
                    media_page = subimg.get('media', {})
                    image_page = media_page.get('image', {})
                    src_page = image_page.get('src')

                    if src_page:
                        disassembled = urlparse(src_page)
                        filename, file_ext = splitext(basename(disassembled.path))
                        result = filename + file_ext
                        response = requests.get(src_page)

                        if response.status_code == 200:
                            with open(result, 'wb') as imgfile:
                                imgfile.write(response.content)

            # elif img_type == "share":
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
                    

download_photo() 