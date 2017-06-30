

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
     

# flips a rectangular two-dimensional list horizontally
def flipH(matrix):
     newMatrix = []
     i = 0
     while i < len(matrix):
          newSubMatrix = []
          j = (len(matrix[i]) - 1)
          while j >= 0:
               newSubMatrix.append(matrix[i][j])
               j -= 1
          newMatrix.append(newSubMatrix)
          i += 1
     return newMatrix


# flips a rectangular two-dimensional list vertically
def flipV(matrix):
     newMatrix = []
     i = (len(matrix) - 1)
     while i >= 0:
          newSubMatrix = []
          j = 0
          while j < len(matrix[i]):
               newSubMatrix.append(matrix[i][j])
               j += 1
          newMatrix.append(newSubMatrix)
          i -= 1
     return newMatrix


# rotates a rectangular two-dimensional list to the right
def rotateRight(matrix):
     newMatrix = []
     numCols = len(matrix[0])
     i = 0
     while i < numCols:
          newSubMatrix = []
          j = (len(matrix) - 1)
          while j >= 0:
               k = 0
               while k < len(matrix[j]):
                    if k == i:
                         newSubMatrix.append(matrix[j][k])
                    k += 1
               j -= 1
          newMatrix.append(newSubMatrix)
          i += 1
     return newMatrix


# rotates a rectangular two-dimensional list to the left
def rotateLeft(matrix):
     newMatrix = []
     i = (len(matrix[0]) - 1)
     while i >= 0:
          newSubMatrix = []
          j = 0
          while j < len(matrix):
               k = 0
               while k < len(matrix[j]):
                    if k == i:
                         newSubMatrix.append(matrix[j][k])
                    k += 1
               j += 1
          newMatrix.append(newSubMatrix)
          i -= 1
     return newMatrix


# rotates a rectangular two-dimensional list 180 degrees
def rotate180(matrix):
     newMatrix = []
          
                   

def main():
     # one dimensional rotations
     matrix1 = [1,6,3,4,5]
     #print(rotateRight1D(matrix1))
     #print(rotateLeft1D(matrix1))

     # two dimensional flips
     matrix2 = [[1,2,3,4],
                [5,6,7,8]]
     matrix3 = [[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]]
     #print(flipH(matrix2))
     #print(flipV(matrix3))
     print(rotateLeft(matrix3))

     

main()
     
