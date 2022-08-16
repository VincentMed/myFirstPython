# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

print('Hello AVC')

# a plot below
# hourly starting at 0700

temp = [67, 70, 81, 88, 90, 95, 102, 104, 102, 94, 93,]
nTemps = len(temp)
print('number of temps {}'.format(nTemps))



xAxis = np.linspace(7,17,nTemps )

#print(xAxis)

plt.plot(xAxis, temp)