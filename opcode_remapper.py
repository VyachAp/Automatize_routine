import re
import random

current_opcode_file = open('../cpython/Lib/opcode.py')
non_argument = [x for x in range(1, 90)]
single_argument = [x for x in range(90, 144)]
extended_args = [x for x in range(144, 255)]
random.shuffle(non_argument)
random.shuffle(single_argument)
random.shuffle(extended_args)
regex_for_opcode = r'^(?P<key>[a-z_]+)+\(\'+(?P<name>[A-Z_]+)+\'+\,\s+(?P<code>\d+)(?P<extra>.*)'
new_opcode_file = open('opcode.py', 'w+')
previous_code = None
for line in current_opcode_file.readlines():
    rex = re.compile(regex_for_opcode).match(line)
    if rex:
        op_code = int(rex.group('code'))
        if op_code < 90:
            new_code = non_argument.pop()
            line = line.replace(rex.group('code'), str(new_code))
            new_opcode_file.write(line)
            previous_code = new_code
        elif op_code < 144:
            new_code = single_argument.pop()
            line = line.replace(rex.group('code'), str(new_code))
            new_opcode_file.write(line)
            previous_code = new_code
        else:
            new_code = extended_args.pop()
            line = line.replace(rex.group('code'), str(new_code))
            new_opcode_file.write(line)
            previous_code = new_code
    else:
        new_opcode_file.write(line)
