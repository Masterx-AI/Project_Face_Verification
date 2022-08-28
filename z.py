import os
# os.system('sudo apt-get install opencv-python-headless -y')
# os.system('pip install opencv-python-headless==4.5.5.64')
# os.system('sudo apt--get install libgl1')
# import cv2

# os.system("sudo apt update")
# os.system("sudo apt -y install python3 python3-pip python3-setuptools python3-dev")
# os.system("sudo pip3 install --upgrade tensorflow requests")

for i in os.environ['PATH'].split(';'):
    a = str(i.split('Scripts')[0].replace('\\', '/')) + 'site-packages/keras_vggface/models.py'

    try:
        with open(a, 'r') as file:
            content = file.read()
            print(len(content))
        content = content.replace('keras.engine.topology', 'keras.utils')
        with open(a, 'w') as file:
            file.write(content)
    except Exception:
        pass

os.system('streamlit run main.py')


# import os
# # print(os.environ['PATH'])

# for i in os.environ['PATH'].split(';'):
#     a = str(i.split('Scripts')[0].replace('\\','/'))
#     print(a)
#     a+='site-packages/keras_vggface/models.py'
#     try:
#         with open(a, 'r') as file:
#             content = file.read()
#             print(len(content))
#         # content = content.replace('keras.engine.topology', 'keras.utils')
#         # with open(a, 'w') as file:
#         #     file.write(content)
#     except:
#         pass