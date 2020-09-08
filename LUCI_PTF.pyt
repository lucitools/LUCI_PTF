# -*- coding: utf-8 -*-
import arcpy
import os
import sys

import configuration
try:
    reload(configuration)  # Python 2.7
except NameError:
    try:
        import importlib # Python 3.4
        importlib.reload(configuration)
    except Exception:
    	arcpy.AddError('Could not load configuration module')
    	sys.exit()

# Load and refresh the refresh_modules module
from LUCI_PTF.lib.external.six.moves import reload_module
import LUCI_PTF.lib.refresh_modules as refresh_modules
reload_module(refresh_modules)
from LUCI_PTF.lib.refresh_modules import refresh_modules

import LUCI_PTF.lib.input_validation as input_validation
refresh_modules(input_validation)

import LUCI_PTF.tool_classes.c_SoilParam as c_SoilParam
refresh_modules(c_SoilParam)
SoilParam = c_SoilParam.SoilParam

##########################
### Toolbox definition ###
##########################

class Toolbox(object):

    def __init__(self):
        self.label = u'LUCI PTF v1.0'
        self.alias = u'LUCI PTF v1.0'
        self.tools = [SoilParam]
