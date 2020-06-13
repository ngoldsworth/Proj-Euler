import numpy as np

grid = np.genfromtxt('11.csv', delimiter=",")

# Want dimensions of grid
height = np.shape(grid)[0]
width = np.shape(grid)[1]

# Need to add "buffer" so that paths that go off the edge have product zero
z0 = np.zeros((4, width))
z1 = np.zeros((height+4, 4))

midgrid = np.concatenate((grid,z0), axis=0)
supergrid = np.concatenate((midgrid, z1), axis=1)

# Create function that finds a vertical, horizontal, and diagonal product
# at each point (i,j) in the grid

def prodlist(i, j):
    hprod = supergrid[(i,j)]*supergrid[(i,j+1)]*supergrid[(i,j+2)]*supergrid[(i,j+3)]
    vprod = supergrid[(i,j)]*supergrid[(i+1,j)]*supergrid[(i+2,j)]*supergrid[(i+3,j)]
    dprod = supergrid[(i,j)]*supergrid[(i+1,j+1)]*supergrid[(i+2,j+2)]*supergrid[(i+3,j+3)]
    return(max(hprod, vprod, dprod))


# Initialize value of maximum product
maxprod = 0

for i in range(height):
    for j in range(width):
        ijmax = prodlist(i,j)
        maxprod=max(maxprod,ijmax)

print(maxprod)
