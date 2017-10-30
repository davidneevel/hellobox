import textwrap
wrapnumber = 23

text = "why is the world in love again why are we standing hand in hand why are the ocean levels rising up it's a brand new record for 1990 they might be giants brand new album flood"

wrapped = textwrap.wrap(text, wrapnumber)

print wrapped


print wrapped[0]
print wrapped[1]
print wrapped[2]
print wrapped[3]



print "as opposed to"

wrapped = textwrap.fill(text, wrapnumber)
print wrapped