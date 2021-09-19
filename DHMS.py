
import time

T= int(input("Please Enter the time in seconds \n "))

D= T // (24 * 3600)

T= T %  (24 * 3600)

H= T // 3600

T %= 3600

M= T // 60

S= T

print("Days: Hours: Minutes: Seconds: \n  %d:%d:%d:%d  " % (D, H, M, S))
