'''
date_vs_accummulated_codec_plot.py

Reads in the file videos_export.csv,
and parses the data,
and plots three histograms of vp8, h264, and hvec by accumlated by date.

Craig Cahillane
May 26, 2020
'''

#####   Imports   #####
import sys
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

import datetime # for sorting dates

# Change the default matplotlib plotting to be better
mpl.rcParams.update({'figure.figsize':(12,9),
                     'text.usetex': False,
                     'font.family': 'serif',
                     # 'font.serif': 'Georgia',
                     # 'mathtext.fontset': 'cm',
                     'lines.linewidth': 2.5,
                     'font.size': 22,
                     'xtick.labelsize': 'large',
                     'ytick.labelsize': 'large',
                     'legend.fancybox': True,
                     'legend.fontsize': 18,
                     'legend.framealpha': 0.7,
                     'legend.handletextpad': 0.5,
                     'legend.labelspacing': 0.2,
                     'legend.loc': 'best',
                     'savefig.dpi': 80,
                     'pdf.compression': 9})

#####   Functions   #####
def main():
    '''main function of this script.  
    Makes date_vs_accumlated_codec_plot.pdf.
    '''
    filename = 'videos_export.csv'
    try:
        data = np.loadtxt(filename, dtype=str, skiprows=1, delimiter=',') # comma delimiter for csv!
    except OSError:
        print(f'\033[91m')
        print(f'Could not find {filename}')
        print(f'Please place in same directory as this script!')
        print(f'\033[0m')
        sys.exit()

    # Separate out columns of data
    dates = data[:,1]
    codecs = data[:,0]

    # # Create list of sortable datetime objects
    # datetimes = np.array([datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]) 

    # # Sort dates, get indicies of the sort, then apply to data
    # indicies = np.argsort(datetimes)
    # dates = dates[indicies]
    # codecs = codecs[indicies]

    
    # We loop through the data and stack our histogram data
    data_dict = {} # set up empty dictionary, which uses key:value hashing
    codec_names = np.array(['vp8', 'h264', 'h263', 'hevc', 'mpeg4'])
    for date, codec in zip(dates, codecs):
        if date not in data_dict.keys():
            data_dict[date] = {}
            for codec_name in codec_names:
                data_dict[date][codec_name] = 0

        try:
            data_dict[date][codec] += 1
        except KeyError:
            print(f'Found unusual codec {codec} in data. Eliminating and moving on')

    # Sort dictionary keys by date
    keys = np.array( list(data_dict.keys()) )
    datetimes = np.array([datetime.datetime.strptime(date, "%Y-%m-%d") for date in keys]) 
    indicies = np.argsort(datetimes)
    keys = keys[indicies]
    datetimes = datetimes[indicies]

    print(f'keys[0] = {keys[0]}')
    print(f'keys[-1] = {keys[-1]}')

    # Sort dictionary into arrays we can plot
    plot_dict = {}
    for codec_name in codec_names:
        codec_array = np.array([])
        for date in keys:
            codec_array = np.append(codec_array, data_dict[date][codec_name]) # makes array from dictionary[date][codec] values
        plot_dict[codec_name] = codec_array


    #####   Figure   #####
    # Figure 1: raw data
    fig, (s1) = plt.subplots() # launch the figure object fig, and axes s1

    xx = np.arange( len(data_dict.keys()) ) # convenient x-axis

    for codec_name in codec_names:
        codec_array = plot_dict[codec_name]
        s1.plot(xx, codec_array, label=codec_name)

    s1.set_xticks(xx[::50])
    s1.set_xticklabels(keys[::50], fontsize=12)

    s1.set_title('Date vs codec occurances')
    s1.set_xlabel('Date')
    s1.set_ylabel('Number of codec occurances')

    s1.grid()
    s1.grid(which='minor', ls='--', alpha=0.5)
    s1.legend()

    plot_name = f'date_vs_codec_plot.pdf'
    print(f'Writing plot PDF: {plot_name}')
    plt.savefig(plot_name, bbox_inches='tight')
    plt.close()



    # Figure 2: accumlated codecs
    fig, (s1) = plt.subplots() # launch the figure object fig, and axes s1

    for codec_name in codec_names:
        codec_array = plot_dict[codec_name]
        accumlated_codecs = np.cumsum(codec_array) # numpy calculates accumulated total for us
        final_total = accumlated_codecs[-1]
        s1.semilogy(xx, accumlated_codecs, label=codec_name + f' Total = {int(final_total)}')

    s1.set_xticks(xx[::50])
    s1.set_xticklabels(keys[::50], fontsize=12)

    s1.set_title('Date vs accumulated codec occurances')
    s1.set_xlabel('Date')
    s1.set_ylabel('Accumulated codec occurances')

    s1.grid()
    s1.grid(which='minor', ls='--', alpha=0.5)
    s1.legend()

    plot_name = f'date_vs_accumlated_codec_plot.pdf'
    print(f'Writing plot PDF: {plot_name}')
    plt.savefig(plot_name, bbox_inches='tight')
    plt.close()

    print('Function main() is done')

    return

# if this .py script is called directly with 
# $ python date_vs_accumlated_codec_plot.py 
# the below is true and main() will be run
if __name__ == "__main__": 
    main()

