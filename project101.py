import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)

                pc_path = os.path.realpath(localPath, filename)
                dbPath = os.path.join(fileTo, pc_path)

                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dbPath,
                                     mode=WriteMode("Overwrite"))


def main():
    accessToken = "sl.BLZN9YtLIDDskRZLA6UgzvbQh67s4LoZt29wSWc22qRoCuZx1aTmuPXr2uE4s1qqX41goIyGLF-Nr-p-uGx7EhzOhomXeQ-KF35pak6gKVhbadMkeKVgRVbGsoEaeSi2fdh2gFUZcoI"
    transferData = TransferData(accessToken)

    file_from = str(
        input("Enter the file path which you want to transfer: \n"))
    file_to = input(
        "Enter the dropbox folder full path where you want to upload file: \n")
    transferData.uploadFiles(file_from, file_to)
    print("File successfully uploaded on the cloud!")
    print("Now you can see it anywhere!")


main()
