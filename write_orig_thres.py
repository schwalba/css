from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from java.lang import Thread, Runnable

sp1_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp1_low_set_2  = display.getWidget("Text_Update_gauge2_sp1_low_set")
sp2_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp2_low_set_2  = display.getWidget("Text_Update_gauge2_sp2_low_set")

sp1_high_set_2PV = sp1_high_set_2.getPV()
sp1_low_set_2PV  = sp1_low_set_2.getPV()
sp2_high_set_2PV = sp2_high_set_2.getPV()
sp2_low_set_2PV  = sp2_low_set_2.getPV()

sp1_high_low_2PV.setValue(PVUtil.getDouble(sp1_high_set_orig_2))
sp1_low_low_2PV.setValue(PVUtil.getDouble(sp1_low_set_orig_2))
sp2_high_low_2PV.setValue(PVUtil.getDouble(sp2_high_set_orig_2))
sp2_low_low_2PV.setValue(PVUtil.getDouble(sp2_low_set_orig_2))