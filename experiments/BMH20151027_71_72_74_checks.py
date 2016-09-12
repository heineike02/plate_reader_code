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
    fname = "20151027_KLTPK2AS_NMPP1_Post.csv"
    #Each column is a time point with 96 measurements. Rows are transposed into columns and stacked on top of one another from row A to H.  
    ntimes = 94
    nrows = 8
    ncols = 12
    starting_row = 'A'
    starting_col = 1
    
    OD_data, time_list = odl.get_OD_data(dirname,fname, ntimes, nrows, ncols,starting_row,starting_col)
    
    #Plot all wells raw OD
    wells = odl.all_wells(['B','C','D','E','F','G'],[2,3,4,5,6,7,8,9,10,11])
    well_arr = odl.well_array(wells)
    
    fig1 = odp.OD_plot_subplots(OD_data, well_arr, time_list,[])
    #plt.show()
    
    #Plot OD of 72, 74, 75 strains
    fig2, ax = plt.subplots()
    
    #legend_list = [[ '69 1 -', '69 2 -', '70 1 -','70 2 -','66 -','67 -','13 -', '29 -', '69 1 +', '69 2 +', '70 1 +','70 2 +','66 +','67 +','13 +', '29 +'],
    #[ '69 1 -', '69 2 -', '70 1 -','70 2 -','66 -','67 -','13 -', '29 -', '69 1 +', '69 2 +', '70 1 +','70 2 +','66 +','67 +','13 +', '29 +']]
    #color_list = [['m','m','r','r','m','r','k','b','m','m','r','r','m','r','k','b'],
    #['m','m','r','r','m','r','k','b','m','m','r','r','m','r','k','b']]
    #linestyle_list = [['-','--','-','--','-','-','-','-',':','_',':','_',':',':',':',':'],
    #['-','--','-','--','-','-','-','-',':','_',':','_',':',':',':',':']]
    
    legend_list = [ '71 1 1', '71 2 1', '71 3 1', '72 1 1', '72 2 1', '72 3 1', '74 1 1', '74 2 1', '74 3 1', '71 1 2', '71 2 2', '71 3 2', '72 1 2', '72 2 2', '72 3 2', '74 1 2', '74 2 2', '74 3 2', '13 1', '29 1', '13 2', '29 2']
    color_list = ['m','m','m', 'r','r','r', 'g','g', 'g','m','m','m', 'r','r','r', 'g','g', 'g','k','b','k','b']
    linestyle_list = ['-','--',':', '-','--', ':', '-','--', ':', '-','--', ':', '-','--', ':', '-','--', ':', '-','-', '--','--']
        
    wells = ['F2','F3','F4','F5','F6','F7','F8','F9','F10','G2','G3','G4','G5','G6','G7','G8','G9','G10','F11','G11','D8','D9']
    well_list = odl.well_array(wells)
    ax = plt.gca()
    odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list,linestyle_list,ax,legend_list)
    #[0,60,0.8,1.1]
    plt.show()    
    
    
    return
    #Plot OD of +/- NMPP1 strains 
    fig3, axarr = plt.subplots(2,1, sharex=True, sharey=True)
    
    #legend_list = [[ '69 1 -', '69 2 -', '70 1 -','70 2 -','66 -','67 -','13 -', '29 -', '69 1 +', '69 2 +', '70 1 +','70 2 +','66 +','67 +','13 +', '29 +'],
    #[ '69 1 -', '69 2 -', '70 1 -','70 2 -','66 -','67 -','13 -', '29 -', '69 1 +', '69 2 +', '70 1 +','70 2 +','66 +','67 +','13 +', '29 +']]
    #color_list = [['m','m','r','r','m','r','k','b','m','m','r','r','m','r','k','b'],
    #['m','m','r','r','m','r','k','b','m','m','r','r','m','r','k','b']]
    #linestyle_list = [['-','--','-','--','-','-','-','-',':','_',':','_',':',':',':',':'],
    #['-','--','-','--','-','-','-','-',':','_',':','_',':',':',':',':']]
    
    legend_list = [[ '70 1 -', '70 2 -', '70 1 +', '70 2 +'],
    [ '70 1 -', '70 2 -', '70 1 +', '70 2 +']]
    color_list = [['m','m','r','r'],
    ['m','m','r','r']]
    linestyle_list = [['-','--','-','--'],
    ['-','--','-','--']]
        
    wells = []
    #wells.append(['B2','B3','B4','B5','B6','B7','B8','B9','C2','C3','C4','C5','C6','C7','C8','C9']) 
    #wells.append(['D2','D3','D4','D5','D6','D7','D8','D9','E2','E3','E4','E5','E6','E7','E8','E9']) 
    
    wells.append(['B4','B5','C4','C5']) 
    wells.append(['D4','D5','E4','E5']) 
    
    
    title_list = ['YPD','SDC']
    #Tracer()()
    for jj in range(len(title_list)):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #[0,60,0.8,1.1]
    #plt.show()    
    
    #Plot OD of +/- NMPP1 strains 
    fig4, axarr = plt.subplots(2,1, sharex=True, sharey=True)
 
    legend_list = [[ '13 -', '29 -', '13 +', '29 +'],
    [ '13 -', '29 -', '13 +', '29 +']]
    color_list = [['k','k','b','b'],
    ['k','k','b','b']]
    linestyle_list = [['-','--','-','--'],
    ['-','--','-','--']]
    
    wells = []

    wells.append(['B8','B9','C8','C9']) 
    wells.append(['D8','D9','E8','E9']) 
    
    
    title_list = ['YPD','SDC']
    #Tracer()()
    for jj in range(len(title_list)):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #[0,60,0.8,1.1]
    #plt.show()    

    #Plot OD of +/- NMPP1 strains 
    fig5, axarr = plt.subplots(2,1, sharex=True, sharey=True)
    
    legend_list = [[ '69 1 1 -', '69 1 2 -', '66 -','69 1 1 +', '69 1 2 +', '66 +'],
    [ '69 1 1 -', '69 1 2 -', '66 -','69 1 1 +', '69 1 2 +', '66 +']]
    color_list = [['m','m','m','r','r','r'],
    ['m','m','m','r','r','r']]
    linestyle_list = [['-','--',':','-','--',':'],
    ['-','--',':','-','--',':']]
    
    wells = []
    wells.append(['B2','B10','B6','C2','C10','C6']) 
    wells.append(['D2','D10','D6','E2','E10','E6']) 
    
    
    title_list = ['YPD','SDC']
    #Tracer()()
    for jj in range(len(title_list)):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #[0,60,0.8,1.1]
    
    
    #Plot OD of +/- NMPP1 strains 
    fig6, axarr = plt.subplots(2,1, sharex=True, sharey=True)
    
    legend_list = [[ '70 1 1 -', '70 1 2 -', '67 -','70 1 1 +', '70 1 2 +', '66 +'],
    [ '70 1 1 -', '70 1 2 -', '67 -','70 1 1 +', '70 1 2 +', '67 +']]
    color_list = [['m','m','m','r','r','r'],
    ['m','m','m','r','r','r']]
    linestyle_list = [['-','--',':','-','--',':'],
    ['-','--',':','-','--',':']]
    
    wells = []
    wells.append(['B3','B11','B7','C3','C11','C7']) 
    wells.append(['D3','D11','D7','E3','E11','E7']) 
    
    
    title_list = ['YPD','SDC']
    #Tracer()()
    for jj in range(len(title_list)):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #[0,60,0.8,1.1]
    plt.show()   
    
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