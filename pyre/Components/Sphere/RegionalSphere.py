#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from Sphere import Sphere

class RegionalSphere(Sphere):


    def __init__(self, name, facility, CitcomModule):
        Sphere.__init__(self, name, facility, CitcomModule)
	self.inventory.nproc_surf = 1
        return



    def launch(self):
        self.CitcomModule.regional_sphere_launch()
	return




# version
__id__ = "$Id: RegionalSphere.py,v 1.7 2003/08/01 19:05:36 tan2 Exp $"

# End of file
