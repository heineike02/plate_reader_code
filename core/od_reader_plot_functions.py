import matplotlib.pyplot as plt
import numpy as np
import pandas as pd  #Just importing this to check a datatype - could probably just do it with long name
from core import od_reader_data_load as odl # See above. 

def OD_plot_subplots(OD_data, well_arr, time_list,axis_vec = []):
    fig, axarr = plt.subplots(well_arr.nrows,well_arr.ncols, sharex=True, sharey=True)
    
    #axarr[0, 0].plot(x, y)
    if isinstance(OD_data, pd.core.frame.DataFrame): 
        for jj in range(well_arr.nrows):
            for kk in range(well_arr.ncols): 
                yy = OD_data[well_arr.wells[jj][kk]]
                axarr[jj, kk].plot(time_list, yy)
                axarr[jj, kk].set_title(well_arr.wells[jj][kk])
                if axis_vec != []:
                    axarr[jj, kk].axis(axis_vec)
    
    
    #Initial version made OD_data_object, but a pandas dataframe is probably better to use. 
    elif isinstance(OD_data, odl.OD_data_obj): 
        for jj in range(well_arr.nrows):
            for kk in range(well_arr.ncols): 
                yy = OD_data.data[OD_data.index[well_arr.wells[jj][kk]]]  #This is the only difference between the two for loops. 
                axarr[jj, kk].plot(time_list, yy)
                axarr[jj, kk].set_title(well_arr.wells[jj][kk])
                if axis_vec != []:
                    axarr[jj, kk].axis(axis_vec)
            
    
    return fig

def OD_plot_sameplot(OD_data, well_list, time_list,color_list, linestyle_list ,ax_in, legend_list):
    #Function requires well_list to be a well array with only one column.
    #plt.hold(True)
    
    for jj in range(well_list.nrows):
       yy = OD_data.data[OD_data.index[well_list.wells[jj]]]
       ax_in.plot(time_list, yy, label = legend_list[jj], color = color_list[jj], linestyle = linestyle_list[jj],linewidth = 3 )
       #axarr[jj, kk].axis(axis_vec)
    ax_in.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol = 2) #bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #return ax_in
