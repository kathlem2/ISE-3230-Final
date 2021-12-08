# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 01:26:31 2021

@author: macle
"""

import cvxpy as cp

#instantiate variables
green  =  [ [ [] for col in range(9) ] for row in range(9)]
for row in range(9):
    for col in range(9):
            green[row][col]= cp.Variable(9, boolean = True)
red  =  [ [ [] for col in range(9) ] for row in range(9)]
for row in range(9):
    for col in range(9):
            red[row][col]= cp.Variable(9, boolean = True)

yellow  =  [ [ [] for col in range(9) ] for row in range(9)]
for row in range(9):
    for col in range(9):
            yellow[row][col]= cp.Variable(9, boolean = True)

blue  =  [ [ [] for col in range(9) ] for row in range(9)]
for row in range(9):
    for col in range(9):
            blue[row][col]= cp.Variable(9, boolean = True)
            
pink  =  [ [ [] for col in range(9) ] for row in range(9)]
for row in range(9):
    for col in range(9):
            pink[row][col]= cp.Variable(9, boolean = True)

obj_func = 0*green[0][0][0]
            
constraints = []

#Each Box has only one value
for row in range(9):
    for col in range(9):
        constraints.append(cp.sum(green[row][col][:9])==1)
        constraints.append(cp.sum(red[row][col][:9])==1)
        constraints.append(cp.sum(yellow[row][col][:9])==1)
        constraints.append(cp.sum(blue[row][col][:9])==1)
        constraints.append(cp.sum(pink[row][col][:9])==1)

#Each Row has a unique 1-9        
row_sum_g, row_sum_r, row_sum_y, row_sum_b, row_sum_p = 0, 0, 0, 0, 0 
for val in range(9):
    for row in range(9):
        for col in range(9):
            row_sum_g += green[row][col][val]
            row_sum_r += red[row][col][val]
            row_sum_y += yellow[row][col][val]
            row_sum_b += blue[row][col][val]
            row_sum_p += pink[row][col][val]
        constraints.append(row_sum_g==1)
        constraints.append(row_sum_r==1)
        constraints.append(row_sum_y==1)
        constraints.append(row_sum_b==1)
        constraints.append(row_sum_p==1)
        row_sum_g, row_sum_r, row_sum_y, row_sum_b, row_sum_p = 0, 0, 0, 0, 0 

#Each Column has a unique 1-9        
col_sum_g, col_sum_r, col_sum_y, col_sum_b, col_sum_p = 0, 0, 0, 0, 0 
for val in range(9):
    for col in range(9):
        for row in range(9):
            col_sum_g += green[row][col][val]
            col_sum_r += red[row][col][val]
            col_sum_y += yellow[row][col][val]
            col_sum_b += blue[row][col][val]
            col_sum_p += pink[row][col][val]
        constraints.append(col_sum_g==1)
        constraints.append(col_sum_r==1)
        constraints.append(col_sum_y==1)
        constraints.append(col_sum_b==1)
        constraints.append(col_sum_p==1)
        col_sum_g, col_sum_r, col_sum_y, col_sum_b, col_sum_p = 0, 0, 0, 0, 0 

#Each InnerBox has a unique 1-9
val_sum1_g, val_sum2_g, val_sum3_g, val_sum4_g, val_sum5_g, val_sum6_g, val_sum7_g, val_sum8_g, val_sum9_g = 0, 0, 0, 0, 0, 0, 0, 0, 0
val_sum1_r, val_sum2_r, val_sum3_r, val_sum4_r, val_sum5_r, val_sum6_r, val_sum7_r, val_sum8_r, val_sum9_r = 0, 0, 0, 0, 0, 0, 0, 0, 0
val_sum1_y, val_sum2_y, val_sum3_y, val_sum4_y, val_sum5_y, val_sum6_y, val_sum7_y, val_sum8_y, val_sum9_y = 0, 0, 0, 0, 0, 0, 0, 0, 0
val_sum1_b, val_sum2_b, val_sum3_b, val_sum4_b, val_sum5_b, val_sum6_b, val_sum7_b, val_sum8_b, val_sum9_b = 0, 0, 0, 0, 0, 0, 0, 0, 0
val_sum1_p, val_sum2_p, val_sum3_p, val_sum4_p, val_sum5_p, val_sum6_p, val_sum7_p, val_sum8_p, val_sum9_p = 0, 0, 0, 0, 0, 0, 0, 0, 0
for val in range(9):
    for i in range(3):
        for j in range(3):
            val_sum1_g += green[i][j][val]
            val_sum2_g += green[i][j+3][val]
            val_sum3_g += green[i][j+6][val]
            val_sum4_g += green[i+3][j][val]
            val_sum5_g += green[i+3][j+3][val]
            val_sum6_g += green[i+3][j+6][val]
            val_sum7_g += green[i+6][j][val]
            val_sum8_g += green[i+6][j+3][val]
            val_sum9_g += green[i+6][j+6][val]
            val_sum1_r += red[i][j][val]
            val_sum2_r += red[i][j+3][val]
            val_sum3_r += red[i][j+6][val]
            val_sum4_r += red[i+3][j][val]
            val_sum5_r += red[i+3][j+3][val]
            val_sum6_r += red[i+3][j+6][val]
            val_sum7_r += red[i+6][j][val]
            val_sum8_r += red[i+6][j+3][val]
            val_sum9_r += red[i+6][j+6][val]
            val_sum1_y += yellow[i][j][val]
            val_sum2_y += yellow[i][j+3][val]
            val_sum3_y += yellow[i][j+6][val]
            val_sum4_y += yellow[i+3][j][val]
            val_sum5_y += yellow[i+3][j+3][val]
            val_sum6_y += yellow[i+3][j+6][val]
            val_sum7_y += yellow[i+6][j][val]
            val_sum8_y += yellow[i+6][j+3][val]
            val_sum9_y += yellow[i+6][j+6][val]
            val_sum1_b += blue[i][j][val]
            val_sum2_b += blue[i][j+3][val]
            val_sum3_b += blue[i][j+6][val]
            val_sum4_b += blue[i+3][j][val]
            val_sum5_b += blue[i+3][j+3][val]
            val_sum6_b += blue[i+3][j+6][val]
            val_sum7_b += blue[i+6][j][val]
            val_sum8_b += blue[i+6][j+3][val]
            val_sum9_b += blue[i+6][j+6][val]
            val_sum1_p += pink[i][j][val]
            val_sum2_p += pink[i][j+3][val]
            val_sum3_p += pink[i][j+6][val]
            val_sum4_p += pink[i+3][j][val]
            val_sum5_p += pink[i+3][j+3][val]
            val_sum6_p += pink[i+3][j+6][val]
            val_sum7_p += pink[i+6][j][val]
            val_sum8_p += pink[i+6][j+3][val]
            val_sum9_p += pink[i+6][j+6][val]
    constraints.append(val_sum1_g==1)
    constraints.append(val_sum2_g==1)
    constraints.append(val_sum3_g==1)
    constraints.append(val_sum4_g==1)
    constraints.append(val_sum5_g==1)
    constraints.append(val_sum6_g==1)
    constraints.append(val_sum7_g==1)
    constraints.append(val_sum8_g==1)
    constraints.append(val_sum9_g==1)
    constraints.append(val_sum1_r==1)
    constraints.append(val_sum2_r==1)
    constraints.append(val_sum3_r==1)
    constraints.append(val_sum4_r==1)
    constraints.append(val_sum5_r==1)
    constraints.append(val_sum6_r==1)
    constraints.append(val_sum7_r==1)
    constraints.append(val_sum8_r==1)
    constraints.append(val_sum9_r==1)
    constraints.append(val_sum1_y==1)
    constraints.append(val_sum2_y==1)
    constraints.append(val_sum3_y==1)
    constraints.append(val_sum4_y==1)
    constraints.append(val_sum5_y==1)
    constraints.append(val_sum6_y==1)
    constraints.append(val_sum7_y==1)
    constraints.append(val_sum8_y==1)
    constraints.append(val_sum9_y==1)
    constraints.append(val_sum1_b==1)
    constraints.append(val_sum2_b==1)
    constraints.append(val_sum3_b==1)
    constraints.append(val_sum4_b==1)
    constraints.append(val_sum5_b==1)
    constraints.append(val_sum6_b==1)
    constraints.append(val_sum7_b==1)
    constraints.append(val_sum8_b==1)
    constraints.append(val_sum9_b==1)
    constraints.append(val_sum1_p==1)
    constraints.append(val_sum2_p==1)
    constraints.append(val_sum3_p==1)
    constraints.append(val_sum4_p==1)
    constraints.append(val_sum5_p==1)
    constraints.append(val_sum6_p==1)
    constraints.append(val_sum7_p==1)
    constraints.append(val_sum8_p==1)
    constraints.append(val_sum9_p==1)
    val_sum1_g, val_sum2_g, val_sum3_g, val_sum4_g, val_sum5_g, val_sum6_g, val_sum7_g, val_sum8_g, val_sum9_g = 0, 0, 0, 0, 0, 0, 0, 0, 0
    val_sum1_r, val_sum2_r, val_sum3_r, val_sum4_r, val_sum5_r, val_sum6_r, val_sum7_r, val_sum8_r, val_sum9_r = 0, 0, 0, 0, 0, 0, 0, 0, 0
    val_sum1_y, val_sum2_y, val_sum3_y, val_sum4_y, val_sum5_y, val_sum6_y, val_sum7_y, val_sum8_y, val_sum9_y = 0, 0, 0, 0, 0, 0, 0, 0, 0
    val_sum1_b, val_sum2_b, val_sum3_b, val_sum4_b, val_sum5_b, val_sum6_b, val_sum7_b, val_sum8_b, val_sum9_b = 0, 0, 0, 0, 0, 0, 0, 0, 0
    val_sum1_p, val_sum2_p, val_sum3_p, val_sum4_p, val_sum5_p, val_sum6_p, val_sum7_p, val_sum8_p, val_sum9_p = 0, 0, 0, 0, 0, 0, 0, 0, 0

# Overlap 
for val in range(9):
    for i in range(3):
        for j in range(3):
            constraints.append(green[6+i][6+j][val]-yellow[i][j][val]==0)
            constraints.append(red[6+i][j][val]-yellow[i][j+6][val]==0)
            constraints.append(blue[i][6+j][val]-yellow[i+6][j][val]==0)
            constraints.append(pink[i][j][val]-yellow[i+6][j+6][val]==0)
    
#Given Variables
constraints.append(green[0][1][1]==1)
constraints.append(green[0][7][6]==1)
constraints.append(green[1][0][7]==1)
constraints.append(green[1][1][5]==1)
constraints.append(green[1][2][2]==1)
constraints.append(green[1][3][1]==1)
constraints.append(green[1][4][3]==1)
constraints.append(green[1][7][8]==1)
constraints.append(green[1][8][0]==1)
constraints.append(green[2][1][4]==1)
constraints.append(green[2][4][0]==1)
constraints.append(green[3][1][6]==1)
constraints.append(green[3][4][2]==1)
constraints.append(green[4][1][3]==1)
constraints.append(green[4][2][0]==1)
constraints.append(green[4][3][6]==1)
constraints.append(green[4][4][7]==1)
constraints.append(green[4][5][8]==1)
constraints.append(green[4][6][2]==1)
constraints.append(green[4][7][1]==1)
constraints.append(green[5][4][4]==1)
constraints.append(green[5][7][3]==1)
constraints.append(green[6][4][6]==1)
constraints.append(green[6][7][7]==1)
constraints.append(green[7][0][3]==1)
constraints.append(green[7][1][2]==1)
constraints.append(green[7][4][5]==1)
constraints.append(green[7][5][7]==1)
constraints.append(green[7][6][8]==1)
constraints.append(green[7][7][4]==1)
constraints.append(green[7][8][1]==1)
constraints.append(green[8][1][7]==1)
constraints.append(green[8][7][5]==1)

constraints.append(red[0][1][7]==1)
constraints.append(red[0][7][6]==1)
constraints.append(red[1][0][5]==1)
constraints.append(red[1][1][2]==1)
constraints.append(red[1][4][3]==1)
constraints.append(red[1][5][7]==1)
constraints.append(red[1][6][1]==1)
constraints.append(red[1][7][4]==1)
constraints.append(red[1][8][0]==1)
constraints.append(red[2][4][4]==1)
constraints.append(red[2][7][5]==1)
constraints.append(red[3][4][6]==1)
constraints.append(red[3][7][7]==1)
constraints.append(red[4][1][4]==1)
constraints.append(red[4][2][2]==1)
constraints.append(red[4][3][3]==1)
constraints.append(red[4][4][0]==1)
constraints.append(red[4][5][5]==1)
constraints.append(red[4][6][6]==1)
constraints.append(red[4][7][8]==1)
constraints.append(red[5][1][0]==1)
constraints.append(red[5][4][1]==1)
constraints.append(red[6][1][1]==1)
constraints.append(red[6][4][7]==1)
constraints.append(red[7][0][0]==1)
constraints.append(red[7][1][5]==1)
constraints.append(red[7][2][3]==1)
constraints.append(red[7][3][2]==1)
constraints.append(red[7][4][8]==1)
constraints.append(red[7][7][1]==1)
constraints.append(red[7][8][7]==1)
constraints.append(red[8][1][8]==1)
constraints.append(red[8][7][0]==1)

constraints.append(yellow[0][1][7]==1)
constraints.append(yellow[0][7][1]==1)
constraints.append(yellow[1][0][8]==1)
constraints.append(yellow[1][1][4]==1)
constraints.append(yellow[1][2][1]==1)
constraints.append(yellow[1][6][0]==1)
constraints.append(yellow[1][7][5]==1)
constraints.append(yellow[1][8][3]==1)
constraints.append(yellow[2][1][5]==1)
constraints.append(yellow[2][4][1]==1)
constraints.append(yellow[2][7][8]==1)
constraints.append(yellow[3][3][0]==1)
constraints.append(yellow[3][5][6]==1)
constraints.append(yellow[4][2][7]==1)
constraints.append(yellow[4][6][6]==1)
constraints.append(yellow[5][3][8]==1)
constraints.append(yellow[5][5][2]==1)
constraints.append(yellow[6][1][1]==1)
constraints.append(yellow[6][4][2]==1)
constraints.append(yellow[6][7][3]==1)
constraints.append(yellow[7][0][4]==1)
constraints.append(yellow[7][1][2]==1)
constraints.append(yellow[7][2][3]==1)
constraints.append(yellow[7][6][8]==1)
constraints.append(yellow[7][7][6]==1)
constraints.append(yellow[7][8][5]==1)
constraints.append(yellow[8][1][0]==1)
constraints.append(yellow[8][7][4]==1)

constraints.append(blue[0][1][7]==1)
constraints.append(blue[0][7][1]==1)
constraints.append(blue[1][0][6]==1)
constraints.append(blue[1][1][0]==1)
constraints.append(blue[1][4][8]==1)
constraints.append(blue[1][5][1]==1)
constraints.append(blue[1][6][4]==1)
constraints.append(blue[1][7][2]==1)
constraints.append(blue[1][8][3]==1)
constraints.append(blue[2][4][2]==1)
constraints.append(blue[2][7][0]==1)
constraints.append(blue[3][4][7]==1)
constraints.append(blue[3][7][6]==1)
constraints.append(blue[4][1][8]==1)
constraints.append(blue[4][2][7]==1)
constraints.append(blue[4][3][3]==1)
constraints.append(blue[4][4][6]==1)
constraints.append(blue[4][5][4]==1)
constraints.append(blue[4][6][1]==1)
constraints.append(blue[4][7][5]==1)
constraints.append(blue[5][1][4]==1)
constraints.append(blue[5][4][0]==1)
constraints.append(blue[6][1][6]==1)
constraints.append(blue[6][4][1]==1)
constraints.append(blue[7][0][4]==1)
constraints.append(blue[7][1][1]==1)
constraints.append(blue[7][2][0]==1)
constraints.append(blue[7][3][2]==1)
constraints.append(blue[7][4][3]==1)
constraints.append(blue[7][7][7]==1)
constraints.append(blue[7][8][6]==1)
constraints.append(blue[8][1][2]==1)
constraints.append(blue[8][7][3]==1)

constraints.append(pink[0][1][3]==1)
constraints.append(pink[0][7][8]==1)
constraints.append(pink[1][0][8]==1)
constraints.append(pink[1][1][6]==1)
constraints.append(pink[1][2][5]==1)
constraints.append(pink[1][3][3]==1)
constraints.append(pink[1][4][7]==1)
constraints.append(pink[1][7][4]==1)
constraints.append(pink[1][8][2]==1)
constraints.append(pink[2][1][4]==1)
constraints.append(pink[2][4][6]==1)
constraints.append(pink[3][1][0]==1)
constraints.append(pink[3][4][1]==1)
constraints.append(pink[4][1][8]==1)
constraints.append(pink[4][2][3]==1)
constraints.append(pink[4][3][5]==1)
constraints.append(pink[4][4][2]==1)
constraints.append(pink[4][5][4]==1)
constraints.append(pink[4][6][1]==1)
constraints.append(pink[4][7][0]==1)
constraints.append(pink[5][4][3]==1)
constraints.append(pink[5][7][5]==1)
constraints.append(pink[6][4][0]==1)
constraints.append(pink[6][7][6]==1)
constraints.append(pink[7][0][0]==1)
constraints.append(pink[7][1][1]==1)
constraints.append(pink[7][4][8]==1)
constraints.append(pink[7][5][5]==1)
constraints.append(pink[7][6][2]==1)
constraints.append(pink[7][7][3]==1)
constraints.append(pink[7][8][4]==1)
constraints.append(pink[8][1][7]==1)
constraints.append(pink[8][7][1]==1)
          

problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)
#problem.solve()

print("obj_func =")
print(obj_func.value)
print("Green =")
for row in range(9):
    for col in range(9):
        for val in range(9):
            if green[row][col][val].value==1:
                print(val+1 , end =" ")
    print("")
print("Red =")
for row in range(9):
    for col in range(9):
        for val in range(9):
            if red[row][col][val].value==1:
                print(val+1 , end =" ")
    print("")
print("Yellow =")
for row in range(9):
    for col in range(9):
        for val in range(9):
            if yellow[row][col][val].value==1:
                print(val+1 , end =" ")
    print("")
print("Blue =")
for row in range(9):
    for col in range(9):
        for val in range(9):
            if blue[row][col][val].value==1:
                print(val+1 , end =" ")
    print("")
print("Pink =")
for row in range(9):
    for col in range(9):
        for val in range(9):
            if pink[row][col][val].value==1:
                print(val+1 , end =" ")
    print("")