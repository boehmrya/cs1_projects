

# rotates a one-dimensional matrix one position to the right
# the item in the last position assumes the first position
def rotateRight1D(matrix):
     newMatrix = [0] * len(matrix) #initialize the new matrix
     i = 0
     while i < len(matrix):
          if i == (len(matrix) - 1):
               newMatrix[0] = matrix[i]
          else:
               newMatrix[i + 1] = matrix[i]
          i += 1
     return newMatrix


# rotates a one-dimensional matrix one position to the left
# the item in the first position assumes the last position
def rotateLeft1D(matrix):
     newMatrix = [0] * len(matrix) #initialize the new matrix
     i = 0
     while i < len(matrix):
          if i == 0:
               newMatrix[-1] = matrix[i]
          else:
               newMatrix[i - 1] = matrix[i]
          i += 1
     return newMatrix
     

# flips a rectangular tow-dimensional list horizontally
def flipH(matrix):
     



def main():
     # one dimensional rotations
     matrix1 = [1,6,3,4,5]
     print(rotateRight1D(matrix1))
     print(rotateLeft1D(matrix1))

     # two dimensional flips
     matrix2 = [[1,2,3,4,],
                [5,6,7,8]]

     

main()
     
