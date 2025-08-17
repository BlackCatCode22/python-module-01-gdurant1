hours= float(input('Hours worked?'))
rate= float(input('Rate worked?'))
if (hours<=40):
    print('Pay:', hours*rate)
else:
    print('Pay:', (40*rate)+((hours-40)*(rate*1.5)))