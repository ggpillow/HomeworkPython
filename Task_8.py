from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from urllib.parse import quote


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    oauth_token = None
    image_url = None

    def do_GET(self):
        file_path = "Uploads/UserImage.jpg"
        html_response = "<html><head><meta charset='utf-8'></head><body>"

        
        response = requests.get(
            f"https://cloud-api.yandex.net/v1/disk/resources?path={quote(file_path)}",
            headers={"Authorization": self.oauth_token}
        )

        if response.status_code == 200:
            html_response += f"<div style='background-color: rgba(0, 200, 0, 0.25);'>{file_path} - Файл уже загружен.</div>"
        else:
            
            upload_link_response = requests.get(
                f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={quote(file_path)}&overwrite=true",
                headers={"Authorization": self.oauth_token}
            )
            if upload_link_response.status_code == 200:
                upload_link = upload_link_response.json().get('href')

                
                upload_file_response = requests.put(upload_link, data=requests.get(self.image_url).content)
                if upload_file_response.status_code == 201:
                    html_response += f"<div style='background-color: rgba(0, 200, 0, 0.25);'>{file_path} - Файл успешно загружен.</div>"
                else:
                    html_response += f"<div>{file_path} - Ошибка загрузки файла.</div>"
            else:
                html_response += f"<div>{file_path} - Не удалось получить ссылку для загрузки.</div>"

        html_response += "</body></html>"
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(html_response.encode('utf-8'))


def run_server():
    
    oauth_token = input("Введите OAuth токен Яндекс.Диска: ")
    SimpleHTTPRequestHandler.oauth_token = f"OAuth {oauth_token}"

    
    image_url = input("Введите ссылку на изображение: ")
    SimpleHTTPRequestHandler.image_url = image_url

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Сервер запущен на порту 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()