import os
import time
import sys

color_yellow = "\33[93m"
color_default = "\033[0m"
color_blue = "\33[34m"
color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_pink = "\033[95m"

print("""\n\nSo, tell me when you're gonna let me in
I'm getting tired, and I need somewhere to begin
And if you have a minute, why don't we go\n""")

line_1_1= "This "
line_1_2 = "could be the end of "
line_1_3 = "every"
line_1_4 = "thing\n"


for char in line_1_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(0.02)

for char in line_1_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

time.sleep(0.2)

for char in line_1_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

for char in line_1_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.26)

line_2_1= "So why don't "
line_2_2 = "we go\n"
line_2_3 = f"Somewhere only we "
line_2_4 = f"know?\n"

time.sleep(0.05)

for char in line_2_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

for char in line_2_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

time.sleep(0.7)

for char in line_2_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

for char in line_2_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(2.2)

line_2_4 = f"{color_yellow}Somewhere only we "
line_2_5 = f"know?\n\n"

for char in line_2_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.11)

for char in line_2_5:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.35)

time.sleep(4)

line_3_1= f"{color_default}Oh simple "
line_3_2 = "thing, "
line_3_3 = "where have you " 
line_3_4 = "gone?\n"


for char in line_3_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

for char in line_3_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.3)

time.sleep(0.1)

for char in line_3_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)

for char in line_3_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.25)

time.sleep(0.48)

line_4_1= "I'm getting old and I need something to "
line_4_2 = "rely on\n"

for char in line_4_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

time.sleep(0.02)

for char in line_4_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.16)

time.sleep(0.95)

line_5_1 = "So tell me "
line_5_2 = "when "
line_5_3 = "you're gonna let me "
line_5_4 = "in\n\n"


for char in line_5_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.11)

for char in line_5_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.4)

time.sleep(0.01)

for char in line_5_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

for char in line_5_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.4)

time.sleep(0.6)

line_6_1 = "I'm "
line_6_2 = "get"
line_6_3 = "ting "
line_6_4 = "tired, " 
line_6_5 = "and "
line_6_5_1 = "I " 
line_6_5_2 = "need "
line_6_6 = "some"
line_6_7 = "where "
line_6_8 = "to "
line_6_9 = "begin\n\n"

print(line_6_1, end="")
time.sleep(0.3)

print(line_6_2, end="")
time.sleep(0.3)

print(line_6_3, end="")
time.sleep(0.3)

print(line_6_4)
time.sleep(0.3)

print(line_6_5, end="")
time.sleep(0.3)
           
print(line_6_5_1, end="")
time.sleep(0.3)

print(line_6_5_2)
time.sleep(0.3)

print(line_6_6, end="")
time.sleep(0.6)

print(line_6_7)
time.sleep(0.3)

print(line_6_8, end="")
time.sleep(0.4)

for char in line_6_9:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.3)

time.sleep(0.35)

line_7_1 = "And "
line_7_1_1 = "if "
line_7_2 = "you have a minute, " 
line_7_3 = "why don't " 
line_7_4 = "we go\n"

for char in line_7_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.15)

for char in line_7_1_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.25)

for char in line_7_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

for char in line_7_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

for char in line_7_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(1.35)

line_8_1 = "Talk "
line_8_1_1 = "about "
line_8_1_1_1 = "it "
line_8_1_2 = f"{color_yellow}somewhere only " 
line_8_1_3 = "we know?"

for char in line_8_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

for char in line_8_1_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)


for char in line_8_1_1_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.06)

for char in line_8_1_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

for char in line_8_1_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.3)

time.sleep(0.25)

print(f"{color_default}")

for char in line_1_1:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(0.02)

for char in line_1_2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

time.sleep(0.1)

for char in line_1_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.08)

for char in line_1_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.25)
 


line_9_1 = f"{color_yellow}\nSo "
line_9_1_1 ="why " 
line_9_1_2 = "don't "
line_9_1_3 = "we \n"
line_9_1_4 ="go?\n"

print(line_9_1)
time.sleep(0.35)

print(line_9_1_1)
time.sleep(0.35)

print(line_9_1_2)
time.sleep(0.35)

for char in line_9_1_3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.09)


for char in line_9_1_4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.09)

time.sleep(0.75)

line_9_2_1 = "\nwe "
line_9_2_2 ="go?"


print(line_9_1, end="\r")
time.sleep(0.35)

print(line_9_1_1, end="\r")
time.sleep(0.35)

print(line_9_1_2, end="\r")
time.sleep(0.35)
sys.stdout.write("\033[2K\r")
sys.stdout.flush()

for line in line_9_2_1:
    sys.stdout.write(line)
    sys.stdout.flush()
    time.sleep(0.06)

for line in line_9_2_2:
    sys.stdout.write(line)
    sys.stdout.flush()
    time.sleep(0.2)


terminal_height, terminal_width = os.get_terminal_size()
sys.stdout.write("\n" * terminal_height)  

color_yellow = "\033[93m"
color_pink = "\033[95m"
color_green1 = "\033[92m"
reset_color = "\033[0m"


lines = ["So why don't we go?", "So why don't we go?", "So why don't we go?", 
         "So why don't we go?", "So why don't we go?", "So why don't we go?", 
         "So why don't we go?"]

colors = [color_pink, color_pink, color_pink, color_pink, color_green1, color_green1, color_green1]

max_len = max(len(line) for line in lines)

for i in range(max_len):
    for j, (line, color) in enumerate(zip(lines, colors)):
        if i < len(line):
            sys.stdout.write("\033[{};1H".format(j+1))  
            sys.stdout.write(color) 
            sys.stdout.write(line[:i+1])  
            sys.stdout.write(reset_color)  
            sys.stdout.flush()
    time.sleep(0.06)

print("\n")

