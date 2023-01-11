def matrix_mult(left_matrix:list, right_matrix:list):
    if len(left_matrix[0]) != len(right_matrix):
        print("Error")
        return
    else:
        output_matrix = []
        for i in range(len(right_matrix)):
            temp_matrix = []
            for j in range(len(right_matrix[0])):
                temp_matrix.append(0)
            output_matrix.append(temp_matrix)

        for row in range(len(output_matrix)):
            for column in range(len(output_matrix[0])):
                num = 0
                for i in range(len(left_matrix)):
                    num += (left_matrix[row][i] * right_matrix[i][column])

                output_matrix[row][column] = round(num,2)

        return output_matrix


def find_conversions(v: int, t: int, y: int, z: int):
    c = 3 * 10 ** 8
    if v > c:
        return ValueError

    gama = (1 - (v ** 2) / (c ** 2)) ** .5
    l = v * t * 365 * 24 * 60 * 60
    print(gama)
    static_frame_list = []
    multiply_operator = []
    for i in range(4):
        static_frame_list.append([])
        temp_list = []
        for j in range(4):
            temp_list.append(0)

        multiply_operator.append(temp_list)

    static_frame_list[0].append(t)
    static_frame_list[1].append(l)
    static_frame_list[2].append(y)
    static_frame_list[3].append(z)

    multiply_operator[0][0] = gama
    multiply_operator[1][1] = gama
    multiply_operator[2][2] = 1/gama
    multiply_operator[3][3] = 1

    motion_frame_list = matrix_mult(multiply_operator, static_frame_list)
    return motion_frame_list


v = int(input("v:"))
t = int(input("t:"))
# l = int(input("l:"))
y = int(input("y:"))
z = int(input("z:"))

print(find_conversions(v, t, y, z))
297000000
100
1000
2

