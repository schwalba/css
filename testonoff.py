from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil

loc_on_set_1     = display.getWidget("Boolean_Switch_on_set_pneuval1_loc")
loc_on_set_2     = display.getWidget("Boolean_Switch_on_set_pneuval2_loc")

loc_on_set_1PV = loc_on_set_1.getPV()
loc_on_set_2PV = loc_on_set_2.getPV()

loc_on_set_2PV.setValue(PVUtil.getString(loc_on_set_1PV))

ConsoleUtil.writeInfo("-----loc_on_set_1-----")
ConsoleUtil.writeInfo(PVUtil.getString(loc_on_set_1PV))
ConsoleUtil.writeInfo("-----loc on_set_2-----")
ConsoleUtil.writeInfo(PVUtil.getString(loc_on_set_2PV))