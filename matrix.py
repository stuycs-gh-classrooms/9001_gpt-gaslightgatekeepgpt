'''
make a file with exactly these functions: make_bezier, make_hermite, generate_curve_coefs, make_translate, make_scale, make_rotX, make_rotY, make_rotZ, print_matrix ,ident, matrix_mult, new_matrix

ok, write code in python to fulfill these requirements:
Write code to work with transformation matrices:

    create a translation matrix
    create a scale matrix
    create a rotation matrix about the x-axis
    create a rotation matrix about the y-axis
    create a rotation matrix about the z-axis
'''

import math

def make_bezier():
    # Bezier matrix
    return [[-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 3, 0, 0],
            [1, 0, 0, 0]]


def make_hermite():
    # Hermite matrix
    return [[2, -2, 1, 1],
            [-3, 3, -2, -1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]]


def generate_curve_coefs(p0, p1, p2, p3, curve_type):
    if curve_type == "hermite":
        result = [[2, -3, 0, 1],
                  [-2, 3, 0, 0],
                  [1, -2, 1, 0],
                  [1, -1, 0, 0]]
    elif curve_type == "bezier":
        result = [[-1, 3, -3, 1],
                  [3, -6, 3, 0],
                  [-3, 3, 0, 0],
                  [1, 0, 0, 0]]
    else:
        print("Invalid curve type")
        return None
    
    x_coefs = [[p0[0], p1[0], p2[0], p3[0]]]
    y_coefs = [[p0[1], p1[1], p2[1], p3[1]]]
    z_coefs = [[p0[2], p1[2], p2[2], p3[2]]]
    
    x_result = matrix_mult(x_coefs, result)
    y_result = matrix_mult(y_coefs, result)
    z_result = matrix_mult(z_coefs, result)
    
    return [x_result[0], y_result[0], z_result[0], [1, 0, 0, 0]]

def make_translate(x, y, z):
    result = [[1, 0, 0, x],
              [0, 1, 0, y],
              [0, 0, 1, z],
              [0, 0, 0, 1]]
    return result

def make_scale(x, y, z):
    result = [[x, 0, 0, 0],
              [0, y, 0, 0],
              [0, 0, z, 0],
              [0, 0, 0, 1]]
    return result

def make_rotX(theta):
    radians = math.radians(theta)
    c = math.cos(radians)
    s = math.sin(radians)
    result = [[1, 0, 0, 0],
              [0, c, -s, 0],
              [0, s, c, 0],
              [0, 0, 0, 1]]
    return result

def make_rotY(theta):
    radians = math.radians(theta)
    c = math.cos(radians)
    s = math.sin(radians)
    result = [[c, 0, s, 0],
              [0, 1, 0, 0],
              [-s, 0, c, 0],
              [0, 0, 0, 1]]
    return result

def make_rotZ(theta):
    radians = math.radians(theta)
    c = math.cos(radians)
    s = math.sin(radians)
    result = [[c, -s, 0, 0],
              [s, c, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]
    return result

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f"{element:.2f}", end=" ")
        print()

def ident(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
        matrix[i][i] = 1

def matrix_mult(m1, m2):
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m2[0])):
            total = 0
            for k in range(len(m1[0])):
                total += m1[i][k] * m2[k][j]
            result[i].append(total)
    for i in range(len(result)):
        for j in range(len(result[i])):
            m1[i][j] = result[i][j]

def new_matrix(rows, cols):
    result = []
    for i in range(rows):
        result.append([])
        for j in range(cols):
            result[i].append(0)
    return result


t = make_translate(1, 2, 3)
r = make_rotX(90)
print_matrix(t)
print("")
print_matrix(r)
