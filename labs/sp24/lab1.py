
def toHex(s):
    vals = ["{:2X}".format(ord(c)) for c in s]
    return ''.join(vals)

msg = "Data models are the abstractions used to describe problems.\nData structures are the programming-language constructs used to represent data models.\nAlgorithms are the techniques used to obtain solutions by manipulating data as represented by the abstractions of a data model."
print("\n\n")
print(msg)
print("# symbols: ",len(msg))

print(toHex(msg))
lets = sorted(list(set(msg)))
print(lets)
print("# unique sybmols",len(lets))


#msg2 = "data models are the abstractions used to describe problems"
#print(len(msg2))
#print(sorted(list(set(msg2))))
#print(len(set(msg2)))
