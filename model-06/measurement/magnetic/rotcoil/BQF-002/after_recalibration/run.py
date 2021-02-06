#!/usr/bin/env python-sirius

import matplotlib.pyplot as plt
import numpy as np


def correct_excdata(plot=True):

    currs = [0.05, 2, 4, 6, 8, 10, 30, 50, 70, 90, 110, 130]

    c1_2021 = np.array([0.0111, 2.0104, 4.0073, 6.0113, 8.0124, 10.0126, 30.0149, 50.016, 70.0169, 90.0138, 110.0141, 130.0187, 110.0145, 90.0139, 70.017, 50.0159, 30.0148, 10.0128, 8.0122, 6.0117, 4.0082, 2.0104, 0.0111, ])
    m1_2021 = np.array([-0.01215491, -0.08626859, -0.1615623, -0.2376747, -0.3138991, -0.3904883, -1.162666, -1.931716, -2.698771, -3.458314, -4.205542, -4.934042, -4.228508, -3.479206, -2.716953, -1.948282, -1.177281, -0.3995486, -0.3218263, -0.2444612, -0.1669741, -0.08989353, -0.01285774, ])
    c2_2021 = np.array([0.0113, 2.0106, 4.0072, 6.0116, 8.0124, 10.0125, 30.0148, 50.016, 70.0169, 90.014, 110.0143, 130.0189, 110.0146, 90.0135, 70.0168, 50.0158, 30.0148, 10.0125, 8.0125, 6.0118, 4.0076, 2.0104, 0.011, ])
    m2_2021 = np.array([-0.01198259, -0.08654086, -0.1615185, -0.23749, -0.3139278, -0.3904646, -1.162067, -1.930927, -2.698374, -3.458122, -4.205655, -4.934025, -4.228286, -3.478934, -2.71647, -1.947923, -1.177429, -0.3995107, -0.3221678, -0.2444059, -0.166983, -0.09002602, -0.01288148, ])
    c3_2021 = np.array([0.0111, 2.0104, 4.0072, 6.0118, 8.0124, 10.0125, 30.015, 50.016, 70.017, 90.014, 110.0142, 130.0188, 110.0147, 90.0139, 70.017, 50.016, 30.015, 10.0125, 8.0127, 6.0118, 4.0081, 2.0104, 0.011, ])
    m3_2021 = np.array([-0.01200303, -0.08626319, -0.1615332, -0.2376098, -0.3138666, -0.3903503, -1.162026, -1.931152, -2.698185, -3.457997, -4.205531, -4.934032, -4.228328, -3.478939, -2.716578, -1.947865, -1.177005, -0.3995779, -0.3219796, -0.2443882, -0.166969, -0.08983911, -0.01286573, ])
    # c_2021_up = np.hstack([c1_2021[:11], c2_2021[:11], c3_2021[:11]])
    # m_2021_up = np.hstack([m1_2021[:11], m2_2021[:11], m3_2021[:11]])
    # zipped = zip(c_2021_up, m_2021_up)
    # zipped = sorted(zipped)
    # c_2021_up, m_2021_up = zip(*zipped)
    # m_2021_up = np.interp(currs, c_2021_up, m_2021_up)
    c_2021_up = (c1_2021[:12] + c2_2021[:12] + c3_2021[:12])/3
    m_2021_up = (m1_2021[:12] + m2_2021[:12] + m3_2021[:12])/3

    c1_2016 = np.array([0.0078, 2.0059, 4.0043, 6.002, 8.0009, 9.9987, 29.9963, 49.9984, 70.0021, 90.0021, 110.0031, 130.0002, 110.0013, 89.9997, 69.9996, 49.9967, 29.9961, 9.9977, 7.9996, 6.0006, 4.0027, 2.0038, 0.0043, ])
    m1_2016 = np.array([-0.01179837, -0.08538105, -0.1592165, -0.2334934, -0.3079047, -0.3823842, -1.133442, -1.888187, -2.641512, -3.388832, -4.125697, -4.835475, -4.143477, -3.406367, -2.657592, -1.903832, -1.147642, -0.3911246, -0.315505, -0.2399524, -0.1643784, -0.08885089, -0.01320705, ])
    c2_2016 = np.array([0.0031, 2.0025, 4.0014, 5.9997, 7.9991, 9.9972, 29.9956, 49.9985, 70.0026, 90.0036, 110.005, 130.0036, 110.0036, 90.0013, 70.0002, 49.9971, 29.9957, 9.997, 7.9991, 5.9999, 4.002, 2.003, 0.0039, ])
    m2_2016 = np.array([-0.01163553, -0.08523227, -0.1591025, -0.2333829, -0.3078286, -0.3823313, -1.133381, -1.888001, -2.641273, -3.388772, -4.125574, -4.835493, -4.143462, -3.406291, -2.657515, -1.9038, -1.147602, -0.3910514, -0.3155562, -0.239949, -0.1643499, -0.08880532, -0.01322885, ])
    # c_2016_up = np.hstack([c1_2016[:11], c2_2016[:11]])
    # m_2016_up = np.hstack([m1_2016[:11], m2_2016[:11]])
    # zipped = zip(c_2016_up, m_2016_up)
    # zipped = sorted(zipped)
    # c_2016_up, m_2016_up = zip(*zipped)
    # m_2016_up = np.interp(currs, c_2016_up, m_2016_up)
    c_2016_up = (c1_2016[:12] + c2_2016[:12])/2
    m_2016_up = (m1_2016[:12] + m2_2016[:12])/2

    diff = 100 * (m_2021_up - m_2016_up) / m_2016_up

    print(currs)
    print(c_2016_up)
    print(m_2016_up)
    print(m_2021_up)

    for i in range(len(currs)):
        print('{:+08.2f}  {:+.6e} {:+.6e}  {:+06.2}'.format(currs[i], m_2016_up[i], m_2021_up[i], diff[i]))

    print(currs)
    print(diff)

    if plot:
        plt.plot(currs, diff, 'o-')
        plt.xlabel('Current [A]')
        plt.ylabel('GL Diff. 2021-2016 [%]')
        plt.title('Booster BQF-002 magnets recalibration')
        plt.grid()
        plt.show()

    excdata = np.array([
        [-0130.00,  +4.975413E-05, -1.251647e-04,  +4.825073e+00, -4.370731e-03,  -1.041956e-02, -1.667820e-01,  -1.111587e+00, +1.740654e+00,  -2.688518e+01, +9.932553e+00,  -6.057332e+04, -5.515321e+02,  +1.233434e+05, -7.827446e+02,  -2.309567e+06, -5.601336e+06,  -2.089645e+08, +8.768356e+07,  +6.099797e+11, -5.473266e+09,  +1.830748e+11, -5.842078e+11,  +5.115496e+12, +1.575038e+13, ],
        [-0110.00,  +4.468525E-05, -1.084278e-04,  +4.119179e+00, -3.734749e-03,  -1.485607e-02, -1.398402e-01,  -1.006962e+00, +1.443497e+00,  -2.380298e+01, +7.292960e+00,  -5.174963e+04, -4.510194e+02,  +1.068457e+05, -3.388785e+03,  -2.123045e+06, -5.105658e+06,  -1.823067e+08, +7.512986e+07,  +5.201871e+11, -4.368900e+09,  +1.638989e+11, -5.021653e+11,  +3.210291e+12, +1.244415e+13, ],
        [-0090.00,  +3.506264E-05, -8.985250e-05,  +3.384542e+00, -3.065197e-03,  -1.323389e-02, -1.146652e-01,  -8.078223e-01, +1.191413e+00,  -1.984210e+01, +5.299454e+00,  -4.255402e+04, -3.713754e+02,  +8.643198e+04, -3.201614e+03,  -1.912936e+06, -4.228049e+06,  -1.442474e+08, +5.811757e+07,  +4.275050e+11, -3.532057e+09,  +1.397439e+11, -4.046176e+11,  +2.199086e+12, +6.257237e+12, ],
        [-0070.00,  +2.769226E-05, -7.081099e-05,  +2.638384e+00, -2.382182e-03,  -1.119286e-02, -8.906358e-02,  -5.941664e-01, +9.331264e-01,  -1.483847e+01, +4.582235e+00,  -3.334584e+04, -2.960058e+02,  +6.696821e+04, -1.069035e+03,  -1.539488e+06, -3.196976e+06,  -9.802001e+07, +4.865710e+07,  +3.336112e+11, -3.191102e+09,  +1.268394e+11, -2.981701e+11,  +2.582209e+12, +8.805070e+12, ],
        [-0050.00,  +2.101568E-05, -5.124401e-05,  +1.886320e+00, -1.687763e-03,  -8.159495e-03, -6.365762e-02,  -4.680534e-01, +6.678828e-01,  -1.091581e+01, +3.164498e+00,  -2.374636e+04, -1.589828e+02,  +4.751822e+04, -2.471981e+03,  -1.082268e+06, -2.266195e+06,  -7.783485e+07, +3.086406e+07,  +2.397330e+11, -1.628409e+09,  +3.263360e+10, -2.437467e+11,  +7.296141e+11, +5.454485e+12, ],
        [-0030.00,  +1.415847E-05, -3.137665e-05,  +1.132137e+00, -9.959846e-04,  -5.144620e-03, -3.816778e-02,  -3.420774e-01, +4.129985e-01,  -5.874273e+00, +2.559648e+00,  -1.476051e+04, -4.692343e+01,  +2.784377e+04, -4.260748e+02,  -4.335212e+05, -1.164266e+06,  -4.156107e+07, +2.531539e+07,  +1.433689e+11, -5.113688e+08,  +4.323662e+10, -1.266462e+11,  +5.425462e+11, +3.161152e+12, ],
        [-0010.00,  +6.945712E-06, -1.122662e-05,  +3.806970e-01, +3.258761e-04,  -2.800998e-03, -1.373344e-02,  -1.700215e-01, +1.109160e-01,  -1.380643e+00, +6.575470e-01,  -5.191920e+03, -8.856127e+01,  +6.705360e+03, -1.665330e+03,  -4.043400e+04, -7.355345e+05,  -1.362301e+07, -7.947977e+06,  +4.868438e+10, -6.987624e+08,  -3.039707e+10, -6.671230e+10,  +1.504686e+12, -2.522009e+12, ],
        [-0008.00,  +6.062070E-06, -9.226832e-06,  +3.060464e-01, -2.746298e-04,  -2.685181e-03, -1.141577e-02,  -1.535821e-01, +7.748079e-02,  -1.032027e+00, +2.028977e-01,  -4.253522e+03, -5.934335e+01,  +1.010444e+04, -1.123064e+03,  -1.371630e+05, -5.133734e+05,  +2.067505e+06, +6.356333e+06,  +3.888603e+10, -1.767112e+08,  +2.513252e+10, -4.299598e+10,  -3.580429e+11, +2.634007e+11, ],
        [-0006.00,  +5.158089E-06, -7.184020e-06,  +2.314631e-01, +1.939842e-04,  -2.425587e-03, -8.789633e-03,  -1.128920e-01, +5.333088e-02,  -2.017947e+00, +3.801416e-03,  -3.376908e+03, -5.030495e+01,  +7.138365e+03, -2.811232e+03,  -2.111745e+04, -3.449331e+05,  -2.170232e+07, -3.837938e+06,  +3.016023e+10, -1.054210e+08,  -2.008309e+09, -6.986779e+10,  +6.485781e+11, -4.341895e+11, ],
        [-0004.00,  +4.252322E-06, -5.179476e-06,  +1.569668e-01, -1.420953e-04,  -2.400881e-03, -6.383120e-03,  -9.973878e-02, +3.142826e-02,  -9.259937e-01, -2.957493e-01,  -2.461973e+03, -2.658068e+01,  +4.685728e+03, -4.200395e+02,  -1.017639e+05, -4.019085e+05,  -4.447178e+06, -5.005527e+06,  +2.084676e+10, -3.665317e+08,  -2.282927e+10, -3.881456e+10,  -1.687947e+12, -1.921884e+12, ],
        [-0002.00,  +3.267350E-06, -3.151156e-06,  +8.288950e-02, -7.282650e-05,  -2.512963e-03, -4.154182e-03,  -6.796411e-02, +2.008410e-06,  -1.157945e+00, -1.107516e+00,  -1.703330e+03, -1.258265e+01,  +6.723557e+03, +7.205065e+02,  +9.632571e+04, -3.699185e+05,  -6.634481e+06, -1.923343e+07,  +9.729464e+09, +4.933769e+08,  -4.632190e+10, +1.696671e+09,  +7.928116e+11, -5.525866e+12, ],
        # [+0000.00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00,  +0.000000e+00, +0.000000e+00, ],
        [+0002.00,  -3.267350e-06, +3.151156e-06,  -8.288950e-02, +7.282650e-05,  +2.512963e-03, +4.154182e-03,  +6.796411e-02, -2.008410e-06,  +1.157945e+00, +1.107516e+00,  +1.703330e+03, +1.258265e+01,  -6.723557e+03, -7.205065e+02,  -9.632571e+04, +3.699185e+05,  +6.634481e+06, +1.923343e+07,  -9.729464e+09, -4.933769e+08,  +4.632190e+10, -1.696671e+09,  -7.928116e+11, +5.525866e+12, ],
        [+0004.00,  -4.252322e-06, +5.179476e-06,  -1.569668e-01, +1.420953e-04,  +2.400881e-03, +6.383120e-03,  +9.973878e-02, -3.142826e-02,  +9.259937e-01, +2.957493e-01,  +2.461973e+03, +2.658068e+01,  -4.685728e+03, +4.200395e+02,  +1.017639e+05, +4.019085e+05,  +4.447178e+06, +5.005527e+06,  -2.084676e+10, +3.665317e+08,  +2.282927e+10, +3.881456e+10,  +1.687947e+12, +1.921884e+12, ],
        [+0006.00,  -5.158089e-06, +7.184020e-06,  -2.314631e-01, -1.939842e-04,  +2.425587e-03, +8.789633e-03,  +1.128920e-01, -5.333088e-02,  +2.017947e+00, -3.801416e-03,  +3.376908e+03, +5.030495e+01,  -7.138365e+03, +2.811232e+03,  +2.111745e+04, +3.449331e+05,  +2.170232e+07, +3.837938e+06,  -3.016023e+10, +1.054210e+08,  +2.008309e+09, +6.986779e+10,  -6.485781e+11, +4.341895e+11, ],
        [+0008.00,  -6.062070e-06, +9.226832e-06,  -3.060464e-01, +2.746298e-04,  +2.685181e-03, +1.141577e-02,  +1.535821e-01, -7.748079e-02,  +1.032027e+00, -2.028977e-01,  +4.253522e+03, +5.934335e+01,  -1.010444e+04, +1.123064e+03,  +1.371630e+05, +5.133734e+05,  -2.067505e+06, -6.356333e+06,  -3.888603e+10, +1.767112e+08,  -2.513252e+10, +4.299598e+10,  +3.580429e+11, -2.634007e+11, ],
        [+0010.00,  -6.945712e-06, +1.122662e-05,  -3.806970e-01, -3.258761e-04,  +2.800998e-03, +1.373344e-02,  +1.700215e-01, -1.109160e-01,  +1.380643e+00, -6.575470e-01,  +5.191920e+03, +8.856127e+01,  -6.705360e+03, +1.665330e+03,  +4.043400e+04, +7.355345e+05,  +1.362301e+07, +7.947977e+06,  -4.868438e+10, +6.987624e+08,  +3.039707e+10, +6.671230e+10,  -1.504686e+12, +2.522009e+12, ],
        [+0030.00,  -1.415847e-05, +3.137665e-05,  -1.132137e+00, +9.959846e-04,  +5.144620e-03, +3.816778e-02,  +3.420774e-01, -4.129985e-01,  +5.874273e+00, -2.559648e+00,  +1.476051e+04, +4.692343e+01,  -2.784377e+04, +4.260748e+02,  +4.335212e+05, +1.164266e+06,  +4.156107e+07, -2.531539e+07,  -1.433689e+11, +5.113688e+08,  -4.323662e+10, +1.266462e+11,  -5.425462e+11, -3.161152e+12, ],
        [+0050.00,  -2.101568e-05, +5.124401e-05,  -1.886320e+00, +1.687763e-03,  +8.159495e-03, +6.365762e-02,  +4.680534e-01, -6.678828e-01,  +1.091581e+01, -3.164498e+00,  +2.374636e+04, +1.589828e+02,  -4.751822e+04, +2.471981e+03,  +1.082268e+06, +2.266195e+06,  +7.783485e+07, -3.086406e+07,  -2.397330e+11, +1.628409e+09,  -3.263360e+10, +2.437467e+11,  -7.296141e+11, -5.454485e+12, ],
        [+0070.00,  -2.769226e-05, +7.081099e-05,  -2.638384e+00, +2.382182e-03,  +1.119286e-02, +8.906358e-02,  +5.941664e-01, -9.331264e-01,  +1.483847e+01, -4.582235e+00,  +3.334584e+04, +2.960058e+02,  -6.696821e+04, +1.069035e+03,  +1.539488e+06, +3.196976e+06,  +9.802001e+07, -4.865710e+07,  -3.336112e+11, +3.191102e+09,  -1.268394e+11, +2.981701e+11,  -2.582209e+12, -8.805070e+12, ],
        [+0090.00,  -3.506264e-05, +8.985250e-05,  -3.384542e+00, +3.065197e-03,  +1.323389e-02, +1.146652e-01,  +8.078223e-01, -1.191413e+00,  +1.984210e+01, -5.299454e+00,  +4.255402e+04, +3.713754e+02,  -8.643198e+04, +3.201614e+03,  +1.912936e+06, +4.228049e+06,  +1.442474e+08, -5.811757e+07,  -4.275050e+11, +3.532057e+09,  -1.397439e+11, +4.046176e+11,  -2.199086e+12, -6.257237e+12, ],
        [+0110.00,  -4.468525e-05, +1.084278e-04,  -4.119179e+00, +3.734749e-03,  +1.485607e-02, +1.398402e-01,  +1.006962e+00, -1.443497e+00,  +2.380298e+01, -7.292960e+00,  +5.174963e+04, +4.510194e+02,  -1.068457e+05, +3.388785e+03,  +2.123045e+06, +5.105658e+06,  +1.823067e+08, -7.512986e+07,  -5.201871e+11, +4.368900e+09,  -1.638989e+11, +5.021653e+11,  -3.210291e+12, -1.244415e+13, ],
        [+0130.00,  -4.975413e-05, +1.251647e-04,  -4.825073e+00, +4.370731e-03,  +1.041956e-02, +1.667820e-01,  +1.111587e+00, -1.740654e+00,  +2.688518e+01, -9.932553e+00,  +6.057332e+04, +5.515321e+02,  -1.233434e+05, +7.827446e+02,  +2.309567e+06, +5.601336e+06,  +2.089645e+08, -8.768356e+07,  -6.099797e+11, +5.473266e+09,  -1.830748e+11, +5.842078e+11,  -5.115496e+12, -1.575038e+13, ],
    ])

    for datum in excdata:
        curr, *mpoles = datum
        mpoles = np.array(mpoles)
        corr = 1 + np.interp(abs(curr), currs, diff)/100
        mpoles *= corr
        # print(curr, corr, mpoles)
        print('{:+08.2f}  '.format(curr), end='')
        for i in range(len(mpoles)//2):
            print('{:+.6e} {:+.6e}  '.format(mpoles[2*i+0], mpoles[2*i+1]), end='')
        print()


correct_excdata(plot=True)
