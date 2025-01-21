#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

if bmi < 18.5:
  print('underweight')
elif bmi <= 24.99 and bmi >= 18.5:
  print('normal')
elif bmi <= 29.99 and bmi >= 25.0:
  print('overweight')
else:
  print('obese')
