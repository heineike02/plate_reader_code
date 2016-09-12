import sys
from ..core import od_reader_data_load as odl
from ..core import od_reader_plot_functions as odp
from IPython.core.debugger import Tracer
from ..core import growth_curve_fit as gc_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix

def main():
    #Need to open data file and save as a .csv
    dirname = "C:/Users/Ben/Google Drive/UCSF/ElSamad_Lab/PKA/WetLab/Plate_reader/"
    fname = "20150410_MSN2vMSN4.csv"
    #Each column is a time point with 96 measurements. Rows are transposed into columns and stacked on top of one another from row A to H.  
    ntimes = 93
    nrows = 8
    ncols = 12
    starting_row = 'A'
    starting_col = 1
    
    OD_data, time_list = odl.get_OD_data(dirname,fname, ntimes, nrows, ncols,starting_row,starting_col)
    
    
    layer_names = ['Strain', 'Biol_Rep','Tech_Rep']
    col_list = ['L','k','x0','y0']
    
    strain_list = [['AS_M2_M4_46', 'AS_M2_M4dZF_47', 'AS_M2_WT_MS01', 'M2_M4_48', 'M2_M4dZF_49', 'M2_WT_HES11-38', 'M2_WT_OLD_SDC_HES11-38','WT_M4dZF_45', 'WT_WT_HES5-41'], ['BR1', 'BR2','BR3'],['TR1','TR2']]      
    data_index = pd.MultiIndex.from_product(strain_list, names= layer_names)
    layer_size = [len(layer_list) for layer_list in strain_list]
    growth_curve_df_1 = pd.DataFrame(np.zeros([np.product(layer_size),len(col_list)]), index = data_index, columns = col_list)
    
    #Only had one technical replicate for this strain
    strain_list_2 = [['WT_M4_44'],['BR1','BR2','BR3'],['TR1']]
    data_index_2 = pd.MultiIndex.from_product(strain_list_2, names= layer_names)
    layer_size = [len(layer_list) for layer_list in strain_list_2]
    growth_curve_df_2 = pd.DataFrame(np.zeros([np.product(layer_size),len(col_list)]), index = data_index_2, columns = col_list)
    
    growth_curve_df = pd.concat([growth_curve_df_1,growth_curve_df_2])
    
    #fig3, axarr = plt.subplots(2,2)
    wells = {}
    wells[strain_list[0][0]] = [['B2','C2'],['D2','E2'],['F2','G2']]
    wells[strain_list[0][1]] = [['B3','C3'],['D3','E3'],['F3','G3']]
    wells[strain_list[0][2]] = [['B9','C9'],['D9','E9'],['F9','G9']] 
    wells[strain_list[0][3]] = [['B4','C4'],['D4','E4'],['F4','G4']]
    wells[strain_list[0][4]] = [['B5','C5'],['D5','E5'],['F5','G5']]
    wells[strain_list[0][5]] = [['B10','C10'],['D10','E10'],['F10','G10']]
    wells[strain_list[0][6]] = [['B11','C11'],['D11','E11'],['F11','G11']]
    wells[strain_list[0][7]] = [['B7','C7'],['D7','E7'],['F7','G7']]
    wells[strain_list[0][8]] = [['B8','C8'],['D8','E8'],['F8','G8']] 
    wells[strain_list_2[0][0]] = [['B6'],['C6'],['D6']]

    params0 = np.array([0.6, 0.01, 600.0, 0.1])
    xdata = time_list
    
    #To visualize fit on one well: 
    ydata = OD_data.data[OD_data.index['B2']]
    popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
    ydata_fit = gc_fit.logistic_function(xdata,popt[0],popt[1],popt[2],popt[3])
    ydata_init = gc_fit.logistic_function(xdata,params0[0],params0[1],params0[2],params0[3])
    
    fig1 = plt.figure()
    ax = fig1.add_subplot(111) 
    
    ax.scatter(xdata,ydata,color = 'k', marker = 'x', label = 'data')
    ax.plot(xdata,ydata_fit, color = 'b', label = 'fit parameters')
    ax.plot(xdata,ydata_init, color = 'r', label = 'initial parameters')
    
    legend = plt.legend(loc='upper left', fontsize='large')
    
    #
    print params0
    print popt
    #
    plt.show()
    
        
    #Cycle through all wells and build up list of fitted parameters

    for jj in range(len(strain_list[0])):
        for kk in range(len(strain_list[1])):
            for nn in range(len(strain_list[2])):
                ydata = OD_data.data[OD_data.index[wells[strain_list[0][jj]][kk][nn]]]
                popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['L'] = popt[0]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['k'] = popt[1]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['x0'] = popt[2]
                growth_curve_df.loc[strain_list[0][jj],strain_list[1][kk],strain_list[2][nn]]['y0'] = popt[3]
        
    for jj in range(len(strain_list_2[0])):
        for kk in range(len(strain_list_2[1])):
            for nn in range(len(strain_list_2[2])):
                ydata = OD_data.data[OD_data.index[wells[strain_list_2[0][jj]][kk][nn]]]
                popt, pcov = gc_fit.growth_curve_fit(xdata,ydata,params0)
                growth_curve_df.loc[strain_list_2[0][jj],strain_list_2[1][kk],strain_list_2[2][nn]]['L'] = popt[0]
                growth_curve_df.loc[strain_list_2[0][jj],strain_list_2[1][kk],strain_list_2[2][nn]]['k'] = popt[1]
                growth_curve_df.loc[strain_list_2[0][jj],strain_list_2[1][kk],strain_list_2[2][nn]]['x0'] = popt[2]
                growth_curve_df.loc[strain_list_2[0][jj],strain_list_2[1][kk],strain_list_2[2][nn]]['y0'] = popt[3]
                    
    print growth_curve_df 
    
    
    #Figure 2 - plot a scatter matrix for all parameters. 
    ax = scatter_matrix(growth_curve_df, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()
    
    fig3 = plt.figure()
    #ax_bar_k = fig3.add_subplot(111)
    ax_bar_k = growth_curve_df['k'].plot(kind='bar');
    plt.show()
    
    fig4 = plt.figure()
    #ax_bar_k = fig3.add_subplot(111)
    ax_bar_L = growth_curve_df['L'].plot(kind='bar');
    plt.show()
    
    fig5 = plt.figure()
    #ax_bar_k = fig3.add_subplot(111)
    ax_bar_x0 = growth_curve_df['x0'].plot(kind='bar');
    plt.show()
    
    fig6 = plt.figure()
    #ax_bar_k = fig3.add_subplot(111)
    ax_bar_y0 = growth_curve_df['y0'].plot(kind='bar');
    plt.show()
    
    
    
        
    return
    Tracer()()
    #groups = growth_curve_df.groupby(level = 'Strain')
    groups = growth_curve_df.groupby(level = ('Strain','Biol_Rep'))
    #Can do groups.mean() or .std()
    
    # Plot
    plt.rcParams.update(pd.tools.plotting.mpl_stylesheet)
    colors = pd.tools.plotting._get_standard_colors(len(groups), color_type='random')

    fig, ax = plt.subplots()
    ax.set_color_cycle(colors)
    ax.margins(0.05)
    for name, group in groups:
        ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, label=name)
    ax.legend(numpoints=1, loc='upper left')

    plt.show()
    
    return
    
   
   
    
    
    #Plot selected wells in subplots
    #wells = [['B2','B3','B4'],['C2','C3','C4']]
    wells = odl.all_wells(['B','C','D','E','F','G'],[2,3,4,5,6,7,8,9,10,11])
    well_arr = odl.well_array(wells)
                  
    #wells = all_wells(['B','C','D','E','F','G'],[1,2,7,8])
    fig1 = odp.OD_plot_subplots(OD_data, well_arr, time_list,[])
    plt.show()
        
        
    #Plot in subplots, overlapping images.
    
    
    fig2, axarr = plt.subplots(3,1, sharex=True, sharey=True)
              
    legend_list = [[ '46_1_1', '46_1_2', '46_2_1','46_2_2','46_3_1','46_3_2','47_1_1', '47_1_2', '47_2_1','47_2_2','47_3_1','47_3_2','MS01_1_1', 'MS01_1_2', 'MS01_2_1','MS01_2_2','MS01_3_1','MS01_3_2'],
    [ '48_1_1', '48_1_2', '48_2_1','48_2_2','48_3_1','48_3_2','49_1_1', '49_1_2', '49_2_1','49_2_2','49_3_1','49_3_2','11_38_1_1', '11_38_1_2', '11_38_2_1','11_38_2_2','11_38_3_1','11_38_3_2','11_38_1_1 old SDC', '11_38_1_2 old SDC', '11_38_2_1 old SDC','11_38_2_2 old SDC','11_38_3_1 old SDC','11_38_3_2 old SDC'],
    [ '44_1', '44_2','44_3','45_1_1', '45_1_2', '45_2_1','45_2_2','45_3_1','45_3_2','5_41_1_1', '5_41_1_2', '5_41_2_1','5_41_2_2','5_41_3_1','5_41_3_2']]
    color_list = [['m','m','m','m','m','m','b','b','b','b','b','b','k','k','k','k','k','k','k'],
    ['m','m','m','m','m','m','b','b','b','b','b','b','k','k','k','k','k','k','k','g','g','g','g','g','g'],
    ['m','m','m','b','b','b','b','b','b','k','k','k','k','k','k','k']]
    linestyle_list = [['-','-','--','--',':',':','-','-','--','--',':',':','-','-','--','--',':',':'],
    ['-','-','--','--',':',':','-','-','--','--',':',':','-','-','--','--',':',':','-','-','--','--',':',':'],
    ['-','--',':','-','-','--','--',':',':','-','-','--','--',':',':']]
    
    wells = []
    wells.append(['B2','C2','D2','E2','F2','G2','B3','C3','D3','E3','F3','G3','B9','C9','D9','E9','F9','G9']) #MS01 based strains
    wells.append(['B4','C4','D4','E4','F4','G4','B5','C5','D5','E5','F5','G5','B10','C10','D10','E10','F10','G10','B11','C11','D11','E11','F11','G11']) #11-38 based strains
    wells.append(['B6','C6','D6','B7','C7','D7','E7','F7','G7','B8','C8','D8','E8','F8','G8']) #MS01 based strains
    
    title_list = ['MS01 based Strains', '11-38 based strains', '5-41 based strains']
    #Tracer()()
    for jj in range(3):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = odl.well_array(wells[jj])
            odp.OD_plot_sameplot(OD_data, well_list, time_list,color_list[jj],linestyle_list[jj],ax,legend_list[jj])
    #[0,60,0.8,1.1]
    plt.show()    
    
    
    
    #Plot parameters of the logistic curve fitted to the data. 
    
    
                    
    
    return
    fig3, axarr = plt.subplots(2,1, sharex=True, sharey=True)
              
    legend_list = [ 'Glu->Glu', 'Glu->Glu (No Spin)', '0.11M Sorb','0.11M Gly','0.11M Gal','no C source']
    color_list = ['b','b','g','c','m','k']
    linestyle_list = ['-','--','-','-','-','-']
    wells = []
    wells.append(['C5','G5','D5','E5','F5','B5']) #S.Cer Gluc Drop
    wells.append(['C10','G10','D10','E10','F10','B10']) #K.Lac Gluc Drop
    title_list = ['YP Media: S.Cer', 'YP Media: K.Lac']
    #Tracer()()
    for jj in range(2):
            ax = axarr[jj]   
            ax.set_title(title_list[jj])     
            well_list = well_array(wells[jj])
            OD_plot_sameplot(OD_data, well_list, time_list,color_list,linestyle_list,ax,legend_list)
    #[0,60,0.8,1.1]
    plt.show() 
    
    fig4, axarr = plt.subplots(2,3, sharex=True, sharey=True)
    array_map = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
                      
    legend_list_vec = []
    legend_list_vec.append(['Glu->Glu', 'Glu->Glu (No Spin)', '0.125M Sorb','0.25M Sorb', '0.5M Sorb','no C source'])
    legend_list_vec.append(['Glu->Glu', 'Glu->Glu (No Spin)','0.125M Glu', '0.25M Glu', '0.5M Glu','no C source'])
    legend_list_vec.append(['Glu->Glu', 'Glu->Glu (No Spin)', '0.125M Gly', '0.25M Gly', '0.5M Gly','no C source'])
    legend_list_vec = legend_list_vec + legend_list_vec
    
    color_list_vec = []
    color_list_vec.append(['b','b','g','g','g','k'])
    color_list_vec.append(['b','b','r','r','r','k'])
    color_list_vec.append(['b','b','c','c','c','k'])
    color_list_vec = color_list_vec + color_list_vec
    
    linestyle_list = ['-','--',':','--','-','-']

    wells = []
    wells.append(['C2','G2','B3','C3','D3','B2']) #S.Cer Sorb Osmo
    wells.append(['C2','G2','E3','F3','G3','B2']) #S.Cer Gluc Osmo
    wells.append(['C2','G2','B4','C4','D4','B2']) #S.Cer Gly Osmo

    wells.append(['C7','G7','B8','C8','D8','B7']) #K.Lac Sorb Osmo
    wells.append(['C7','G7','E8','F8','G8','B7']) #K.Lac Gluc Osmo
    wells.append(['C7','G7','B9','C9','D9','B7']) #K.Lac Gly Osmo
    title_list = ['SC Media: S.Cer Sorb','SC Media: S.Cer Gluc' ,'SC Media: S.Cer Gly','SC Media: K.Lac Sorb', 'SC Media: K.Lac Glu', 'SC Media: K.Lac Gly' ]
    #Tracer()()
    for jj in range(len(array_map)):
            ax = axarr[array_map[jj]]   
            ax.set_title(title_list[jj])     
            well_list = well_array(wells[jj])
            OD_plot_sameplot(OD_data, well_list, time_list,color_list_vec[jj],linestyle_list,ax,legend_list_vec[jj])
    #[0,60,0.8,1.1]
    plt.show() 
    
    
    fig5, axarr = plt.subplots(2,2, sharex=True, sharey=True)
    array_map = [(0,0),(0,1),(1,0),(1,1)]
                      
    legend_list_vec = []
    legend_list_vec.append(['Glu->Glu', 'Glu->Glu (No Spin)', '0.125M Sorb','0.25M Sorb', '0.5M Sorb','no C source'])
    legend_list_vec.append(['Glu->Glu', 'Glu->Glu (No Spin)','0.125M Glu', '0.25M Glu', '0.5M Glu','no C source'])
    legend_list_vec = legend_list_vec + legend_list_vec
    
    color_list_vec = []
    color_list_vec.append(['b','b','g','g','g','k'])
    color_list_vec.append(['b','b','r','r','r','k'])
    color_list_vec = color_list_vec + color_list_vec
    
    linestyle_list = ['-','--',':','--','-','-']

    wells = []
    wells.append(['C5','G5','B6','C6','D6','B5']) #S.Cer Sorb Osmo
    wells.append(['C5','G5','E6','F6','G6','B5']) #S.Cer Gluc Osmo

    wells.append(['C10','G10','B11','C11','D11','B10']) #K.Lac Sorb Osmo
    wells.append(['C10','G10','E11','F11','G11','B10']) #K.Lac Gluc Osmo
    
    title_list = ['YP Media: S.Cer Sorb','YP Media: S.Cer Gluc' ,'YP Media: K.Lac Sorb', 'YP Media: K.Lac Glu']
    #Tracer()()
    for jj in range(len(array_map)):
            ax = axarr[array_map[jj]]   
            ax.set_title(title_list[jj])     
            well_list = well_array(wells[jj])
            OD_plot_sameplot(OD_data, well_list, time_list,color_list_vec[jj],linestyle_list,ax,legend_list_vec[jj])
    #[0,60,0.8,1.1]
    plt.show() 
    
    
    
    
    
    return
    
    #Plot in subplots, overlapping images.
    fig2, axarr = plt.subplots(2,2, sharex=True, sharey=True)
    array_map = [(0,0),(0,1),(1,0),(1,1)]
    
    legend_list_osmo = [ 'Glu->Glu', 'Glu->Glu (no Spin)', 'Glu->2%% Glu + 0.5M Glu 1','Glu->2%% Glu + 0.5M Glu 2','Glu->2%% Glu + 0.5M Sorb 1','Glu->2%% Glu + 0.5M Sorb 2','Glu->2%% Glu + 0.25M NaCl 1', 'Glu->2%% Glu + 0.25M NaCl 2']
    
    legend_list_GD = [ 'Glu->Glu', 'Glu->Glu (no Spin)' ,'Glu->nothing','Glu->0.11M Sorb','Glu->0.11M Gly','Glu-> 2%%Gal','Glu->0.056M Lac','Glu->0.056M NaCl']
    
    wells = []
    wells.append(['B10','G9','B11','C11','D11','E11','F11','G11']) #S.Cer Gluc Drop
    wells.append(['B10','G9','D10','F9','C10','E9','E10','F10']) #S.Cer Osmo
    wells.append(['B5','G4','B6','C6','D6','E6','F6','G6']) #K.Lac Gluc Drop
    wells.append(['B5','G4','D5','F4','C5','E4','E5','F5']) #K.Lac Osmo
    title_list = ['S.Cer Gluc Drop','S.Cer Osmo', 'K.Lac Gluc Drop', 'K.Lac Osmo']
    legend_list_vec = [legend_list_GD,legend_list_osmo,legend_list_GD,legend_list_osmo]
    for jj in range(len(array_map)):
            ax = axarr[array_map[jj]]   
            ax.set_title(title_list[jj])     
            well_list = well_array(wells[jj])
            color_list = [[0.0,1.0,1.0]]
            legend_list = legend_list_vec[jj]
            OD_plot_sameplot(OD_data, well_list, time_list,color_list,ax,legend_list)
    #[0,60,0.8,1.1]
    plt.show()
    
    sys.exit()
    Tracer()()
    

    
        #Plot in subplots, overlapping images.
    fig4, axarr = plt.subplots(2,2, sharex=True, sharey=True)
    array_map = [(0,0),(0,1),(1,0),(1,1)]
    
    legend_list = [ 'Glu->Glu', 'Glu->0.11M Sorb','Glu->0.11M Gly','Glu->Gal','Glu->No Glu','Glu->0.056M Lac']

    wells = all_wells(['B','C','D','E','F','G'],[4,5,8,10])
    title_list = ['S.Cer 37','S.Cer 42', 'K.Lac 13a', 'K.Lac 39']
    #Tracer()()
    for jj in range(4):
            ax = axarr[array_map[jj]]   
            ax.set_title(title_list[jj])     
            wells_jj = [well_row[jj] for well_row in wells]
            well_list = well_array(wells_jj)
            color_list = [[0.0,1.0,1.0]]
            OD_plot_sameplot(OD_data, well_list, time_list,color_list,ax,legend_list)
    #[0,60,0.8,1.1]
    plt.show()
    
    fig5, axarr = plt.subplots(2,2, sharex=True, sharey=True)
    array_map = [(0,0),(0,1),(1,0),(1,1)]
    
    legend_dict = {'YP': [ 'Glu->Glu', 'Glu->0.11M Sorb','Glu->0.11M Gly','Glu->Gal','Glu->No Glu','Glu->0.056M Lac'],
                   'SC': [ 'Glu->Glu', 'Glu->0.11M Sorb','Glu->0.11M Gly','Glu->Gal','Glu->0.11M Lac','Glu->0.056M Lac']}
    legend_order = ['SC','YP','SC','YP']
    
    wells = all_wells(['B','C','D','E','F','G'],[3,5,7,9])
    title_list = ['S.Cer SC Media','S.Cer YP Media', 'K.Lac SC Media', 'K.Lac YP Media']
    #Tracer()()
    for jj in range(4):
            ax = axarr[array_map[jj]]   
            ax.set_title(title_list[jj])     
            wells_jj = [well_row[jj] for well_row in wells]
            well_list = well_array(wells_jj)
            legend_list = legend_dict[legend_order[jj]]
            color_list = [[0.0,1.0,1.0]]
            OD_plot_sameplot(OD_data, well_list, time_list,color_list,ax,legend_list)
    #[0,60,0.8,1.1]
    plt.show()
    
if __name__=="__main__":
    main()