#! /usr/bin/env python3

import sys
import pandas as pd

def main():
  # print(sys.version)

  params = ', '.join(sys.argv)
  print(params)

  # df = pd.read_csv('./data.csv', header=None)
  df = pd.read_excel('./data.xlsx', header=None)

  print(df)
  print(df[0][0])
  print(df[1][2])

  # df.to_excel('data.xlsx', index=False, header=False)

if __name__ == '__main__':
  main()
