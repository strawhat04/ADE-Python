#This module is to put the input condition for the simulation
import numpy as np


runtime=1	#simulation time
dt=0.1		#time step

#put your velocity model here, it may be function or you can import from a file
#keep the dimension in mind

def velocity_model(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos):
	flow_u=1
	flow_v=1
	flow_w=-1

	#need to difine at cv inteference points
	u=flow_u*np.ones((CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos))
	v=flow_v*np.ones((CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos))
	w=flow_w*np.ones((CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos))

	assert u.shape==(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos), "inncorect, shape of u"
	assert v.shape==(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos), "inncorect, shape of v"
	assert w.shape==(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos), "inncorect, shape of w"

	return u,v,w


#put your diffusion model here, it may be function or you can import from a file
#keep the dimension in mind
def diffusion_model(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos):
	G0=1
	
	#need to difine at cv inteference points
	gamma=G0*np.ones((CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos))		#create real diffusion coeff grid

	
	#subtract false diffusion coefficient due to oblique flow
	
	# for j in range(1, yGRID_nos):
	# 	for i in range(1, xGRID_nos):
	# 		if u[i,j]!=0 and v[i,j]!=0:
	# 			theta=atan(v[i,j]/u[i,j])
	# 			gamma[i,j]=gamma[i,j]-rho[i,j]*sqrt(u[i,j]**2+v[i,j]**2)*dxg(i)*dyg(j)*sin(2*theta)/(4*dyg(j)*sin(theta)**3+4*dxg(i)*cos(theta)**3) 
	
	assert gamma.shape==(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos), "inncorect, shape of gamma"
	return gamma


#put your velocity model here, it may be function or you can import from a file
#keep the dimension in mind
def density_model(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos):
	r0=20

	#need to difine at cv inteference points
	rho=r0*np.ones((CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos))

	assert rho.shape==(CV_zGRID_nos,CV_yGRID_nos,CV_xGRID_nos), "inncorect, shape of rho"
	return rho


#put your sourse term model here, it may be function or you can import from a file
#keep the dimension in mind
def source_model(zGRID_nos,yGRID_nos,xGRID_nos):
	sp0=0
	sc0=0

	#need to be defined at all grid points
	sp=sp0*np.ones((zGRID_nos,yGRID_nos,xGRID_nos))
	sc=sc0*np.ones((zGRID_nos,yGRID_nos,xGRID_nos))

	assert sp.shape==(zGRID_nos,yGRID_nos,xGRID_nos), "inncorect,shape of sp"
	assert sc.shape==(zGRID_nos,yGRID_nos,xGRID_nos), "inncorect,shape of sc"

	return sc, sp

