
# slicing strings is a technique used to return substrings (parts of the original string), informing start, stop and step: [start:stop[:step]]

txt = "Miguel and Dmitri"

print(txt[:])
# Miguel and Dmitri

print(txt[0])
# M

print(txt[:6])
# Miguel

print(txt[11:])
# Dmitri

print(txt[7:11])
# and

print(txt[7:11:2])
# ad

print(txt[11::2])
# Dir

print(txt[::-1])
# irtimD dna leugiM
# Miguel and Dmitri