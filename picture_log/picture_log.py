import cv2
import os.path
import datetime
import yagmail


def get_name():
    """uses current time as a name to fails and logs"""

    time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    return f"{time}.png"


def save_img(result, image):
    """save image to data directory"""

    path = " -- your full path -- /data/"  # place the path to the data folder
    name = get_name()
    cv2.imwrite(f"{path}{name}", image)

    """after image is saved call the mail function"""

    send_mail()


def img_error_log(*args):
    """log errors to a txt file in data directory"""

    path = " -- your full path -- /data/"  # place the path to the data folder
    name = "error.txt"
    complete_name = os.path.join(path, name)
    error_file = open(complete_name, "a")

    write_to_file = f"ERROR -- {args} {get_name()}\n"  # catches errors from webcam or sending mail and logs them
    error_file.write(write_to_file)
    error_file.close()


def take_picture():
    """function to take a picture"""

    cam_port = 0  # port 0 is from webcam
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()

    if result:
        save_img(result, image)  # takes picture and saves it locally to data directory
    else:
        img_error_log('Cam Problem')  # calls the function and registers it locally to text file in data directory


def send_mail():
    """send mail function"""

    receiver = "-- your mail --@gmail.com"  # place your gmail
    user = "-- your mail --@gmail.com"  # place your gmail
    password = "-- generated password --"  # you get this password from gmail settings

    file_name = get_name()  # gets the same name as the saved/error file
    file_path = " -- your full path -- /data/"
    attached_file = f"{file_path}{file_name}"
    body = ""

    yag = yagmail.SMTP(user, password)

    try:
        yag.send(
            to=receiver,
            subject=f"UNLOCK DETECTED {file_name}",
            contents=body,
            attachments=attached_file
        )
    except:
        img_error_log('Mail Problem')  # calls the function and registers it locally to text file in data directory


if __name__ == "__main__":
    take_picture()
