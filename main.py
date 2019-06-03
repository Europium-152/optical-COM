import numpy as np


class Line:  # Line in cartesian coordinates y = m * x + b

    def __init__(self, a, b):
        self.m = (b[1] - a[1]) / (b[0] - a[0])
        self.b = a[1] - self.m * a[0]

    def intersect(self, other):

        x = (other.b - self.b) / (self.m - other.b)
        y = self.m * x + self.b

        return np.array([x, y])


# Signals from the tomography diagnostic (top and out cameras) --------------------------------
signals_top = np.arange(16)
signals_out = np.arange(16)

# Spacial positioning of the pinholes -----------------------------------------------------------

pinhole_x_top = 5.0
pinhole_y_top = 97.

pinhole_x_out = 109.
pinhole_y_out = 0.

# Spacial positioning of the top and out detectors, 1 to 16 -------------------------------------
detectors_top_x = [-2.125, -1.175, -0.225,  0.725,  1.675,  2.625,  3.575,  4.525,
                   5.475,  6.425,  7.375,  8.325,  9.275, 10.225, 11.175, 12.125]
detectors_top_y = [106., 106., 106., 106., 106., 106., 106., 106., 106., 106., 106.,
                   106., 106., 106., 106., 106.]

detectors_out_x = [118., 118., 118., 118., 118., 118., 118., 118., 118., 118., 118.,
                   118., 118., 118., 118., 118.]
detectors_out_y = [7.125,  6.175,  5.225,  4.275,  3.325,  2.375,  1.425,  0.475,
                   -0.475, -1.425, -2.375, -3.325, -4.275, -5.225, -6.175, -7.125]

# Average or find the maximum of the signals --------------------------------------------------
avg_x_top = np.average(detectors_top_x, weights=signals_top)
avg_y_top = np.average(detectors_top_y, weights=signals_top)

avg_x_out = np.average(detectors_out_x, weights=signals_out)
avg_y_out = np.average(detectors_out_y, weights=signals_out)


# Define the lines of sight that correspond to the average sensors ----------------------------
line_top = Line([avg_x_top, avg_y_top], [pinhole_x_top, pinhole_y_top])
line_out = Line([avg_x_out, avg_y_out], [pinhole_x_out, pinhole_y_out])

