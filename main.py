import numpy as np


def tomo_centroid(signals):
    """ Return the optical estimation for the center of mass

    Parameters
    ----------
    signals: nd array 32 x T
        32 by T array, where T is the number of time instants

    Returns
    -------
    tomo_r0: nd array 1 x T
        R coordinate of the center of mass for each time instant
    tomo_z: nd array 1 x T
        z coordinate of the center of mass for each time instant

    """
    # Signals from the tomography diagnostic (top and out cameras) --------------------------------
    signals_top = np.array(signals[:16]).T  # T by 16
    signals_out = np.array(signals[16:]).T  # T by 16

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

    # Find average sensors  ------------------------------------------------------------------------
    avg_x_top = np.sum(signals_top * detectors_top_x, axis=1) / np.sum(signals_top, axis=1)
    avg_y_top = np.sum(signals_top * detectors_top_y, axis=1) / np.sum(signals_top, axis=1)

    avg_x_out = np.sum(signals_out * detectors_out_x, axis=1) / np.sum(signals_out, axis=1)
    avg_y_out = np.sum(signals_out * detectors_out_y, axis=1) / np.sum(signals_out, axis=1)

    # Define the lines of sight that correspond to the average sensors ----------------------------
    m_top = (avg_y_top - pinhole_y_top) / (avg_x_top - pinhole_x_top)  # Slope of top LoS
    b_top = pinhole_y_top - m_top * pinhole_x_top  # y intercept of top LoS

    m_out = (avg_y_out - pinhole_y_out) / (avg_x_out - pinhole_x_out)  # Slope of out LoS
    b_out = pinhole_y_out - m_out * pinhole_x_out  # y intercept of out LoS

    r_intersection = (b_top - b_out) / (m_out - m_top)  # x of top and out LoS intersection
    z_intersection = m_out * r_intersection + b_out     # y of top and out LoS intersection

    return r_intersection, z_intersection


# test_signals = np.random.random((32, 100))
# test_result = tomo_centroid(test_signals)
