import macaddress
import random
import uuid
import datetime

fileName = input("Please enter the exported file name : ")
print()
filepath = input("Please enter the path of Windows DHCP reservation export file.\nIf the file is in the same directory with the script please leave blank :")

fullPath = ""
if filepath == "":
    fullPath = fileName
elif filepath.endswith('\\'):
    fullPath = filepath + filepath
else:
    fullPath = filepath + "\\" + filepath

final = "config reserved-address\n"
try:
    with open(fullPath, 'r') as file:
        lines = file.readlines()
        j = 1
        for i in lines:
            if j + 1 > 2:
                sp = i.split('\t')
                mac = macaddress.MAC(sp[4])
                final += 'edit {0} \nset ip {1}\nset mac {2}\nset description {3}next\n'.format((j - 1), sp[0], str(mac).replace('-', ':'), sp[1])

            j += 1
except IOError as err:
    print(err)

final += "end"
uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')

outfilename = "fortiscript_{0}.txt".format(uniq_filename)

try:
    with open(outfilename, 'w') as f:
        f.write(final)
except IOError as err:
    print(err)

print("{0} generated from {1}".format(outfilename, fullPath))
print("You can copy and paste it to your\x1B[3m config system dhcp server\x1B[0m -\x1B[3m edit ""XXXXXX""\x1B[0m")

