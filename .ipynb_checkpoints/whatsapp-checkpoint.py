import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you want to send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

# Send the text message
pywhatkit.sendwhatmsg(mobile, message, hour, minute)

# Optionally, send a file (image in this case)
send_file = input('Do you want to send a file? (yes/no): ').strip().lower()
if send_file == 'yes':
    file_path = input('Enter the full path of the file (image) to send: ')
    caption = input('Enter a caption for the file: ')
    pywhatkit.sendwhats_image(mobile, file_path, caption)