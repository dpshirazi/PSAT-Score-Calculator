# -*- coding: utf-8 -*-
"""pSat Score Calculator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aWJujKmtJTWbKpK5raW0PJTfEkDjU4va
"""

print('Hello This Pogram will tell you What your pSat Score will look like, All you have to do is insert your Raw score for the Raw score of the Reading and the math. ')
ReadingScore=int(input('Insert Reading Comp. Raw  Score:   '))
WritingScore=int(input('Insert Writing Language Raw Score:  '))
MathNoCalc=int(input('Insert Math-No calc-Raw score:   '))
MathCalc=int(input('Insert Math-Calc-Raw Score:  '))

# xReading is the Reading Comprenhension score, while the Reading Score is the Raw Reading comprehension score

if(ReadingScore>=0 and ReadingScore<=4):
  xReadingScore=ReadingScore+8
elif(ReadingScore>=5 and ReadingScore<=7):
  xReadingScore=ReadingScore+9
elif(ReadingScore>=8 and ReadingScore<=9):
  xReadingScore=8+ReadingScore
elif(ReadingScore>=10 and ReadingScore<=11):
  xReadingScore=18
elif(ReadingScore>=12 and ReadingScore<=13):
  xReadingScore=19
elif(ReadingScore>=14 and ReadingScore<=15):
  xReadingScore=20
elif(ReadingScore>=16 and ReadingScore<=17):
  xReadingScore=21
elif(ReadingScore>=18 and ReadingScore<=19):
  xReadingScore=22
elif(ReadingScore>=20 and ReadingScore<=21):
  xReadingScore=23
elif(ReadingScore>=22 and ReadingScore<=23):
  xReadingScore=24
elif(ReadingScore==24):
  xReadingScore=25
elif(ReadingScore>=25 and ReadingScore<=26):
  xReadingScore=26
elif(ReadingScore>=27 and ReadingScore<=28):
  xReadingScore=27
elif(ReadingScore>=29 and ReadingScore<=30):
  xReadingScore=28
elif(ReadingScore>=31 and ReadingScore<=32):
  xReadingScore=29
elif(ReadingScore>=33 and ReadingScore<=34):
  xReadingScore=30
elif(ReadingScore>=35 and ReadingScore<=36):
  xReadingScore=31
elif(ReadingScore>=37 and ReadingScore<=38):
  xReadingScore=32
elif(ReadingScore==39):
  xReadingScore=33
elif(ReadingScore>=40 and ReadingScore<=41):
  xReadingScore=34
elif(ReadingScore==42):
  xReadingScore=35
elif(ReadingScore==43):
  xReadingScore=36
elif(ReadingScore>=44 and ReadingScore<=45):
  xReadingScore=37
elif(ReadingScore>=46 and ReadingScore<=47):
  xReadingScore=38
else:
  print(' There is no such Raw Score for the reading comprehension as the one you put in, please check your score again.')
#xWriting is the score for the writing section of the pSat


if(WritingScore>=0 and WritingScore<=5):
  xWriting=WritingScore+8
elif(WritingScore>=6 and WritingScore<=7):
  xWriting=14
elif(WritingScore>=8 and WritingScore<=9):
  xWriting=15
elif(WritingScore>=10 and WritingScore<=11):
  xWriting=16
elif(WritingScore==12):
  xWriting=17
elif(WritingScore>=13 and WritingScore<=14):
  xWriting=18
elif(WritingScore==15):
  xWriting=19
elif(WritingScore>=16 and WritingScore<=17):
  xWriting=20
elif(WritingScore>=18 and WritingScore<=19):
  xWriting=21
elif(WritingScore==20):
  xWriting=22
elif(WritingScore==21):
  xWriting=23
elif(WritingScore>=22 and WritingScore<=23):
  xWriting=24
elif(WritingScore>=24 and WritingScore<=25):
  xWriting=25
elif(WritingScore==26):
  xWriting=26
elif(WritingScore>=27 and WritingScore<=28):
  xWriting=27
elif(WritingScore>=29 and WritingScore<=30):
  xWriting=28
elif(WritingScore>=31 and WritingScore<=32):
  xWriting=29
elif(WritingScore>=33 and WritingScore<=34):
  xWriting=30
elif(WritingScore==35):
  xWriting=31
elif(WritingScore>=36 and WritingScore<=37):
  xWriting=32
elif(WritingScore==38):
  xWriting=33
elif(WritingScore==39):
  xWriting=34
elif(WritingScore==40):
  xWriting=35
elif(WritingScore==41):
  xWriting=36
elif(WritingScore>=42 and WritingScore<=43):
  xWriting=37
elif(WritingScore==44):
  xWriting=38
else:
  print('Your Raw Writing Score is not a actual score, please check and re-run the program. ')

tMath=MathNoCalc + MathCalc
if(tMath>=0 and tMath<=1):
  xMath=160+30*tMath
elif(tMath==2):
  xMath=210
elif(tMath>=3 and tMath<=4):
  xMath=210+30*(tMath-2)
elif(tMath==5):
  xMath=290
elif(tMath==6):
  xMath=320
elif(tMath==7):
  xMath=340
elif(tMath==8):
  xMath=360
elif(tMath==9):
  xMath=370
elif(tMath==10):
  xMath=390
elif(tMath==11):
  xMath=400
elif(tMath==12):
  xMath=420
elif(tMath==13):
  xMath=430
elif(tMath==14):
  xMath=440
elif(tMath==15):
  xMath=460
elif(tMath==16):
  xMath=470
elif(tMath==17):
  xMath=480
elif(tMath==18):
  xMath=490
elif(tMath>=19 and tMath<=27):
  xMath=500+10*(tMath-19)
elif(tMath>=28 and tMath<=35):
  xMath=580+10*(tMath-28)
elif(tMath>=36 and tMath<=38):
  xMath=670+10*(tMath-36)
elif(tMath==39):
  xMath=710
elif(tMath==40):
  xMath=720
elif(tMath==41):
  xMath=730
elif(tMath==42):
  xMath=730
elif(tMath==43):
  xMath=740
elif(tMath==44):
  xMath=740
elif(tMath>=45 and tMath<=46):
  xMath=750
elif(tMath>=47 and tMath<=48):
  xMath=760
else:
  print('You have not entered a right Math score.')

zWriting=xReadingScore + xWriting
tWriting=10*zWriting
TotalScore = tWriting + xMath
print('Your Math sub-score was a  ' + str(xMath)+'.')
print('Your Reading and writing subscore was a '+ str(tWriting)+'.')
print('You got a '+ str(TotalScore) +' on the Psat, Congrats!')