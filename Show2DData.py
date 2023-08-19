## How to visualize a 2D uniform grid colored with the array attribute.
#############################################################################

## Import VTK
from vtk import *
#################################


## Load data
#######################################
reader = vtkXMLImageDataReader() # To read the image file .vti extension
reader.SetFileName('Data/Isabel_2D.vti') # Set the file which you want to read
reader.Update() # Update is important or else code will not run
data = reader.GetOutput() # Getting output of image in data variable

print(data)

## create a surface representation from 2D uniform grid data
surface = vtkGeometryFilter() # We use this filter to get the overall geometry of our dataset
surface.SetInputData(data) # Inputting our data in the filter
surface.Update() # Update is imp !!!

## Output of geometry filter is a vtkpolydata
pdata = surface.GetOutput() # Getting output of the filter in pdata variable
range = pdata.GetPointData().GetArray('Pressure').GetRange()
#GetPointData() # To get the info of points in the dataset
#GetArray('Pressure') # To get the pressure array from the points data
#GetRange()  # Will give us range (min, max)
print(range)

# create the scalar_bar
##########################
lut = vtkLookupTable()  # lookup table 
lut.Build() # Building a lookup table
scalar_bar = vtkScalarBarActor() # Created an actor of scalarbar
scalar_bar.SetLookupTable(lut) # Inserting the lookup table values in the scalarbar actor
scalar_bar.SetTitle("Pressure") # Setting the title of our scalar bar
scalar_bar.SetNumberOfLabels(6) # Setting up the number of lables in our scalar bar
scalar_bar.SetMaximumWidthInPixels(150) # Width of bar
scalar_bar.SetMaximumHeightInPixels(600) # Height of bar


### Setup mapper and actor
##########################
mapper = vtkPolyDataMapper() # Creating mapper of our polyData
mapper.SetInputData(pdata) # Inputting data in the mapper
mapper.SetScalarRange(range) # Setting up the range in the mapper
mapper.SetLookupTable(lut) # Setting up the look up table in the mapper
actor = vtkActor() # Created an actor
actor.SetMapper(mapper) # Setting the mapper to our actor

### Axes actor
###############
axes = vtkAxesActor() # Setting up axes actor
axes.SetTotalLength(50, 50, 50) # Length of axes in x, y and z direction
axes.AxisLabelsOff()  # Making label off


### Setup render window, renderer, and interactor
##################################################
renderer = vtkRenderer() # Making a renderer
renderer.SetBackground(0.5,0.5,0.5) # Color of background
render_window = vtkRenderWindow() # Making a render window
render_window.SetSize(1400,1000) # setting size of render window
render_window.AddRenderer(renderer) # Renderer is added in our render window
render_windowInteractor = vtkRenderWindowInteractor() # Making a rwi
render_windowInteractor.SetRenderWindow(render_window) # inputting rw into rwi
render_windowInteractor.SetInteractorStyle(vtkInteractorStyleTrackballCamera()) # Style
renderer.AddActor(actor) # Adding our actor into renderer
renderer.AddActor(axes) # Adding axes into renderer

## show the scalar bar
scalar_bar_widget = vtkScalarBarWidget() # Setting up widget
scalar_bar_widget.SetInteractor(render_windowInteractor) # Inputting scalar bar into rwi
scalar_bar_widget.SetScalarBarActor(scalar_bar) # Setting up scalar bar actor in our widget
scalar_bar_widget.On() # Making widget visible in our window


### Finally render the object
#############################
render_window.Render() # Rendering will start from here
render_windowInteractor.Start() # Interaction will start from here
