#import pdb; pdb.set_trace()
import math

bin_leet_num = 0b10100111001
oct_leet_num = 0o2471
hex_leet_num = 0x539
int_leet_num = 1337 
float_leet_num = 1337e3
squared_leet_num = int_leet_num ** 2

print("type cast formatting")
print("Integer:", int_leet_num,"Float:", float_leet_num, "Binary:", bin(int_leet_num),"Octal:", oct(int_leet_num), "Hexadecimal:", hex(int_leet_num))
print()
print("f-string formatting")
print(f"Integer: {int_leet_num}, Float: {float_leet_num:.3f}, Binary: {int_leet_num:016b}, Octal: {int_leet_num:08o}, Hexadecimal: {int_leet_num:08x}")
print()
print("Squared:", squared_leet_num)
print(f"Square root: {math.sqrt(int_leet_num):.3f}")
