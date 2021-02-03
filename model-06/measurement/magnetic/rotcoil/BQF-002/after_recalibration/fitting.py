#!/usr/bin/env python-sirius

import random
import numpy as np
from siriuspy.clientconfigdb import PVsConfig
import matplotlib.pyplot as plt
from siriuspy.pwrsupply.siggen import SigGenFactory


def waveform_configdb_get():

    global_config_name = 'ConfigB_adjust_rffreq'
    pvname = 'BO-Fam:PS-QF:Wfm-SP'
    o = PVsConfig(name=global_config_name)
    wfm = np.array(o.pvs[pvname])
    return wfm


def run():

    wfm = waveform_configdb_get()
    currmax = max(abs(wfm))
    print('Max. current: {} A'.format(currmax))

    # currdif = currmax * percent

    # curridx = [0, ]
    # currvalue = wfm[0]
    # lasti = 0
    # for i in range(1, len(wfm)):
    #     value = wfm[i]
    #     if abs(value - currvalue) > currdif:
    #         curridx.append(i)
    #         currvalue = value
    #         lasti = i
    # # if len(wfm) - 1 not in curridx:
    # #     curridx.append(len(wfm) - 1)
    # curridx = np.array(curridx)
    # currwfm = wfm[curridx]

    curridx = range(0,len(wfm), 1)
    currwfm = wfm[curridx]

    # print(len(curridx))
    plt.plot(wfm)
    plt.plot(curridx, currwfm, 'o')
    plt.show()
    for v in currwfm:
        print('{:07.2f}'.format(v))


def norm_time(rampup_time, plateau_time, rampdown_time):

    tot_time = (rampup_time + plateau_time + rampdown_time)
    rampup_time *= (0.5/tot_time)
    plateau_time *= (0.5/tot_time)
    rampdown_time *= (0.5/tot_time)

    return rampup_time, plateau_time, rampdown_time


def gen_wfm_siggen(amplitude, rampup_time, plateau_time, rampdown_time):

    # tot_time = (rampup_time + plateau_time + rampdown_time)
    # rampup_time *= (0.5/tot_time)
    # plateau_time *= (0.5/tot_time)
    # rampdown_time *= (0.5/tot_time)

    sg = SigGenFactory.create(
        sigtype='Trapezoidal',
        num_cycles=1,
        amplitude=amplitude,
        offset=0,
        aux_param=[rampup_time, plateau_time, rampdown_time, 0]
        )

    # print(sg.rampup_time)
    # print(sg.plateau_time)
    # print(sg.rampdown_time)

    wfm_siggen, time = sg.get_waveform(len(wfm_ramp))

    return np.array(wfm_siggen), np.array(time)


def fit():

    # otimização fixando amplitude máxima
    delta_amplitude = 0
    amplitude = 104.89
    rampup_time = 0.32550204440509495
    plateau_time = 0.030437405474594968
    rampdown_time = 0.14862606770348888

    rampup_time, plateau_time, rampdown_time = norm_time(rampup_time, plateau_time, rampdown_time)
    wfm_siggen, time = gen_wfm_siggen(amplitude, rampup_time, plateau_time, rampdown_time)
    chi = np.sum((wfm_siggen - wfm_ramp)**2)
    print('chi inicial: ', np.sqrt(chi))
    it_max = 1000
    it = 0
    while True:
        it += 1
        amplitude_new = amplitude * (1 + 2*(random.random() - 0.5)*delta_amplitude)
        rampup_time_new = rampup_time * (1 + 2*(random.random() - 0.5)*0.01)
        rampdown_time_new = rampdown_time * (1 + 2*(random.random() - 0.5)*0.01)
        plateau_time_new = plateau_time * (1 + 2*(random.random() - 0.5)*0.01)
        rampup_time, plateau_time, rampdown_time = norm_time(rampup_time, plateau_time, rampdown_time)
        wfm_siggen_new, time = gen_wfm_siggen(amplitude_new, rampup_time_new, plateau_time_new, rampdown_time_new)
        chi_new = np.sum((wfm_siggen_new - wfm_ramp)**2)
        if chi_new < chi:
            amplitude = amplitude_new
            rampup_time = rampup_time_new
            rampdown_time = rampdown_time_new
            plateau_time = plateau_time_new
            chi = chi_new
            print(np.sqrt(chi), amplitude_new, rampup_time_new, plateau_time_new, rampdown_time_new)
        if it % 1000 == 0:
            print('iteration: ', it)
        if it > it_max:
            break

    wfm_siggen, time = gen_wfm_siggen(amplitude, rampup_time, plateau_time, rampdown_time)
    plt.plot(time, wfm_ramp)
    plt.plot(time, wfm_siggen)
    plt.xlabel('Time [s]')
    plt.ylabel('Current [A]')
    plt.title('BO QF Cycling')
    plt.grid()
    plt.show()


wfm_ramp = waveform_configdb_get()

# run()
fit()
