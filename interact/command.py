import os

cmd = "git --version"
os.system(cmd)
returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)

#os.popen("python D:/iot/manage.py runserver")
