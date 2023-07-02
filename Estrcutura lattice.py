# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:58:18 2023

@author: ALEJANDRO FERNANDEZ ARELLANO
"""

# Save by alex2 on 2023_02_16-09.20.14; build 2019 2018_09_24-20.41.51 157541
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

'Variables'
import math
#Altura
h = 20.0
#longitud
l = 30.0
#Parametros de la estrutura
w = 2.5
u = 2.5
t = 2.5
#Angulo
s =45.0
s1= float(s)
s2=math.radians(s1)
r=math.tan(s2)
#profundidad
profundidad=2.0
#Altura 1
y1=(h/2)-w
x1=y1/r
#Altura 2
y2=(h/2)-w-(t/2)
x2=y2/r
#Dimensiones de la celda
ejex=2
ejey=2
ejez=2
#Mallado
mallado=5.0
#Fuerza
F=40.0
deformacion=(h+(h-w)*(ejey-1))*0.1
b=3*l-2*(x2+u)

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Part
#-----------------------------------------------------------------------------------------------------------------------------
#Part X1

#Crear Un Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Rectangulo abajo
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(l, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, 0.0), point2=(l, w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, w), point2=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u, w), point2=(l-u, w))

#Barra1_izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,w), point2=(x2+u, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)-(t/2)), point2=(x2+u, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)+(t/2)), point2=(u, h-w))

#Barra2_Izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, w), point2=(x1, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x1,h/2), point2=(0.0, h-w))

#Rectangulo arriba
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, h-w), point2=(0.0, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,h ), point2=(l, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, h), point2=(l, h-w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,  h-w), point2=( l-u,  h-w))

#Barra_Derecha
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u, w), point2=(l-u-x2, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)-(t/2)), point2=(l-u-x2, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)+(t/2)), point2=(l-u, h-w))

#Barra_derecha2
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, h-w))

#Profundidad
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='X1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['X1'].BaseSolidExtrude(depth=profundidad, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#Part X2
#Crear un Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Rectangulo abajo
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(l, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, 0.0), point2=(l, profundidad))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, profundidad), point2=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u, profundidad), point2=(l-u, profundidad))

#Barra1_izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,profundidad), point2=(x2+u, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)-(t/2)), point2=(x2+u, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)+(t/2)), point2=(u, h-profundidad))

#Barra2_Izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, profundidad), point2=(x1, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x1,h/2), point2=(0.0, h-profundidad))

#Rectangulo arriba
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, h-profundidad), point2=(0.0, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,h ), point2=(l, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, h), point2=(l, h-profundidad))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,  h-profundidad), point2=( l-u,  h-profundidad))

#Barra_Derecha
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u, profundidad), point2=(l-u-x2, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)-(t/2)), point2=(l-u-x2, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)+(t/2)), point2=(l-u, h-profundidad))

#Barra_derecha2
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, profundidad))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, h-profundidad))

#Profundidad
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='X2', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['X2'].BaseSolidExtrude(depth=w, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Assembly
#-----------------------------------------------------------------------------------------------------------------------------

#Union de las estructuras X

#Creador de las 4 X
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X-1', part=mdb.models['Model-1'].parts['X1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X-2', part=mdb.models['Model-1'].parts['X2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X-3', part=mdb.models['Model-1'].parts['X2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X-4', part=mdb.models['Model-1'].parts['X1'])

#Posicionamiento
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=-90.0, axisDirection=(10.0,0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('X-2', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=-90.0, axisDirection=(10.0,0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('X-3', ))
#Movimiento
mdb.models['Model-1'].rootAssembly.translate(instanceList=('X-2', ), vector=(0.0, 0.0, profundidad))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('X-3', ), vector=(0.0, h-w , profundidad))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('X-4', ), vector=(0.0, 0.0, -h+profundidad))

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Part
#-----------------------------------------------------------------------------------------------------------------------------

#Creador de la estructura Barras con w
#Crear el Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Barra 1
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.0, w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, w), point2=(h, h*r+w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(h, h*r+w),point2=(h, h*r))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(h, h*r),point2=(0.0, 0.0))

#Profundidad=t
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Barra_inclinada1', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Barra_inclinada1'].BaseSolidExtrude(depth=t, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#Creador de barras inclinadas con profundidad
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Barra 2
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.0, profundidad))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, profundidad), point2=(h, h*r+profundidad))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(h, h*r+profundidad),point2=(h, h*r))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(h, h*r),point2=(0.0, 0.0))

#Profundidad=t
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Barra_inclinada2', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Barra_inclinada2'].BaseSolidExtrude(depth=t, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Assembly
#-----------------------------------------------------------------------------------------------------------------------------

#Creador de barras
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-1', part=mdb.models['Model-1'].parts['Barra_inclinada1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-2', part=mdb.models['Model-1'].parts['Barra_inclinada1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-3', part=mdb.models['Model-1'].parts['Barra_inclinada2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-4', part=mdb.models['Model-1'].parts['Barra_inclinada2'])

#Barra 1 
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-1',), vector=(l-u-x2, 0.0, -1*(h/2+t/2-profundidad)))

#Barra 2 
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=270.0, axisDirection=(0.0, 0.0,10.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-2', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 0.0,10.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-2', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=180.0, axisDirection=(0.0,10.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-2',))
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-2',), vector=(l, -1*((h*r)+w), 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-2',), vector=(h-u-x2, h, -1*(h/2-t/2-profundidad)))

#Barra 3
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0,0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-3', ))
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-3',), vector=(l-u-x2, h/2+t/2, -1*(h-profundidad)))

#Barra 4
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=-90.0, axisDirection=(10.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-4', ))
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-4', ), vector=(l-u-x2, h/2-t/2, profundidad))

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Copia de las barras en la parte de la derecha 
#Crear 4 barras 
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-5', part=mdb.models['Model-1'].parts['Barra_inclinada1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-6', part=mdb.models['Model-1'].parts['Barra_inclinada1'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-7', part=mdb.models['Model-1'].parts['Barra_inclinada2'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Barra_inclinada-8', part=mdb.models['Model-1'].parts['Barra_inclinada2'])

#Barra 5
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-5',), vector=(-1*h, -1*((h*r)+w), 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-5',), vector=(x2+u, h, -1*(h/2+t/2-profundidad)))

#Barra 6
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=180.0, axisDirection=(0.0,10.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-6', ))
#Movimeto
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-6', ), vector=(x2+u, 0.0, -1*(h/2-t/2-profundidad)))

#Barra 8
#Roatar
mdb.models['Model-1'].rootAssembly.rotate(angle=-90.0, axisDirection=(10.0, 0.0, 0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-8', ))
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-8', ), vector=(-1*h, -t,  h*r+profundidad))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-8', ), vector=(x2+u, h/2+t/2, -1*(h-profundidad)))


#Barra 7
#Rotar
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(10.0, 0.0,0.0), axisPoint=(0.0, 0.0, 0.0), instanceList=('Barra_inclinada-7', ))
#Mover
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-7',), vector=(-1*h, 0.0, -1*(h*r+profundidad)))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Barra_inclinada-7',), vector=(x2+u, h/2+t/2, profundidad))

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Assembly Celda unidad
#-----------------------------------------------------------------------------------------------------------------------------

#Creacion de la celda unidad

mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['X-1'], 
    mdb.models['Model-1'].rootAssembly.instances['X-2'], 
    mdb.models['Model-1'].rootAssembly.instances['X-3'], 
    mdb.models['Model-1'].rootAssembly.instances['X-4'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-2'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-3'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-4'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-5'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-6'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-7'], 
    mdb.models['Model-1'].rootAssembly.instances['Barra_inclinada-8']), name=
    'Celda unidad', originalInstances=SUPPRESS)
    
    
#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Part
#-----------------------------------------------------------------------------------------------------------------------------   
    
#Planos de corte en la figura

#Primer plano de corte
    
#Definir plano    
plano_punto=(l/2,0, profundidad)    
plano=mdb.models['Model-1'].parts['Celda unidad'].faces.findAt(plano_punto,)
#Definir eje
eje_punto=(l,h-w/2,0)
eje=mdb.models['Model-1'].parts['Celda unidad'].edges.findAt(eje_punto,)

#Corte
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=4.94, name='__profile__', 
    sheetSize=197.98, transform=
    mdb.models['Model-1'].parts['Celda unidad'].MakeSketchTransform(
    
    sketchPlane=plano, 
    
    sketchPlaneSide=SIDE1, 
    
    sketchUpEdge=eje, 
    
    sketchOrientation=RIGHT, 
    origin=(l/2, h/2, profundidad)))



#Se crea un part en 2D para hacer el plano que se quiere hacer
mdb.models['Model-1'].parts['Celda unidad'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])

#Rectangulo de arriba
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2, (h/2-w)), point2=
    (l/2, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, h/2), 
    point2=(l/2, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, h/2), 
    point2=(-l/2, h/2-w))

#La parte del medio Izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, (h/2-w)), 
    point2=(-l/2, h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, h/4), 
    point2=(-(l/2)+0.4, h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-(l/2)+0.4, 
    h/4), point2=(-(l/2)+0.4, r*2.3))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-(l/2)+0.4, 
    r*2.3), point2=(-(l/2)+0.4, -r*2.3))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-(l/2)+0.4, 
    -r*2.3), point2=(-(l/2)+0.4, -h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, -(h/2-w)), 
    point2=(-l/2, -h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, -h/4), 
    point2=(-(l/2)+0.4, -h/4))

#Rectangulo de abajo
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, -(h/2-w)), 
    point2=(-l/2, - h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2, -h/2), 
    point2=(l/2, -(h/2-w)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-l/2, -h/2), 
    point2=(l/2, -h/2))

#La parte del medio Derecha
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2, -(h/2-w)), 
    point2=(l/2, -h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2, 
    -h/4), point2=(l/2-0.4, -h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2-0.4, 
    -h/4), point2=(l/2-0.4, -r*2.3))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2-0.4, 
    -r*2.3), point2=(l/2-0.4, r*2.3))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2-0.4, 
    r*2.3), point2=(l/2-0.4, h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2-0.4, 
    h/4), point2=(l/2, h/4))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l/2, h/2-w), point2=
    (l/2, h/4))

#Rectangulo exterior

mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-l*2, h*2), 
    point2=(l*2, -h*2))

#Profundidad del corte
mdb.models['Model-1'].parts['Celda unidad'].CutExtrude(flipExtrudeDirection=OFF
    , 
    sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=RIGHT, 
    sketchPlane=plano, 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=eje)
del mdb.models['Model-1'].sketches['__profile__']

#------------------------------------------------------------------------------------------------------------------------------
#Segundo plano de corte

#Definir los puntos del plano y eje 
plano_punto2=(l/2,w/2, profundidad)    
plano2=mdb.models['Model-1'].parts['Celda unidad'].faces.findAt(plano_punto2,)
 
eje_punto2=(0,w/2,profundidad)
eje2=mdb.models['Model-1'].parts['Celda unidad'].edges.findAt(eje_punto2,)

#Creas un modulo Part
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=5.0, name='__profile__', 
    sheetSize=200.0, transform=
    mdb.models['Model-1'].parts['Celda unidad'].MakeSketchTransform(
    sketchPlane=plano2,
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=eje2, 
    sketchOrientation=RIGHT,
    origin=(l/2, h/2, -profundidad)))

#Rectangulo interior 
mdb.models['Model-1'].parts['Celda unidad'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-l/2, h/2), 
    point2=(l/2, -h/2))

#Rectangulo exterior
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-l*2, 
    h*2), point2=(l*2, -h*2))

#Profundidad del corte
mdb.models['Model-1'].parts['Celda unidad'].CutExtrude(flipExtrudeDirection=ON, 
    sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=RIGHT,
    sketchPlane=plano2, 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=eje2)
del mdb.models['Model-1'].sketches['__profile__']

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Part
#-----------------------------------------------------------------------------------------------------------------------------   

#Part X3

#Crear un Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)

#Rectangulo abajo
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(l, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, 0.0), point2=(l, t))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, t), point2=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u, t), point2=(l-u, t))

#Barra1_izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,t), point2=(x2+u, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)-(t/2)), point2=(x2+u, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u, (h/2)+(t/2)), point2=(u, h-t-w+t))


#Barra2_Izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, t), point2=(x1, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x1,h/2), point2=(0.0, h-t-w+t))

#Rectangulo arriba
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, h-t-w+t), point2=(0.0, h-w+t))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,h-w+t ), point2=(l, h-w+t))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, h-w+t), point2=(l, h-t-w+t))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,  h-t-w+t), point2=( l-u,  h-t-w+t))


#Barra_Derecha
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u, t), point2=(l-u-x2, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)-(t/2)), point2=(l-u-x2, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2, (h/2)+(t/2)), point2=(l-u, h-t-w+t))


#Barra_derecha2
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, t))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, h-t-w+t))

#Profundidad
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='X3', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['X3'].BaseSolidExtrude(depth=profundidad, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


#-----------------------------------------------------------------------------------------------------------------------------
#Part X4

#Crear un Part
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)


#Rectangulo abajo
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(l, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, 0.0), point2=(l, w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, w), point2=(0.0, 0.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u, w), point2=(l-u, w))

#Barra1_izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,w), point2=(x2+u-0.4, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u-0.4, (h/2)-(t/2)), point2=(x2+u-0.4, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x2+u-0.4, (h/2)+(t/2)), point2=(u, h-w))


#Barra2_Izquierda
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, w), point2=(x1, h/2))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(x1,h/2), point2=(0.0, h-w))

#Rectangulo arriba
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, h-w), point2=(0.0, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0,h ), point2=(l, h))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l, h), point2=(l, h-w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(u,  h-w), point2=( l-u,  h-w))


#Barra_Derecha
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u, w), point2=(l-u-x2+0.4, (h/2)-(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2+0.4, (h/2)-(t/2)), point2=(l-u-x2+0.4, (h/2)+(t/2)))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-u-x2+0.4, (h/2)+(t/2)), point2=(l-u, h-w))


#Barra_derecha2
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, w))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(l-x1, h/2), point2=(l, h-w))

#Profundidad
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='X4', type=DEFORMABLE_BODY)
mdb.models['Model-1'].parts['X4'].BaseSolidExtrude(depth=profundidad+t-profundidad, sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Assembly
#-----------------------------------------------------------------------------------------------------------------------------  


#Dimension de la celda

lista_de_celdas=[]

for i in range(ejex):
    for j in range(ejey):
        for k in range (ejez):
            mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)    
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,name='Celda unidad-1'+str(i)+str(j)+str(k),
                                  part=mdb.models['Model-1'].parts['Celda unidad'])
            
            mdb.models['Model-1'].rootAssembly.translate(instanceList=('Celda unidad-1'+str(i)+str(j)+str(k),), vector=((((l+(l-u-x2)-(x2+u))*i), ((h-w)*j), ((h-profundidad)*(k+1)))))    
            lista_de_celdas.append('Celda unidad-1'+str(i)+str(j)+str(k))
            
#Barra del medio

for k in range (ejez+1):
    for j in range(ejey-1):
        for i in range(ejex-1):
            mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN) 
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X'+str(i)+str(j)+str(k)+str(k), 
                      part=mdb.models['Model-1'].parts['X3'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=('X'+str(i)+str(j)+str(k)+str(k),), 
                       vector=(((l-u-x2)+((i)*(l+l-u-x2-u-x2))), ((h/2)-(t/2)+(j*(h-w))), ((h-profundidad)*k)))    
            lista_de_celdas.append('X'+str(i)+str(j)+str(k)+str(k))
    

#Barra del exterior
 
for k in range (ejez):
    for j in range(ejey):
        for i in range(ejex-1):
            mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN) 
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='X'+str(-10*i)+str(k)+str(j), 
                      part=mdb.models['Model-1'].parts['X4'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=('X'+str(-10*i)+str(k)+str(j),), 
                       vector=(((l-u-x2)+(i*(l+l-u-x2-u-x2))), ((h-w)*j), ((h/2)-(t/2)+(k*(h-profundidad)))))    
            lista_de_celdas.append('X'+str(-10*i)+str(k)+str(j))
            
#Celda prueba Union en un solido

mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY,  
instances= ([mdb.models['Model-1'].rootAssembly.instances[lista_de_celdas[n]] for n 
in range (len(lista_de_celdas))]),name='celda prueba', originalInstances=SUPPRESS)
    
#Hay una celda que se repite hay que borrarla 
del mdb.models['Model-1'].rootAssembly.features['Celda unidad-1']

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Mesh
#-----------------------------------------------------------------------------------------------------------------------------  

#Mallado

mdb.models['Model-1'].parts['celda prueba'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=mallado)
mdb.models['Model-1'].parts['celda prueba'].setMeshControls(elemShape=TET, 
    regions=
    mdb.models['Model-1'].parts['celda prueba'].cells.getSequenceFromMask((
    '[#1 ]', ), ), technique=FREE)
mdb.models['Model-1'].parts['celda prueba'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(
    mdb.models['Model-1'].parts['celda prueba'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Model-1'].parts['celda prueba'].generateMesh()

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Assembly
#-----------------------------------------------------------------------------------------------------------------------------  

#Creacion de 2 sets

#Defirnir el set 1
#Punto del plano
Punto_Plano_de_arriba=(l/2,h+(h-w)*(ejey-1), profundidad/2)
Punto_Plano_de_arriba2=(l/2,h+(h-w)*(ejey-1), profundidad/2)

#Defirnir el set 2
#Punto del plano
Punto_Plano_de_abajo=(l/2,0, profundidad/2)
#Definir el plano
Plano_de_arriba=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].faces.findAt((Punto_Plano_de_arriba,))
Plano_de_arriba2=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].faces.findAt((Punto_Plano_de_arriba2,))

#Definir el plano
Plano_de_abajo=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].faces.findAt((Punto_Plano_de_abajo,))

#Confirmar el plano
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set(faces=
    Plano_de_arriba, name='Parte de arriba')
mdb.models['Model-1'].rootAssembly.Set(faces=
    Plano_de_abajo, name='Parte de abajo')
mdb.models['Model-1'].rootAssembly.Set(faces=
    Plano_de_arriba, name='Parte de arriba2')


Empotramineto1=(0,0,0)
Empotramineto2=(l+(l-x2-u)*ejex,0,0)
Empotramineto3=(0,0,h*ejez-profundidad*(ejez-1))
Empotramineto4=(l+(l-x2-u)*ejex,0,h*ejez-profundidad*(ejez-1))

Empotramineto11=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].vertices.findAt((Empotramineto1,))
Empotramineto22=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].vertices.findAt((Empotramineto2,))
Empotramineto33=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].vertices.findAt((Empotramineto3,))
Empotramineto44=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].vertices.findAt((Empotramineto4,))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set( 
          vertices=Empotramineto11,name='Set-4')
mdb.models['Model-1'].rootAssembly.Set( 
          vertices=Empotramineto22,name='Set-5')
mdb.models['Model-1'].rootAssembly.Set( 
          vertices=Empotramineto33,name='Set-6')
mdb.models['Model-1'].rootAssembly.Set( 
          vertices=Empotramineto44,name='Set-7')



#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Property
#-----------------------------------------------------------------------------------------------------------------------------  

#Material
mdb.models['Model-1'].Material(name='ABS')
mdb.models['Model-1'].materials['ABS'].Elastic(table=((862.0, 0.35), ))
mdb.models['Model-1'].materials['ABS'].Plastic(table=((33.3, 0.0), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='ABS', name='Section-1', 
    thickness=None)
mdb.models['Model-1'].parts['celda prueba'].Set(cells=
    mdb.models['Model-1'].parts['celda prueba'].cells.getSequenceFromMask((
    '[#1 ]', ), ), name='Set-3')
mdb.models['Model-1'].parts['celda prueba'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['celda prueba'].sets['Set-3'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Load
#-----------------------------------------------------------------------------------------------------------------------------  

#Condiciones de contorno
#Crear las condiciones
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].StaticStep(name='CargaPaso', previous='Initial')
mdb.models['Model-1'].HistoryOutputRequest(createStepName='CargaPaso', name=
    'H-Output-2', variables=PRESELECT)



#Definir las condiciones
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='YBaseFixed', 
    region=mdb.models['Model-1'].rootAssembly.sets['Parte de abajo'], u1=UNSET, 
    u2=SET, u3=UNSET, ur1=SET, ur2=UNSET, ur3=SET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name=
    'Carga_de_compresion', region=
    mdb.models['Model-1'].rootAssembly.sets['Parte de arriba'], u1=UNSET, u2=
    SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
del mdb.models['Model-1'].boundaryConditions['Carga_de_compresion']
mdb.models['Model-1'].boundaryConditions['YBaseFixed'].setValuesInStep(
    stepName='CargaPaso', ur1=FREED, ur3=FREED)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'CargaPaso', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-8', region=mdb.models['Model-1'].rootAssembly.sets['Set-4'], 
    u1=UNSET, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'CargaPaso', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-9', region=mdb.models['Model-1'].rootAssembly.sets['Set-5'], 
    u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'CargaPaso', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-10', region=mdb.models['Model-1'].rootAssembly.sets['Set-6'], 
    u1=UNSET, u2=0.0, u3=UNSET, ur1=0.0, ur2=0.0, ur3=0.0)
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-7', region=mdb.models['Model-1'].rootAssembly.sets['Set-7'])
#Modulo de la carga


mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'CargaPaso', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-3', region=mdb.models['Model-1'].rootAssembly.sets['Parte de arriba2'], 
    u1=UNSET, u2=1.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['BC-3'].setValues(u2=-deformacion)


#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Step
#-----------------------------------------------------------------------------------------------------------------------------  


#Step

mdb.models['Model-1'].steps['CargaPaso'].setValues(initialInc=0.01, maxInc=0.1, 
    maxNumInc=10000, nlgeom=ON)

#Reference Point
mdb.models['Model-1'].parts['celda prueba'].ReferencePoint(point=(-10.0, h*ejey-profundidad*(ejey-1), 
    h*ejez-profundidad*(ejez-1)))
mdb.models['Model-1'].rootAssembly.regenerate()
Puntodereferencia=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].referencePoints.findAt((-10.0, h*ejey-profundidad*(ejey-1), 
    h*ejez-profundidad*(ejez-1),)) 
mdb.models['Model-1'].rootAssembly.Set(name='RP', referencePoints=(Puntodereferencia,))

#Interation
mdb.models['Model-1'].Equation(name='Constraint-1', terms=((1.0, 
    'Parte de arriba', 2), (-1.0, 'RP', 2)))
#Deformacion
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName=
    'CargaPaso', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=
    None, name='BC-11', region=mdb.models['Model-1'].rootAssembly.sets['RP']
    , u1=UNSET, u2=-deformacion, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['BC-3'].suppress()


#Punto del plano
Punto_Plano_de_lateral=(x2+u,h+(h/2-w)*(ejey-1), h+(-profundidad+h-profundidad/2)*(ejez-1))
#Definir el plano
Plano_de_lateral2=mdb.models['Model-1'].rootAssembly.instances['celda prueba-1'].faces.findAt((Punto_Plano_de_lateral,))
#Confirmar el plano
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.Set(faces=
    Plano_de_lateral2, name='Parte lateral')

mdb.models['Model-1'].HistoryOutputRequest(createStepName='CargaPaso', name=
    'H-Output-3', rebar=EXCLUDE, region=
    mdb.models['Model-1'].rootAssembly.sets['Parte lateral'], sectionPoints=
    DEFAULT, variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3'))
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(rebar=
    EXCLUDE, region=mdb.models['Model-1'].rootAssembly.sets['RP']
    , sectionPoints=DEFAULT, variables=('RT', 'TF1', 'TF2', 'TF3', 'TM1', 
    'TM2', 'TM3', 'NFORC','U1','U2','U3','UR1','UR2','UR3'))

#-----------------------------------------------------------------------------------------------------------------------------
#Modulo Job
#-----------------------------------------------------------------------------------------------------------------------------  

#Job
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
