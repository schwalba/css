from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from java.lang import Thread, Runnable

#show the original thresholds, at the end _1 = GAUGE1, _2 = Gauge2, at the end _low Schwelle zurücksetzen

#first pneuval1
#to get the original values
sp1_high_set_1 = display.getWidget("Text_Update_gauge1_sp1_high_set")
sp1_low_set_1  = display.getWidget("Text_Update_gauge1_sp1_low_set")
sp2_high_set_1 = display.getWidget("Text_Update_gauge1_sp1_high_set")
sp2_low_set_1  = display.getWidget("Text_Update_gauge1_sp2_low_set")

sp1_high_set_1PV = sp1_high_set_1.getPV()
sp1_low_set_1PV  = sp1_low_set_1.getPV()
sp2_high_set_1PV = sp2_high_set_1.getPV()
sp2_low_set_2PV  = sp2_low_set_1.getPV()

#first check pneuval1 PV connection
if (sp1_high_set_1PV.getValue()):
    ConsoleUtil.writeInfo("-----Pneuval 1-----")
    
    #label_gauge1_sp1_high_set_2 = display.getWidget("Label_gauge1_sp1_high_set_2")
    #label_gauge1_sp1_low_set_2 = display.getWidget("Label_gauge1_sp1_low_set_2")
    #label_gauge1_sp2_high_set_2 = display.getWidget("Label_gauge1_sp2_high_set_2")
    #label_gauge1_sp2_low_set_2 = display.getWidget("Label_gauge1_sp2_low_set_2")
    
    #fields to set new thresholds, first locally
    loc_sp1_high_set_1 = display.getWidget("Text_Input_gauge1_sp1_high_set")
    loc_sp1_low_set_1  = display.getWidget("Text_Input_gauge1_sp1_low_set")
    loc_sp2_high_set_1 = display.getWidget("Text_Input_gauge1_sp2_high_set")
    loc_sp2_low_set_1  = display.getWidget("Text_Input_gauge1_sp2_low_set")

    loc_sp1_high_set_1PV = loc_sp1_high_set_1.getPV()
    loc_sp1_low_set_1PV  = loc_sp1_low_set_1.getPV()
    loc_sp2_high_set_1PV = loc_sp2_high_set_1.getPV()
    loc_sp2_low_set_1PV  = loc_sp2_low_set_1.getPV()
    
    on_set_1     = display.getWidget("Boolean_Switch_on_set_pneuval1")
    loc_on_set_1 = display.getWidget("Boolean_Switch_on_set_pneuval1")
    bar_1        = display.getWidget("Progress_Bar_1")
    p_get_1      = display.getWidget("Text_Update_p_get_1")
    
    on_set_1PV     = on_set_1.getPV()
    loc_on_set_1PV = loc_on_set_1.getPV()
    p_get_1PV      = p_get_1.getPV()
    bar_1PV        = bar_1.getPV()
    
    ConsoleUtil.writeInfo("-----Orig thresholds-----")
    #remember the original thresholds
    if ((sp1_high_set_1PV.getValue()) and (sp1_low_set_1PV.getValue())):
        sp1_high_set_orig_1 = PVUtil.getDouble(sp1_high_set_1PV)
        sp1_low_set_orig_1  = PVUtil.getDouble(sp1_low_set_1PV)
        ConsoleUtil.writeInfo(str(sp1_high_set_orig_1))
        ConsoleUtil.writeInfo(str(sp1_low_set_orig_1))

    if ((sp2_high_set_1PV.getValue()) and (sp2_low_set_1PV.getValue())):   
        sp2_high_set_orig_1 = PVUtil.getDouble(sp2_high_set_1PV)
        sp2_low_set_orig_1  = PVUtil.getDouble(sp2_low_set_1PV)
        ConsoleUtil.writeInfo(str(sp2_high_set_orig_1))
        ConsoleUtil.writeInfo(str(sp2_low_set_orig_1))
        
    ConsoleUtil.writeInfo("-----New thresholds-----")
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())):   
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_high_set_1PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_low_set_1PV))
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())): 
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_high_set_1PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_low_set_1PV))   
    
    #Labels for the input fields to set the orig thresholds
    label_sp1_high_low_1 = display.getWidget("Label_gauge1_sp1_high_set_low")
    label_sp1_low_low_1  = display.getWidget("Label_gauge1_sp1_low_set_low")
    label_sp2_high_low_1 = display.getWidget("Label_gauge1_sp2_high_set_low")
    label_sp2_low_low_1  = display.getWidget("Label_gauge1_sp2_low_set_low")
    
    #input fields to set the orig thresholds
    loc_input_sp1_high_low_1 = display.getWidget("Text_Input_gauge1_sp1_high_set_low")
    loc_input_sp1_low_low_1  = display.getWidget("Text_Input_gauge1_sp1_low_set_low")
    loc_input_sp2_high_low_1 = display.getWidget("Text_Input_gauge1_sp2_high_set_low")
    loc_input_sp2_low_low_1  = display.getWidget("Text_Input_gauge1_sp2_low_set_low")
    
    #write old values to loc vars and new thresholds to PVs
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())): 
        loc_input_sp1_high_low_1.setValue(sp1_high_set_orig_1)
        loc_input_sp1_low_low_1.setValue(sp1_low_set_orig_1)
        #sp1_high_set_1PV.setValue(PVUtil.getDouble(loc_sp1_high_set_1PV))
        #sp1_low_setPV_1.setValue(PVUtil.getDouble(loc_sp1_low_set_1PV))
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())):
        loc_input_sp2_high_low_1.setValue(sp2_high_set_orig_1)
        loc_input_sp2_low_low_1.setValue(sp2_low_set_orig_1)
        #sp2_high_setPV_1.setValue(PVUtil.getDouble(loc_sp2_high_set_1PV))
        #sp2_low_setPV_1.setValue(PVUtil.getDouble(loc_sp2_low_set_1PV))  
    
    #on_set_1PV.setValue(PVUtil.getDouble(loc_on_set_1PV)) 
    
    bar_1.setVisible(True)    
    p_get_1.setVisible(True)  
    #if (p_get_1PV.getValue()):
    bar_1PV.setValue(PVUtil.getDouble(p_get_1PV))
    #bar_1PV.setValue(8e-10)
    
    if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())):
        label_sp1_high_low_1.setVisible(True)
        label_sp1_low_low_1.setVisible(True)
        input_sp1_high_low_1.setVisible(True)
        input_sp1_low_low_1.setVisible(True)
    if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())):   
        label_sp2_high_low_1.setVisible(True)
        label_sp2_low_low_1.setVisible(True)
        input_sp2_high_low_1.setVisible(True)
        input_sp2_low_low_1.setVisible(True)   
        
