# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import datetime

in1 = "1536557984.290    "
in2 = 0
in3 = " 127.0.0.1 TCP_MISS/301 "
in4 = " GET http://www.instagram.com/ - HIER_DIRECT/185.60.216.37 text/plain"

start_time = datetime.datetime.now()

with open("output.txt", "w") as op:
    while True:
        in2 += 1
        st_final = in1 + str(in2) + in3 + str(in2) + in4
        op.write(st_final + '\n')
        print(st_final)

end_time = datetime.datetime.now()
print("Number: ", in2, "\nStart Time: ",
      start_time, "End Time: ", end_time)
