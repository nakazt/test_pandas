#! /usr/bin/env python3

import sys
import pandas as pd

def main():
  # print(sys.version)

  params = ', '.join(sys.argv)
  print(params)

  # header=None, index_col=None
  #   特定の行、列をヘッダー、インデックスとしない(0からの連番)
  #   0〜 で特定の特定の行、列を指定
  df = pd.read_csv('./data.csv', header=None)
  # df = pd.read_excel('./data.xlsx', header=None)

  print(df)
  print(df[0][0])   # a1
  print(df[1][2])   # b3

  # index=False, columns=False
  #   index(行名)、columns(列名)を書き出さない
  #   df.to_excel('data.xlsx', index=False, header=False)

if __name__ == '__main__':
  main()