#end if first check pneuval1 PV connection
#else:
    #ConsoleUtil.writeInfo("Pneuval 1 not connected")

####################second pneuval2#######################
#show the original thresholds, _1 = GAUGE1, _2 = Gauge"
sp1_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp1_low_set_2  = display.getWidget("Text_Update_gauge2_sp1_low_set")
sp2_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp2_low_set_2  = display.getWidget("Text_Update_gauge2_sp2_low_set")

sp1_high_set_2PV = sp1_high_set_2.getPV()
sp1_low_set_2PV  = sp1_low_set_2.getPV()
sp2_high_set_2PV = sp2_high_set_2.getPV()
sp2_low_set_2PV  = sp2_low_set_2.getPV()

#first check pneuval2 PV connection
if (sp1_high_set_2PV.getValue()):        
    ConsoleUtil.writeInfo("-----Pneuval 2-----")
    
    #label_gauge2_sp1_high_set_2 = display.getWidget("Label_gauge2_sp1_high_set_2")
    #label_gauge2_sp1_low_set_2 = display.getWidget("Label_gauge2_sp1_low_set_2")
    #label_gauge2_sp2_high_set_2 = display.getWidget("Label_gauge2_sp2_high_set_2")
    #label_gauge2_sp2_low_set_2 = display.getWidget("Label_gauge2_sp2_low_set_2")
    
    #fields to set new thresholds, first locally
    loc_sp1_high_set_2 = display.getWidget("Text_Input_gauge2_sp1_high_set")
    loc_sp1_low_set_2  = display.getWidget("Text_Input_gauge2_sp1_low_set")
    loc_sp2_high_set_2 = display.getWidget("Text_Input_gauge2_sp2_high_set")
    loc_sp2_low_set_2  = display.getWidget("Text_Input_gauge2_sp2_low_set")
    
    loc_sp1_high_set_2PV = loc_sp1_high_set_2.getPV()
    loc_sp1_low_set_2PV  = loc_sp1_low_set_2.getPV()
    loc_sp2_high_set_2PV = loc_sp2_high_set_2.getPV()
    loc_sp2_low_set_2PV  = loc_sp2_low_set_2.getPV()
    
    on_set_2     = display.getWidget("Boolean_Switch_on_set_pneuval2")
    loc_on_set_2 = display.getWidget("Boolean_Switch_on_set_pneuval2")
    bar_2        = display.getWidget("Progress_Bar_2")
    p_get_2      = display.getWidget("Text_Update_p_get_2") 

    on_set_2PV     = on_set_2.getPV()
    loc_on_set_2PV = loc_on_set_2.getPV()
    p_get_2PV      = p_get_2.getPV()
    bar_2PV        = bar_2.getPV()
    #bar_2PV.setValue(8e-10)
    
    #remember the original thresholds
    ConsoleUtil.writeInfo("-----Orig thresholds-----")
    if ((sp1_high_set_2PV.getValue()) and (sp1_low_set_2PV.getValue())):    
        sp1_high_set_orig_2 = PVUtil.getDouble(sp1_high_set_2PV)
        sp1_low_set_orig_2  = PVUtil.getDouble(sp1_low_set_2PV)
        ConsoleUtil.writeInfo(str(sp1_high_set_orig_2))
        ConsoleUtil.writeInfo(str(sp1_low_set_orig_2))
    
    if ((sp2_high_set_2PV.getValue()) and (sp2_low_set_2PV.getValue())):    
        sp2_high_set_orig_2 = PVUtil.getDouble(sp2_high_set_2PV)
        sp2_low_set_orig_2  = PVUtil.getDouble(sp2_low_set_2PV)
        ConsoleUtil.writeInfo(str(sp2_high_set_orig_2))
        ConsoleUtil.writeInfo(str(sp2_low_set_orig_2))
    
    ConsoleUtil.writeInfo("-----New thresholds-----")
    if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())):
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_high_set_2PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_low_set_2PV))
    if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())): 
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_high_set_2PV))
        ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_low_set_2PV))
    
    #Labels for the input fields to set the orig thresholds
    label_sp1_high_low_2 = display.getWidget("Label_gauge2_sp1_high_set_low")
    label_sp1_low_low_2  = display.getWidget("Label_gauge2_sp1_low_set_low")
    label_sp2_high_low_2 = display.getWidget("Label_gauge2_sp2_high_set_low")
    label_sp2_low_low_2  = display.getWidget("Label_gauge2_sp2_low_set_low")
    
    #input fields to set the orig thresholds                
    loc_input_sp1_high_low_2 = display.getWidget("Text_Input_gauge2_sp1_high_set_low")
    loc_input_sp1_low_low_2  = display.getWidget("Text_Input_gauge2_sp1_low_set_low")
    loc_input_sp2_high_low_2 = display.getWidget("Text_Input_gauge2_sp2_high_set_low")
    loc_input_sp2_low_low_2  = display.getWidget("Text_Input_gauge2_sp2_low_set_low")
    
    #write old values to loc vars and new thresholds to PVs         
    if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())): 
        loc_input_sp1_high_low_2.setValue(sp1_high_set_orig_2)
        loc_input_sp1_low_low_2.setValue(sp1_low_set_orig_2)
        #sp1_high_set_2PV.setValue(PVUtil.getDouble(loc_sp1_high_set_2PV))
        #sp1_low_setPV_2.setValue(PVUtil.getDouble(loc_sp1_low_set_2PV))
    if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())): 
        loc_input_sp2_high_low_2.setValue(sp2_high_set_orig_2)
        loc_input_sp2_low_low_2.setValue(sp2_low_set_orig_2)
        #sp2_high_setPV_2.setValue(PVUtil.getDouble(loc_sp2_high_set_2PV))
        #sp2_low_setPV_2.setValue(PVUtil.getDouble(loc_sp2_low_set_2PV))
     
    #on_set_2PV.setValue(PVUtil.getDouble(loc_on_set_2PV))   
     
    bar_2.setVisible(True)
    p_get_2.setVisible(True)
    #if (p_get_2PV.getValue()):
    bar_2PV.setValue(PVUtil.getDouble(p_get_2PV))
    
    if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())):
        label_sp1_high_low_2.setVisible(True)
        label_sp1_low_low_2.setVisible(True)
        loc_input_sp1_high_low_2.setVisible(True)
        loc_input_sp1_low_low_2.setVisible(True)
    if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())):   
        label_sp2_high_low_2.setVisible(True)
        label_sp2_low_low_2.setVisible(True)
        loc_input_sp2_high_low_2.setVisible(True)
        loc_input_sp2_low_low_2.setVisible(True)
    
#end if second check pneuva2 PV connection

if ((sp1_high_set_1PV.getValue()) or (sp1_high_set_2PV.getValue())):
    action = display.getWidget("Action Button")
    blink  = display.getWidget("blink_action")
    action.setVisible(False)       
    blink.setVisible(True)
    if (sp1_high_set_1PV.getValue()):
        blink_gauge1_reset = display.getWidget("blink_gauge1_reset")
        blink_gauge1_reset.setVisible(True)
    if (sp1_high_set_2PV.getValue()):
        blink_gauge2_reset = display.getWidget("blink_gauge2_reset")
        blink_gauge2_reset.setVisible(True)
    
    
 



