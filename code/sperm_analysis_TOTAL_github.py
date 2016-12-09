import sys
import numpy as np
from numpy.random import *
from numpy.linalg import *
from math import *
from numpy.linalg import norm
from scipy import *
from scipy.io import *
from scipy import stats
import vtk
   

def write_Mean_Gaussian_curvature_single_cell(vtk_file=None,spermatids=None) :
    """
    Computes the local mean and gaussian curvatures of a vtk mesh.
    """
    if spermatids: 
        write_file = '../output/Observables_Curvature_Spermatids.dat'
        write_file_local_gauss = '../output/Gaussian_local_curv_Spermatids.dat'
        write_file_local_mean = '../output/Mean_local_curv_Spermatids.dat'
    else:
        write_file = '../output/Observables_Spermatozoa.dat'
        write_file_local_gauss = '../output/Gaussian_local_curv_Spermatozoa.dat'
        write_file_local_mean = '../output/Mean_local_curv_Spermatozoa.dat'

    
    file = open(write_file,'a')
    file_gauss = open(write_file_local_gauss,'w')
    file_mean = open(write_file_local_mean,'w')

    set_printoptions(threshold=np.inf)

    filename_upload = vtk_file
    mesh_name = vtk_file.split('.')[0]
    print filename_upload
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(filename_upload)
    reader.Update()   
    polydata = reader.GetOutput()
    sources = list()
    sources.append(polydata)
    sources.append(polydata)
    curvatures = list()        
    for idx in range(len(sources)):
        curvatures.append(vtk.vtkCurvatures())
    if idx % 2 == 0:
        curvatures[idx].SetCurvatureTypeToGaussian()
    else:
        curvatures[idx].SetCurvatureTypeToMean()

    for idx, item in enumerate(sources):
        
        curvatures[idx].SetInputData(sources[idx])
        curvatures[idx].Update() 
        
        writer_Mean = vtk.vtkXMLPolyDataWriter();
        writer_Gaussian = vtk.vtkXMLPolyDataWriter();
        writer_Mean.SetFileName('../output/Mean_curvature_'+mesh_name+'.vtp');
        writer_Gaussian.SetFileName('../output/Gaussian_curvature_'+mesh_name+'.vtp');
        
        writer_Gaussian.SetInputData(curvatures[0].GetOutput())
        writer_Mean.SetInputData(curvatures[1].GetOutput())
        writer_Gaussian.Write()
        writer_Mean.Write()
                                    

    Gaussian_curvature_array = array([curvatures[0].GetOutput().GetPointData().GetScalars().GetTuple1(k) for k in range(curvatures[0].GetOutput().GetNumberOfPoints())])
    Mean_curvature_array = array([curvatures[1].GetOutput().GetPointData().GetScalars().GetTuple1(k) for k in range(curvatures[1].GetOutput().GetNumberOfPoints())])
                                        
    s =   str(mean(Gaussian_curvature_array)) + ' ' + str(std(Gaussian_curvature_array)/mean(Gaussian_curvature_array)) + ' ' + str(mean(Mean_curvature_array)) + ' ' + str(std(Mean_curvature_array)/mean(Mean_curvature_array)) + '\n'
    file.write(s)
    s =   array_str(Gaussian_curvature_array) + ' ' +  str(reader.GetNumberOfPolys()) + '\n'
    file_gauss.write(s)
    s =   array_str(Mean_curvature_array) + ' ' + str(reader.GetNumberOfPolys()) + '\n'
    file_mean.write(s)       
        


def Kolmogorov_Smirnov_test() :

    whats = ['Surface','Volume','Real_Sphericity','Relative_Error_Gaussian_curvature','Relative_Error_Mean_curvature','Average_Mean_curvature','Average_Gaussian_curvature']

    print "Kolmogorov_Smirnov_test"

    for what in whats:
        osservabile_1 = array([])
        osservabile_2 = array([])
        filename_uploads_1 = '../output/' + what + '_Spermatids_cumulative_distribution.dat'
        filename_uploads_2 = '../output/' + what + '_Spermatozoa_cumulative_distribution.dat'
        write_file = '../output/' + what + '_Spermatozoa_vs_Spermatids_KS_test.dat'
        upload_1  = loadtxt(filename_uploads_1)
        for i in range(0,len(upload_1)):  
            osservabile_1 = append(upload_1[i][0], osservabile_1)
        upload_2  = loadtxt(filename_uploads_2)
        for i in range(0,len(upload_2)):  
            osservabile_2 = append(upload_2[i][0], osservabile_2)

        p=stats.ks_2samp(osservabile_1,osservabile_2)

        file=open(write_file,'w')
        s= what + ' Spermatozoa vs Spermatids' + '  KS test  '+str(p[1])+'\n'
        file.write(s)
        file.close

if __name__ == '__main__':
    
    example_input_mesh = "../data/Example_mesh.vtk"
    print "# Running code with example mesh: %s" % example_input_mesh
    write_Mean_Gaussian_curvature_single_cell(vtk_file=example_input_mesh,spermatids=True)
    #Kolmogorov_Smirnov_test() 




