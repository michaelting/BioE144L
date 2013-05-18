load 1m9bA.complex.pdb
bg_color white
hide all
resume 1m9bA.cbcvg
show spheres, chain A
zoom chain A
remove   (not (chain A or  resn IBG))
color green, resn IBG
show sticks, resn IBG 
hide spheres, resn IBG 
