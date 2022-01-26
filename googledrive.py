from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

dir_credentials = 'credentials_module.json'


# initial login
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(dir_credentials)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(dir_credentials)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)


# create text file
def create_text_file(name_file, content, id_folder):
    credential = login()
    file = credential.CreateFile(
        {'title': name_file, 'parents': [{'kind': 'drive#fileLink', 'id': id_folder}]}
    )
    file.SetContentString(content)
    file.Upload()


def upload_file(file_path, id_folder):
    credential = login()
    file = credential.CreateFile(
        {'parents': [{'kind': 'drive#fileLink', 'id': id_folder}]}
    )
    file['title'] = file_path.split('/')[-1]
    file.SetContentFile(file_path)
    file.Upload()


def down_file(id_file, file_path):
    credential = login()
    file = credential.CreateFile({'id': id_file})
    name_file = file['title']
    file.GetContentFile(file_path + name_file)


def search(query):
    result = []
    credential = login()
    list_file = credential.ListFile({'q': query}).GetList()

    for f in list_file:
        print(f['id'])
        print(f['embedLink'])
        print(f['downloadUrl'])
        print(f['title'])
        print(f['mimeType'])
        print(f['labels']['trashed'])
        print(f['createdDate'])
        print(f['modifiedDate'])
        print(f['version'])
        print(f['fileSize'])
        result.append(f)
    return result


def delete_recover(id_file):
    credential = login()
    file = credential.CreateFile({'id': id_file})
    file.Trash()
    file.UnTrash()
    file.Delete()


if __name__ == "__main__":
    #    create_text_file(
    #        'myhellodrive.txt', 'hi testing googleDrive!', '0B6ZvE'
    #    )
    #    upload_file(
    #        '/home/xxx/xxx/margaretHamilton.png', '0B6Zv4'
    #    )
    #    down_file('1Ab8jXecFy01NJw', '/home/ali/Downloads/')
    #    search("title = 'Workshop Git.pdf'")
    delete_recover('1gL50CiRhsr4UXqqu3')
