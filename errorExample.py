import traceback
try:
    raise Exception('This is the error meassge.')
except:
    errorFile = open('errorInfo.txt', 'w')

try:
    raise Exception('This is the error meassge.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
