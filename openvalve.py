from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil


sp1_high_set_1 = display.getWidget("Text_Update_gauge_sp1_high_set")
sp1_low_set_1  = display.getWidget("Text_Update_gauge_sp1_low_set")
sp2_high_set_1 = display.getWidget("Text_Update_gauge_sp2_high_set")
sp2_low_set_1  = display.getWidget("Text_Update_gauge_sp2_low_set")

sp1_high_set_1PV = sp1_high_set_1.getPV()
sp1_low_set_1PV  = sp1_low_set_1.getPV()
sp2_high_set_1PV = sp2_high_set_1.getPV()
sp2_low_set_1PV  = sp2_low_set_1.getPV()

#first check pneuval PV connection
if (sp1_high_set_1PV.getValue()):
    ConsoleUtil.writeInfo("-----Pneuval 1-----")
    
    label_gauge_sp1_high_set_2 = display.getWidget("Label_gauge_sp1_high_set_2")
    label_gauge_sp1_low_set_2  = display.getWidget("Label_gauge_sp1_low_set_2")
    label_gauge_sp2_high_set_2 = display.getWidget("Label_gauge_sp2_high_set_2")
    label_gauge_sp2_low_set_2  = display.getWidget("Label_gauge_sp2_low_set_2")
    
    #fields to set new thresholds, first locally
    loc_sp1_high_set_1 = display.getWidget("Text_Input_gauge_sp1_high_set")
    loc_sp1_low_set_1  = display.getWidget("Text_Input_gauge_sp1_low_set")
    loc_sp2_high_set_1 = display.getWidget("Text_Input_gauge_sp2_high_set")
    loc_sp2_low_set_1  = display.getWidget("Text_Input_gauge_sp2_low_set")

    loc_sp1_high_set_1PV = loc_sp1_high_set_1.getPV()
    loc_sp1_low_set_1PV  = loc_sp1_low_set_1.getPV()
    loc_sp2_high_set_1PV = loc_sp2_high_set_1.getPV()
    loc_sp2_low_set_1PV  = loc_sp2_low_set_1.getPV()
    
    on_set     = display.getWidget("Boolean_Switch_on_set_pneuval")
    loc_on_set = display.getWidget("Boolean_Switch_on_set_pneuval_loc")
    bar        = display.getWidget("Progress_Bar")
    p_get      = display.getWidget("Text_Update_p_get")
    
    on_setPV     = on_set.getPV()
    loc_on_setPV = loc_on_set.getPV()
    p_getPV      = p_get.getPV()
    barPV        = bar.getPV()
    
    ConsoleUtil.writeInfo("-----Orig thresholds-----")
    #remember the original thresholds
    if ((sp1_high_set_1PV.getValue()) and (sp1_low_set_1PV.getValue())):
        sp1_high_set_orig = PVUtil.getDouble(sp1_high_set_1PV)
        sp1_low_set_orig  = PVUtil.getDouble(sp1_low_set_1PV)
        ConsoleUtil.writeInfo(str(sp1_high_set_orig))
        ConsoleUtil.writeInfo(str(sp1_low_set_orig))

    if ((sp2_high_set_1PV.getValue()) and (sp2_low_set_1PV.getValue())):   
        sp2_high_set_orig = PVUtil.getDouble(sp2_high_set_1PV)
        sp2_low_set_orig  = PVUtil.getDouble(sp2_low_set_1PV)
        ConsoleUtil.writeInfo(str(sp2_high_set_orig))
        ConsoleUtil.writeInfo(str(sp2_low_set_orig))
       
    ConsoleUtil.writeInfo("-----New thresholds-----")
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())):   
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_high_set_1PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_low_set_1PV))
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())): 
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_high_set_1PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_low_set_1PV))   
    
    #Labels for the input fields to set the orig thresholds
    label_sp1_high_low = display.getWidget("Label_gauge_sp1_high_set_low")
    label_sp1_low_low  = display.getWidget("Label_gauge_sp1_low_set_low")
    label_sp2_high_low = display.getWidget("Label_gauge_sp2_high_set_low")
    label_sp2_low_low  = display.getWidget("Label_gauge_sp2_low_set_low")
    
    #input fields to set the orig thresholds
    loc_input_sp1_high_low = display.getWidget("Text_Input_gauge_sp1_high_set_low")
    loc_input_sp1_low_low  = display.getWidget("Text_Input_gauge_sp1_low_set_low")
    loc_input_sp2_high_low = display.getWidget("Text_Input_gauge_sp2_high_set_low")
    loc_input_sp2_low_low  = display.getWidget("Text_Input_gauge_sp2_low_set_low")
    
    #write old values to loc vars and new thresholds to PVs
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())): 
        loc_input_sp1_high_low.setValue(sp1_high_set_orig)
        loc_input_sp1_low_low.setValue(sp1_low_set_orig)
        sp1_high_set_1PV.setValue(PVUtil.getDouble(loc_sp1_high_set_1PV))
        sp1_low_set_1PV.setValue(PVUtil.getDouble(loc_sp1_low_set_1PV))
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())):
        loc_input_sp2_high_low.setValue(sp2_high_set_orig)
        loc_input_sp2_low_low.setValue(sp2_low_set_orig)
        sp2_high_set_1PV.setValue(PVUtil.getDouble(loc_sp2_high_set_1PV))
        sp2_low_set_1PV.setValue(PVUtil.getDouble(loc_sp2_low_set_1PV))  
    
    ConsoleUtil.writeInfo("-----loc_on_setPV-----")
    loc_on = PVUtil.getLong(loc_on_setPV)
    ConsoleUtil.writeInfo(str(loc_on))
    ConsoleUtil.writeInfo(PVUtil.getString(loc_on_setPV))
    on_setPV.setValue(PVUtil.getString(loc_on_setPV)) 
    ConsoleUtil.writeInfo("-----on_setPV-----")
    ConsoleUtil.writeInfo(PVUtil.getString(on_setPV)) 
    
    bar.setVisible(True)    
    p_get.setVisible(True)  
    #if (p_get_1PV.getValue()):
    barPV.setValue(PVUtil.getDouble(p_getPV))
    #bar_1PV.setValue(8e-10)
    
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())):
        label_sp1_high_low.setVisible(True)
        label_sp1_low_low.setVisible(True)
        loc_input_sp1_high_low.setVisible(True)
        loc_input_sp1_low_low.setVisible(True)
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())):   
        label_sp2_high_low.setVisible(True)
        label_sp2_low_low.setVisible(True)
        loc_input_sp2_high_low.setVisible(True)
        loc_input_sp2_low_low.setVisible(True)   
        
#end if first check pneuval1 PV connection
#else:
    #ConsoleUtil.writeInfo("Pneuval 1 not connected")



#if ((sp1_high_setPV.getValue()) or (sp1_high_setPV.getValue())):
if (sp1_high_set_1PV.getValue()):
    action = display.getWidget("Action Button")
    blink  = display.getWidget("blink_action")
    action.setVisible(False)       
    blink.setVisible(True)
    if (sp1_high_set_1PV.getValue()):
        action_gauge_reset = display.getWidget("action_gauge_reset")
        action_gauge_reset.setVisible(True)
    
    
 



