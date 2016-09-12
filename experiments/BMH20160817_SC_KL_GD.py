#import sys
from ..core import od_reader_data_load as odl
from ..core import od_reader_plot_functions as odp
#from IPython.core.debugger import Tracer
from ..core import growth_curve_fit as gc_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
#from pandas.tools.plotting import scatter_matrix

def main():
    #Need to open data file and save as a .csv
    dirname = "C:/Users/Ben/Google Drive/UCSF/ElSamad_Lab/PKA/WetLab/Plate_reader/"
    fname = "20160817_SC_KL_GD.csv"
    #Each column is a time point with 96 measurements. Rows are transposed into columns and stacked on top of one another from row A to H.  
    ntimes = 94
    nrows = 8
    ncols = 12
    starting_row = 'A'
    starting_col = 1
    
    OD_data, time_list = odl.get_OD_data(dirname,fname, ntimes, nrows, ncols,starting_row,starting_col)
    
        
    #Multiindex object - four conditions, N replicates
    layer_names = ['Species', 'Condition','Replicate']
    
    experiment_setup = [['K.Lac','S.Cer'],['SDC','SDC NO Spin', 'Gluc->Sorb', 'Gluc DO'],['1','2','3','5','6','7','8']]      
    data_index = pd.MultiIndex.from_product(experiment_setup, names= layer_names)
    #Remove missing conditions from the end of S.Cer data
    missing_condition_indices = [7*jj - 2 for jj in [6,8]]+[7*jj - 1 for jj in [6,8]]
    data_index_adjusted = data_index.set_labels([np.delete(label_level,[missing_condition_indices]) for label_level in data_index.labels])
    
    wells = ['B4','C4','D4','F4','G4','B2','B3','B7','C7','D7','F7','G7','E2','E3','B5','C5','D5','F5','G5','C2','C3','B6','C6','D6','F6','G6','D2','D3', 
            'B8','C8','D8','F8','G8','F2','F3','B11','C11','D11','F11','G11','B9','C9','D9','F9','G9','H2','H3','B10','C10','D10','F10','G10'] 
    
    color_list = ['k','g','b','c']
    blank = np.mean(OD_data.data[OD_data.index['A2']])
    growth_data = [OD_data.data[OD_data.index[well]]-blank for well in wells ]
    #len(growth_data)
    growth_data_df = pd.DataFrame(growth_data, index=data_index_adjusted, columns = time_list)
    growth_data_mean = growth_data_df.loc['K.Lac'].groupby(level='Condition').mean().transpose()
    growth_data_std = growth_data_df.loc['K.Lac'].groupby(level = 'Condition').std().transpose()
    
    fig1 , ax_KL_0817 = plt.subplots()
    ax_KL_0817 = growth_data_mean.plot(kind = 'line',yerr = growth_data_std, color = color_list);
    ax_KL_0817.set_title('K.Lac Growth')
    ax_KL_0817.set_ylabel('OD600')
    ax_KL_0817.set_xlabel('time(min)')
    ax_KL_0817.set_ylim([0,1.2]) 
    plt.show()
    
    #Plot S.Cerevisiae data    
    growth_data_mean = growth_data_df.loc['S.Cer'].groupby(level='Condition').mean().transpose()
    growth_data_std = growth_data_df.loc['S.Cer'].groupby(level = 'Condition').std().transpose()
    fig2 , ax_SC_0817 = plt.subplots()
    ax_SC_0817 = growth_data_mean.plot(kind = 'line',yerr = growth_data_std, color = color_list);
    ax_SC_0817.set_title('S.Cer Growth')
    ax_SC_0817.set_ylabel('OD600')
    ax_SC_0817.set_xlabel('time(min)')
    ax_SC_0817.set_ylim([0,1.2]) 
    plt.show()
    #Can't figure out how to get it to save the figure!!
    #fig1.tight_layout()
    #fig1.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20160817_KL.png'))
    #fig8 = plt.figure()
    #ax_bar_k = growth_curve_df_YP_only['k'].plot(kind='bar');
    #fig8.tight_layout()
    #fig8.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20151027_YP_k.png'))
    
    #Need to open data file and save as a .csv
    dirname = "C:/Users/Ben/Google Drive/UCSF/ElSamad_Lab/PKA/WetLab/Plate_reader/"
    fname = "20160816_SC_KL_GD_after_break.csv"
    #Each column is a time point with 96 measurements. Rows are transposed into columns and stacked on top of one another from row A to H.  
    ntimes = 91
    nrows = 8
    ncols = 12
    starting_row = 'A'
    starting_col = 1
    
    OD_data, time_list = odl.get_OD_data(dirname,fname, ntimes, nrows, ncols,starting_row,starting_col)
    
    #Multiindex object - four conditions, N replicates
    layer_names = ['Species', 'Condition','Replicate']
    
    experiment_setup = [['K.Lac','S.Cer'],['SDC','SDC NO Spin', 'Gluc->Sorb', 'Gluc DO'],['1','2','3','4','5','6','7','8']]      
    data_index = pd.MultiIndex.from_product(experiment_setup, names= layer_names)
    #Remove missing conditions from the end of S.Cer data
    missing_condition_indices = [7*jj - 2 for jj in [6,8]]+[7*jj - 1 for jj in [6,8]]
    data_index_adjusted = data_index.set_labels([np.delete(label_level,[missing_condition_indices]) for label_level in data_index.labels])
    
    wells = ['B4','C4','D4','E4','F4','G4','B2','B3','B7','C7','D7','E7','F7','G7','E2','E3','B5','C5','D5','E5','F5','G5','C2','C3','B6','C6','D6','E6','F6','G6','D2','D3', 
            'B8','C8','D8','E8','F8','G8','F2','F3','B11','C11','D11','E11','F11','G11','B9','C9','D9','E9','F9','G9','H2','H3','B10','C10','D10','E10','F10','G10'] 
    
    blank = np.mean(OD_data.data[OD_data.index['A2']])
    growth_data = [OD_data.data[OD_data.index[well]]-blank for well in wells ]
    #len(growth_data)
    
    #Note: can't use linestyles with error bars. 
    color_list = ['k','g','b','c']
    growth_data_df = pd.DataFrame(growth_data, index=data_index_adjusted, columns = time_list)
    growth_data_mean = growth_data_df.loc['K.Lac'].groupby(level='Condition').mean().transpose()
    growth_data_std = growth_data_df.loc['K.Lac'].groupby(level = 'Condition').std().transpose()
    
    fig4, ax_KL_0816 = plt.subplots();
    ax_KL_0816 = growth_data_mean.plot(kind = 'line', yerr = growth_data_std, color = color_list);
    ax_KL_0816.set_title('K.Lac Growth')
    ax_KL_0816.set_ylabel('OD600')
    ax_KL_0816.set_xlabel('time(min)')
    ax_KL_0816.set_ylim([0,1.2])        
    plt.show()
    #yerr = growth_data_std
    #layer_size = [len(layer_list) for layer_list in strain_list]
    #growth_curve_df = pd.DataFrame(np.zeros([np.product(layer_size),len(col_list)]), index = data_index, columns = col_list)
    

    #Plot S.Cerevisiae data    
    growth_data_mean = growth_data_df.loc['S.Cer'].groupby(level='Condition').mean().transpose()
    growth_data_std = growth_data_df.loc['S.Cer'].groupby(level = 'Condition').std().transpose()
    fig4 , ax_SC_0816 = plt.subplots()
    ax_SC_0816 = growth_data_mean.plot(kind = 'line',yerr = growth_data_std, color = color_list);
    ax_SC_0816.set_title('S.Cer Growth')
    ax_SC_0816.set_ylabel('OD600')
    ax_SC_0816.set_xlabel('time(min)')
    ax_SC_0816.set_ylim([0,1.2]) 
    plt.show()
    
    
    

    
    
    return
    
    #Plot all wells raw OD
    wells = odl.all_wells(['B','C','D','E','F','G'],[2,3,4,5,6,7,8,9,10,11])
    well_arr = odl.well_array(wells)
    
    #fig1 = odp.OD_plot_subplots(OD_data, well_arr, time_list,[])
    #plt.show()
      
    #Plot OD of KL and SC SDC strains
    fig2, axarr = plt.subplots(2,1, sharex=True, sharey=True)
    
    # E Wells looked very bad - all clumped together afterwards - why all in the same well?
    legend_list = [[ 'SDC 1', 'SDC 2','SDC 3', 'SDC 4', 'SDC 5','SDC 6','SDC 7', 'SDC 8','SDC No spin 1', 'SDC No spin 2','SDC No spin 3','SDC No spin 4','SDC No spin 5','SDC No spin 6','SDC No spin 7','SDC No spin 8','GD 1', 'GD 2', 'GD 3','GD 4', 'GD 5','GD 6','GD 7','GD 8','GD NO 1','GD NO 2','GD NO 3','GD NO 4','GD NO 5','GD NO 6','GD NO 7','GD NO 8'] ,
    [ 'SDC 1', 'SDC 2','SDC 3', 'SDC 4', 'SDC 5','SDC 6','SDC 7', 'SDC 8','SDC No spin 1', 'SDC No spin 2','SDC No spin 3','SDC No spin 4','SDC No spin 5','SDC No spin 6','GD 1', 'GD 2', 'GD 3','GD 4', 'GD 5','GD 6','GD 7','GD 8','GD NO 1','GD NO 2','GD NO 3','GD NO 4','GD NO 5','GD NO 6']]
    color_list = [['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','r','r','r','r','r','r','r','r','k','k','k','k','k','k','k','k'],
    ['b','b','b','b','b','b','b','b','b','b','b','b','b','b','r','r','r','r','r','r','r','r','k','k','k','k','k','k']]
    linestyle_list = [['-','-','-','-','-','-','-','-','--','--','--','--','--','--','--','--','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-','-','--','--','--','--','--','--','-','-','-','-','-','-','-','-','-','-','-','-','-','-']]
        
    wells = []
    wells.append(['B4','C4','D4','E4','F4','G4','B2','B3','B7','C7','D7','E7','F7','G7','E2','E3','B5','C5','D5','E5','F5','G5','C2','C3','B6','C6','D6','E6','F6','G6','D2','D3']) 
    wells.append(['B8','C8','D8','E8','F8','G8','F2','F3','B11','C11','D11','E11','F11','G11','B9','C9','D9','E9','F9','G9','H2','H3','B10','C10','D10','E10','F10','G10']) 
    
            
    title_list = ['KLac','SCer']
    #Tracer()()
    for jj in range(len(title_list)):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #plt.show()    
    
    fname = "20160816_SC_KL_GD_after_break.csv"
    #Each column is a time point with 96 measurements. Rows are transposed into columns and stacked on top of one another from row A to H.  
    ntimes = 91
    nrows = 8
    ncols = 12
    starting_row = 'A'
    starting_col = 1
    
    OD_data, time_list = odl.get_OD_data(dirname,fname, ntimes, nrows, ncols,starting_row,starting_col)
    
    #Plot all wells raw OD
    wells = odl.all_wells(['B','C','D','E','F','G'],[2,3,4,5,6,7,8,9,10,11])
    well_arr = odl.well_array(wells)
    
    fig3 = odp.OD_plot_subplots(OD_data, well_arr, time_list,[])
    plt.show()
    
    
    #Average all traces together. 
    
    
   
    
    #To visualize fit on one well: 
    #Control Strain YPD
    xdata = time_list
    params0 = np.array([0.6, 0.01, 600.0, 0.1])
    
    ydata = OD_data.data[OD_data.index['B8']]
    popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
    ydata_fit = gc_fit.logistic_function(xdata,popt[0],popt[1],popt[2],popt[3])
    ydata_init = gc_fit.logistic_function(xdata,params0[0],params0[1],params0[2],params0[3])
        
    fig6= plt.figure()
    ax = fig6.add_subplot(111) 
    
    ax.scatter(xdata,ydata,color = 'k', marker = 'x', label = 'data')
    ax.plot(xdata,ydata_fit, color = 'b', label = 'fit parameters')
    ax.plot(xdata,ydata_init, color = 'r', label = 'initial parameters')
    
    legend = plt.legend(loc='upper left', fontsize='large')
    
    #To visualize fit on one well: 
    #Control Strain SDC
    xdata = time_list
    params0 = np.array([0.6, 0.01, 600.0, 0.1])
    
    ydata = OD_data.data[OD_data.index['D8']]
    popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
    ydata_fit = gc_fit.logistic_function(xdata,popt[0],popt[1],popt[2],popt[3])
    ydata_init = gc_fit.logistic_function(xdata,params0[0],params0[1],params0[2],params0[3])
        
    fig7= plt.figure()
    ax = fig7.add_subplot(111) 
    
    ax.scatter(xdata,ydata,color = 'k', marker = 'x', label = 'data')
    ax.plot(xdata,ydata_fit, color = 'b', label = 'fit parameters')
    ax.plot(xdata,ydata_init, color = 'r', label = 'initial parameters')
    
    legend = plt.legend(loc='upper left', fontsize='large')
    
    
    
    #Fit YPD plots and plot parameters
    layer_names = ['Strain', 'Media','NMPP1']
    col_list = ['L','k','x0','y0']
        
    strain_list = [[ '69 1 1','69 1 2', '69 2', '66', '70 1', '70 1 2','70 2','67','13', '29'],['YP', 'SC'],['-NMPP1','+NMPP1']]      
    data_index = pd.MultiIndex.from_product(strain_list, names= layer_names)
    layer_size = [len(layer_list) for layer_list in strain_list]
    growth_curve_df = pd.DataFrame(np.zeros([np.product(layer_size),len(col_list)]), index = data_index, columns = col_list)
    
    #set up well list to populate data in df in following steps.  [[YPD-, YPD+][SDC-, SDC+]]
    wells = {}
    wells[strain_list[0][0]] = [['B2','C2'],['D2','E2']]
    wells[strain_list[0][1]] = [['B10','C10'],['D10','E10']]
    wells[strain_list[0][2]] = [['B3','C3'],['D3','E3']]
    wells[strain_list[0][3]] = [['B6','C6'],['D6','E6']]
    wells[strain_list[0][4]] = [['B4','C4'],['D4','E4']]
    wells[strain_list[0][5]] = [['B11','C11'],['D11','E11']]
    wells[strain_list[0][6]] = [['B5','C5'],['D5','E5']]
    wells[strain_list[0][7]] = [['B7','C7'],['D7','E7']]
    wells[strain_list[0][8]] = [['B8','C8'],['D8','E8']]
    wells[strain_list[0][9]] = [['B9','C9'],['D9','E9']]
    
    params0 = np.array([0.6, 0.01, 600.0, 0.1])
    xdata = time_list
    
    for jj in range(len(strain_list[0])):
        for kk in range(len(strain_list[1])):
            for nn in range(len(strain_list[2])):
                ydata = OD_data.data[OD_data.index[wells[strain_list[0][jj]][kk][nn]]]
                popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['L'] = popt[0]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['k'] = popt[1]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['x0'] = popt[2]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['y0'] = popt[3]

    growth_curve_media_group = growth_curve_df.groupby( level = 'Media')
    growth_curve_df_YP_only = growth_curve_media_group.get_group('YP')
    
    fig8 = plt.figure()
    ax_bar_k = growth_curve_df_YP_only['k'].plot(kind='bar');
    fig8.tight_layout()
    fig8.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20151027_YP_k.png'))
    
    fig9 = plt.figure()
    ax_bar_L = growth_curve_df_YP_only['L'].plot(kind='bar');
    fig9.tight_layout()
    fig9.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20151027_YP_L.png'))
   
    fig10 = plt.figure()
    ax_bar_x0 = growth_curve_df_YP_only['x0'].plot(kind='bar');
    fig10.tight_layout()
    fig10.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20151027_YP_x0.png'))
    
    fig11 = plt.figure()
    ax_bar_y0 = growth_curve_df_YP_only['y0'].plot(kind='bar');
    fig11.tight_layout()
    fig11.savefig(os.path.abspath('C:\Users\Ben\Google Drive\UCSF\ElSamad_Lab\PKA\WetLab\Plate_reader\\20151027_YP_y0.png'))
    
    plt.show()
if __name__=="__main__":
    main()