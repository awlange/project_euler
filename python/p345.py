import time

"""
We define the Matrix Sum of a matrix as the maximum sum of matrix elements with each element being the only one in his row and column. For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

   7    53   183   439  [863]
 497  [383]  563    79   973
 287    63  [343]  169   583
 627   343   773  [959]  943
[767]  473   103   699   303
Find the Matrix Sum of:

  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
"""

matrix = [
  [  7,  53, 183, 439, 863],
  [497, 383, 563,  79, 973],
  [287,  63, 343, 169, 583],
  [627, 343, 773, 959, 943],
  [767, 473, 103, 699, 303]
]

max_x = 0
picks = []

def compute_exclusive_matrix_maximum(rows_picked, cols_picked, N):
  m = 0
  for r in range(N):
    if r not in rows_picked:
      for c in range(N):
        if c not in cols_picked:
          if m < matrix[r][c]:
            m = matrix[r][c]
  return m


def compute2(rows_picked, cols_picked, x, N):
  """
  Pick element which maximizes the sub-matrix's maximum
  In case of tie for sub-matrix max, pick the max element value
  """
  global max_x
  global picks
  if len(rows_picked) == N or len(cols_picked) == N:
    if x > max_x:
      max_x = x
      picks = [matrix[rows_picked[n]][cols_picked[n]] for n in range(N)]
    return

  element_r = 0
  element_c = 0
  element_val = 0
  sub_matrix_maximum = 0
  for r in range(N):
    if r not in rows_picked:
      for c in range(N):
        if c not in cols_picked:
          rows_picked.append(r)
          cols_picked.append(c)        
          m = compute_exclusive_matrix_maximum(rows_picked, cols_picked, N)
          rows_picked.pop()
          cols_picked.pop()
          #print("zzz: ", matrix[r][c], m)
          if m >= sub_matrix_maximum and matrix[r][c] > element_val:
            element_r = r
            element_c = c
            element_val = matrix[r][c]
            sub_matrix_maximum = m
   
  print(element_val, sub_matrix_maximum)
  
  # recurse
  rows_picked.append(element_r)
  cols_picked.append(element_c)        
  compute2(rows_picked, cols_picked, x, N) 
  


def compute(rows_picked, cols_picked, x, N):
  global max_x
  global picks
  if len(rows_picked) == N or len(cols_picked) == N:
    if x > max_x:
      max_x = x
      picks = [matrix[rows_picked[n]][cols_picked[n]] for n in range(N)]
    return

  for r in range(N):
    if r not in rows_picked:
      for c in range(N):
        if c not in cols_picked:
           new_rows_picked = [i for i in rows_picked]
           new_cols_picked = [i for i in cols_picked]
           new_rows_picked.append(r)
           new_cols_picked.append(c)
           compute(new_rows_picked, new_cols_picked, x + matrix[r][c], N)


def main():
  ts = time.time()

  rows_picked = []
  cols_picked = []

  #compute(rows_picked, cols_picked, 0, 3)
  compute2(rows_picked, cols_picked, 0, 5)
  print(max_x)
  print(picks)

  print(time.time() - ts)

if __name__ == '__main__':
  main()
