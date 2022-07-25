import os

a = str(os.environ['PATH']).split(';')[0].split('Scripts')[0].replace('\\','/')
a+='lib/site-packages/keras_vggface/models.py'
    
import fileinput

for line in fileinput.input(a, inplace=True):
    if 'keras.engine.topology' in line:
        print('from keras.utils import get_source_inputs')
    else:
        print(line, end='')
        
os.system('streamlit run .\main.py')