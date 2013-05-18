load 1m9bA.complex.pdb
bg_color white
hide all
resume 1m9bA.cbcvg
show spheres, chain A
zoom chain A
remove   (not (chain A or chain B))
set cartoon_transparency, 0.5 
cartoon tube 
color green, chain B 
show cartoon,  chain B
