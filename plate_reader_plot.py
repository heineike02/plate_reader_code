import sys
import importlib
experiment_name = sys.argv[1]
assert not ' ' in experiment_name, 'input should be the filename without the .py extension'
assert not '.py' in experiment_name, 'do not include the .py extension'
#from experiments import BMH20150410_MSN2vMSN4 as experiment
experiment = importlib.import_module("plate_reader_code.experiments.%s" % experiment_name)
        
def main():
    #run the routine from the command line as follows.  
    #From the directory above the plate_reader_code directory
    #python -m plate_reader_code.plate_reader_plot <experiment filename>
    #e.g. python -m plate_reader_code.plate_reader_plot BMH20150410_MSN2vMSN4
    #
    #Can also run with magic run from enthought canopy command line but need to be in the 
    #directory above the plate_reader_code directory
    #e.g. %run C:/Users/Ben/Documents/GitHub/plate_reader_code/plate_reader_plot.py BMH20150410_MSN2vMSN4
    #
    # for editing, the following commands will allow changes in the files to be reloaded automatically
    # %load_ext autoreload
    # autoreload 2
    #
    # Make all changes for each experiment layout in the appropriate file in the /experiments folder
    experiment.main()
    

if __name__=="__main__":    
    main()
    