from visual import *

CAMERA_ROTATE = False
MAKE_TRAIL = True

#frame setting
scene = display(title='Bead Dynamics', x=0, y=0)
scene.width = 1200
scene.height = 1200
scene.background = (0, 0, 0)
scale = 0.5
scene.scale = (scale, scale, scale)
scene.autoscale = False


# constants
g = 9.81

step_power = 3.5
dt = 10**(-step_power)
speed = 0.6*10**step_power


# physical parameters
omega = 3
R = 1
mu = 0.1

theta = 1
dtheta = 7

phi = pi/2


# visual parameters (irrelevant to motion)
bead_rad = 0.1
ring_thk = 0.01*R
axis_length = 2.4*R
axis_thk = 0.015


# visual object creation
ring = ring(pos=(0, 0, 0), axis=(cos(phi), 0, sin(phi)), radius=R, thickness=ring_thk, color=(0.5, 0.5, 0.5))
bead = sphere(pos=(R*sin(theta)*sin(phi), -R*cos(theta), -R*sin(theta)*cos(phi)), radius=bead_rad, color=color.red, make_trail=MAKE_TRAIL)
axis = cylinder(pos=(0, -axis_length/2, 0), axis=(0, axis_length, 0), radius=axis_thk)



while True:
    # calculations
    ddtheta = ((omega**2*cos(theta)/R) - (g/(R**2)))*sin(theta)
    f = mu*((omega**2*(sin(theta))**2) + (g*cos(theta)/R) + (dtheta**2))
    ddtheta -= f*cmp(dtheta, 0)


    dtheta += ddtheta*dt
    theta += dtheta*dt

    if not CAMERA_ROTATE:
        phi += omega*dt

    ring.axis = (cos(phi), 0, sin(phi))
    bead.pos = (R*sin(theta)*sin(phi), -R*cos(theta), -R*sin(theta)*cos(phi))

    rate(speed)
