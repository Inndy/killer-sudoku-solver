from z3 import Int, Solver

solver = Solver()

board = [ Int('b%d' % i) for i in range(81) ]

def AllDifferent(*cells):
    for i in cells:
        for j in cells:
            if i is not j:
                solver.add(i != j)
    return True

# Basic Sudoku constraints
solver.add(board[0] >= 1)
solver.add(board[0] <= 9)
solver.add(board[1] >= 1)
solver.add(board[1] <= 9)
solver.add(board[2] >= 1)
solver.add(board[2] <= 9)
solver.add(board[3] >= 1)
solver.add(board[3] <= 9)
solver.add(board[4] >= 1)
solver.add(board[4] <= 9)
solver.add(board[5] >= 1)
solver.add(board[5] <= 9)
solver.add(board[6] >= 1)
solver.add(board[6] <= 9)
solver.add(board[7] >= 1)
solver.add(board[7] <= 9)
solver.add(board[8] >= 1)
solver.add(board[8] <= 9)
solver.add(board[9] >= 1)
solver.add(board[9] <= 9)
solver.add(board[10] >= 1)
solver.add(board[10] <= 9)
solver.add(board[11] >= 1)
solver.add(board[11] <= 9)
solver.add(board[12] >= 1)
solver.add(board[12] <= 9)
solver.add(board[13] >= 1)
solver.add(board[13] <= 9)
solver.add(board[14] >= 1)
solver.add(board[14] <= 9)
solver.add(board[15] >= 1)
solver.add(board[15] <= 9)
solver.add(board[16] >= 1)
solver.add(board[16] <= 9)
solver.add(board[17] >= 1)
solver.add(board[17] <= 9)
solver.add(board[18] >= 1)
solver.add(board[18] <= 9)
solver.add(board[19] >= 1)
solver.add(board[19] <= 9)
solver.add(board[20] >= 1)
solver.add(board[20] <= 9)
solver.add(board[21] >= 1)
solver.add(board[21] <= 9)
solver.add(board[22] >= 1)
solver.add(board[22] <= 9)
solver.add(board[23] >= 1)
solver.add(board[23] <= 9)
solver.add(board[24] >= 1)
solver.add(board[24] <= 9)
solver.add(board[25] >= 1)
solver.add(board[25] <= 9)
solver.add(board[26] >= 1)
solver.add(board[26] <= 9)
solver.add(board[27] >= 1)
solver.add(board[27] <= 9)
solver.add(board[28] >= 1)
solver.add(board[28] <= 9)
solver.add(board[29] >= 1)
solver.add(board[29] <= 9)
solver.add(board[30] >= 1)
solver.add(board[30] <= 9)
solver.add(board[31] >= 1)
solver.add(board[31] <= 9)
solver.add(board[32] >= 1)
solver.add(board[32] <= 9)
solver.add(board[33] >= 1)
solver.add(board[33] <= 9)
solver.add(board[34] >= 1)
solver.add(board[34] <= 9)
solver.add(board[35] >= 1)
solver.add(board[35] <= 9)
solver.add(board[36] >= 1)
solver.add(board[36] <= 9)
solver.add(board[37] >= 1)
solver.add(board[37] <= 9)
solver.add(board[38] >= 1)
solver.add(board[38] <= 9)
solver.add(board[39] >= 1)
solver.add(board[39] <= 9)
solver.add(board[40] >= 1)
solver.add(board[40] <= 9)
solver.add(board[41] >= 1)
solver.add(board[41] <= 9)
solver.add(board[42] >= 1)
solver.add(board[42] <= 9)
solver.add(board[43] >= 1)
solver.add(board[43] <= 9)
solver.add(board[44] >= 1)
solver.add(board[44] <= 9)
solver.add(board[45] >= 1)
solver.add(board[45] <= 9)
solver.add(board[46] >= 1)
solver.add(board[46] <= 9)
solver.add(board[47] >= 1)
solver.add(board[47] <= 9)
solver.add(board[48] >= 1)
solver.add(board[48] <= 9)
solver.add(board[49] >= 1)
solver.add(board[49] <= 9)
solver.add(board[50] >= 1)
solver.add(board[50] <= 9)
solver.add(board[51] >= 1)
solver.add(board[51] <= 9)
solver.add(board[52] >= 1)
solver.add(board[52] <= 9)
solver.add(board[53] >= 1)
solver.add(board[53] <= 9)
solver.add(board[54] >= 1)
solver.add(board[54] <= 9)
solver.add(board[55] >= 1)
solver.add(board[55] <= 9)
solver.add(board[56] >= 1)
solver.add(board[56] <= 9)
solver.add(board[57] >= 1)
solver.add(board[57] <= 9)
solver.add(board[58] >= 1)
solver.add(board[58] <= 9)
solver.add(board[59] >= 1)
solver.add(board[59] <= 9)
solver.add(board[60] >= 1)
solver.add(board[60] <= 9)
solver.add(board[61] >= 1)
solver.add(board[61] <= 9)
solver.add(board[62] >= 1)
solver.add(board[62] <= 9)
solver.add(board[63] >= 1)
solver.add(board[63] <= 9)
solver.add(board[64] >= 1)
solver.add(board[64] <= 9)
solver.add(board[65] >= 1)
solver.add(board[65] <= 9)
solver.add(board[66] >= 1)
solver.add(board[66] <= 9)
solver.add(board[67] >= 1)
solver.add(board[67] <= 9)
solver.add(board[68] >= 1)
solver.add(board[68] <= 9)
solver.add(board[69] >= 1)
solver.add(board[69] <= 9)
solver.add(board[70] >= 1)
solver.add(board[70] <= 9)
solver.add(board[71] >= 1)
solver.add(board[71] <= 9)
solver.add(board[72] >= 1)
solver.add(board[72] <= 9)
solver.add(board[73] >= 1)
solver.add(board[73] <= 9)
solver.add(board[74] >= 1)
solver.add(board[74] <= 9)
solver.add(board[75] >= 1)
solver.add(board[75] <= 9)
solver.add(board[76] >= 1)
solver.add(board[76] <= 9)
solver.add(board[77] >= 1)
solver.add(board[77] <= 9)
solver.add(board[78] >= 1)
solver.add(board[78] <= 9)
solver.add(board[79] >= 1)
solver.add(board[79] <= 9)
solver.add(board[80] >= 1)
solver.add(board[80] <= 9)
solver.add(AllDifferent(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
solver.add(AllDifferent(board[9], board[10], board[11], board[12], board[13], board[14], board[15], board[16], board[17]))
solver.add(AllDifferent(board[18], board[19], board[20], board[21], board[22], board[23], board[24], board[25], board[26]))
solver.add(AllDifferent(board[27], board[28], board[29], board[30], board[31], board[32], board[33], board[34], board[35]))
solver.add(AllDifferent(board[36], board[37], board[38], board[39], board[40], board[41], board[42], board[43], board[44]))
solver.add(AllDifferent(board[45], board[46], board[47], board[48], board[49], board[50], board[51], board[52], board[53]))
solver.add(AllDifferent(board[54], board[55], board[56], board[57], board[58], board[59], board[60], board[61], board[62]))
solver.add(AllDifferent(board[63], board[64], board[65], board[66], board[67], board[68], board[69], board[70], board[71]))
solver.add(AllDifferent(board[72], board[73], board[74], board[75], board[76], board[77], board[78], board[79], board[80]))
solver.add(AllDifferent(board[0], board[9], board[18], board[27], board[36], board[45], board[54], board[63], board[72]))
solver.add(AllDifferent(board[1], board[10], board[19], board[28], board[37], board[46], board[55], board[64], board[73]))
solver.add(AllDifferent(board[2], board[11], board[20], board[29], board[38], board[47], board[56], board[65], board[74]))
solver.add(AllDifferent(board[3], board[12], board[21], board[30], board[39], board[48], board[57], board[66], board[75]))
solver.add(AllDifferent(board[4], board[13], board[22], board[31], board[40], board[49], board[58], board[67], board[76]))
solver.add(AllDifferent(board[5], board[14], board[23], board[32], board[41], board[50], board[59], board[68], board[77]))
solver.add(AllDifferent(board[6], board[15], board[24], board[33], board[42], board[51], board[60], board[69], board[78]))
solver.add(AllDifferent(board[7], board[16], board[25], board[34], board[43], board[52], board[61], board[70], board[79]))
solver.add(AllDifferent(board[8], board[17], board[26], board[35], board[44], board[53], board[62], board[71], board[80]))
solver.add(AllDifferent(board[0], board[1], board[2], board[9], board[10], board[11], board[18], board[19], board[20]))
solver.add(AllDifferent(board[3], board[4], board[5], board[12], board[13], board[14], board[21], board[22], board[23]))
solver.add(AllDifferent(board[6], board[7], board[8], board[15], board[16], board[17], board[24], board[25], board[26]))
solver.add(AllDifferent(board[27], board[28], board[29], board[36], board[37], board[38], board[45], board[46], board[47]))
solver.add(AllDifferent(board[30], board[31], board[32], board[39], board[40], board[41], board[48], board[49], board[50]))
solver.add(AllDifferent(board[33], board[34], board[35], board[42], board[43], board[44], board[51], board[52], board[53]))
solver.add(AllDifferent(board[54], board[55], board[56], board[63], board[64], board[65], board[72], board[73], board[74]))
solver.add(AllDifferent(board[57], board[58], board[59], board[66], board[67], board[68], board[75], board[76], board[77]))
solver.add(AllDifferent(board[60], board[61], board[62], board[69], board[70], board[71], board[78], board[79], board[80]))

# Killer cage constraints
solver.add(board[0]+board[1]+board[2] == 15)
solver.add(board[3]+board[12]+board[13] == 14)
solver.add(board[4] == 4)
solver.add(board[5]+board[14] == 10)
solver.add(board[7]+board[8] == 13)
solver.add(board[16] == 9)
solver.add(board[17]+board[26]+board[25] == 9)
solver.add(board[23]+board[32] == 12)
solver.add(board[6]+board[15]+board[24]+board[33] == 21)
solver.add(board[35]+board[34]+board[43] == 14)
solver.add(board[44]+board[53]+board[62] == 15)
solver.add(board[71]+board[80] == 7)
solver.add(board[79]+board[78] == 9)
solver.add(board[70]+board[69]+board[68] == 20)
solver.add(board[75]+board[76]+board[77] == 14)
solver.add(board[72]+board[74]+board[73]+board[45]+board[54]+board[63] == 33)
solver.add(board[27]+board[36] == 6)
solver.add(board[9]+board[18] == 10)
solver.add(board[10]+board[19] == 10)
solver.add(board[11]+board[20] == 10)
solver.add(board[28]+board[29] == 5)
solver.add(board[37]+board[46] == 15)
solver.add(board[56]+board[55]+board[64]+board[65] == 19)
solver.add(board[21]+board[22]+board[31] == 18)
solver.add(board[30]+board[39] == 13)
solver.add(board[66]+board[67] == 11)
solver.add(board[57]+board[58]+board[49] == 12)
solver.add(board[40]+board[41]+board[42]+board[50] == 22)
solver.add(board[59]+board[60]+board[51] == 13)
solver.add(board[52]+board[61] == 8)
solver.add(board[38]+board[48]+board[47] == 14)

print(solver.check())
m = solver.model()
for i, b in enumerate(board):
    print(m[b],end='\n' if i % 9 == 8 else '')
