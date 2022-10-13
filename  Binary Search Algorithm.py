{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Recursive Binary Search algorithm in Python\
\
def binarySearch(array, x, low, high):\
\
if high >= low:\
\
mid = low + (high - low)//2\
\
# If found at mid, return the value\
\
if array[mid] == x:\
\
return mid\
\
# Search the first half\
\
elif array[mid] > x:\
\
return binarySearch(array, x, low, mid-1)\
\
# Search the second half\
\
else:\
\
return binarySearch(array, x, mid + 1, high)\
\
else:\
\
return -1\
\
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\
\
x = int(input("Enter a number between 1 and 10:"))\
\
result = binarySearch(array, x, 0, len(array)-1)\
\
if result != -1:\
\
print("Element is present at position" + str(result))\
\
else:\
\
print("Element not found")}