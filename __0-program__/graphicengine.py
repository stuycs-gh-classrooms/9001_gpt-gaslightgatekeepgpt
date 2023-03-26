import math

# function to create PPM file from list containing pixel values
def save_ppm(filename, img):
    with open(filename, "wb") as f:
        header = "P6\n{} {}\n255\n".format(len(img[0]), len(img))
        f.write(bytes(header, "ascii"))
        for row in img:
            for pixel in row:
                f.write(bytes(pixel))

# matrix multiplication
def matmul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# function to apply a transformation matrix to a list of points
def transform(points, matrix):
    new_points = []
    for point in points:
        p = [point[0], point[1], 1]
        new_p = matmul([p], matrix)[0]
        new_points.append((int(new_p[0]), int(new_p[1])))
    return new_points

# function to draw a line using Bresenham's algorithm
def draw_line(img, x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while x1 != x2 or y1 != y2:
        img[y1][x1] = color
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    img[y1][x1] = color

# function to draw an edge list
def draw_edge_list(img, edge_list, color):
    for i in range(0, len(edge_list) - 1, 2):
        x1, y1, x2, y2 = edge_list[i][0], edge_list[i][1], edge_list[i+1][0], edge_list[i+1][1]
        draw_line(img, x1, y1, x2, y2, color)

# create a blank image
img = [[[0, 0, 0] for j in range(512)] for i in range(512)]

# edge list of a triangle
edge_list = [(100, 100), (300, 100),
             (300, 100), (200, 300),
             (200, 300), (100, 100)]

# draw the original triangle
draw_edge_list(img, edge_list, [255, 255, 255])

# translation matrix
T = [[1, 0, 100],
     [0, 1, 200],
     [0, 0, 1]]

# rotate 30 degrees counterclockwise about origin matrix
R = [[math.cos(math.pi/6), -math.sin(math.pi/6), 0],
     [math.sin(math.pi/6), math.cos(math.pi/6), 0],
     [0, 0, 1]]

# dilation matrix
D = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 1]]

# apply transformations
edge_list = transform(edge_list, T)
edge_list = transform(edge_list, R)
edge_list = transform(edge_list, D)

# draw the transformed triangle
draw_edge_list(img, edge_list, [255, 0, 0])

# save and display the image
save_ppm("output.ppm", img)
import subprocess
subprocess.call("open output.ppm", shell=True)
