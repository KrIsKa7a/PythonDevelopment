sec1 = int(input())
sec2 = int(input())
sec3 = int(input())

summed = sec1 + sec2 + sec3

minutes = summed // 60
seconds = summed - (minutes * 60)

print("{0}:{1:02d}".format(minutes, seconds))

