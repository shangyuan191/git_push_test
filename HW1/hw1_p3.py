v=int(input("input velocity:"))
c=299792458
p=round(v/c,6)
r=1*(((1-(v**2/c**2))**0.5)**-1)
al=4.3
ba=6.0
be=309
an=2000000
print("Input velocity: "+str(v))
print("Percentage of light speed = "+str(p))
print("Travel time to Alpha Centauri = "+str(al/r))
print("Travel time to Barnard's Star = "+str(ba/r))
print("Travel time to Betelgeuse (in the Milky way) = "+str(be/r))
print("Travel time to Andromeda Galaxy (closest galaxy) = "+str(an/r))