# Create 1000x1000 grid
N = 7
M = 127

plane = [[']'] for i in range(N)]
for i in range(N):
    for j in range(M):
        plane[i].append([''])



def print_plane():
    for i in range(N):
        for j in range(M):
            print(plane[i][j])

def set_plane(x,y):
    plane[x][y] = "#"

