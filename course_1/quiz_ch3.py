# robotics_coursera_course1_week3_quiz3

import numpy as np
from numpy.linalg import matrix_power
import modern_robotics as mr

# Question 3
R_sa = [[0,1,0],
        [0,0,1],
        [1,0,0]]

R_as = np.transpose(R_sa)

R_sb = [[1,0,0],
       [0,0,1],
       [0,-1,0]]

R_ab = np.dot(R_as,R_sb)

print('\n')
print('Question 3 Info: \n')
print('R_as =')
print(R_as)
print('\n')
print('R_ab =')
print(R_ab)
print('\n')

# Question 4
R1 = np.dot(R_sa,R_sb)
print('Question 4 Info: \n')
print('R1 = ')
print(R1)
print('\n')

# Question 5
p_b = [[1],
       [2],
       [3]]
p_s = np.dot(R_sb,p_b)
print('Question 5: Convert p_b vector to p_s \n')
print('p_s = ')
print(p_s)
print('\n')

# Question 6
print('Question 6: Convert angular velocity vector w from s to a \n')
print('reference frame.\n')
w_s = [[3],
       [2],
       [1]]

w_a = np.dot(R_as,w_s)
print('w_a = ')
print(w_a)
print('\n')

# Question 9
w_theta = [[1],[2],[0]]
theta = np.sqrt(5)
w_hat = np.dot(1/theta,w_theta)
w_hat_skew = [[0,0,2/np.sqrt(5)],
              [0,0,-1/np.sqrt(5)],
              [-2/np.sqrt(5),1/np.sqrt(5),0]]

# Rodrigues formula
# splitting forumula into terms
print('Question 9: Calculate the matrix exponential\n')
term1 = np.identity(3)
term2 = np.dot(np.sin(theta),w_hat_skew)
term3_a = (1-np.cos(np.sqrt(5)))
term3_b = matrix_power(w_hat_skew,2)
term3 = np.dot(term3_a,term3_b)
R = term1 + term2 + term3
print('R =')
print(R)
print('\n')

# Question 10
print('Question 10: Create skew symmetric matrix using vector w.\n')
# np.array([1, 2, 3])
w = np.array([[1],[2],[0.5]])
w_skew = mr.VecToso3(w)
print('w_skew = ')
print(w_skew)
print('\n')

# Question 11
print('Question 11: Calculate rotation matrix using matrix exponential\n')
w_hat_theta = np.array([[0,0.5,-1],
                        [-0.5,0,2],
                        [1,-2,0]])
R = mr.MatrixExp3(w_hat_theta)
print('R =')
print(R)
print('\n')

# Question 12
print('Question 12: Calculate matrix logarithm given matrix exponential\n')
R = np.array([[0,0,1],
              [-1,0,0],
              [0,-1,0]])

w_hat_theta = mr.MatrixLog3(R)
print('w_hat_theta = ')
print(w_hat_theta)
print('\n')