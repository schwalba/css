from org.csstudio.opibuilder.scriptUtil import PVUtil
#from org.csstudio.opibuilder.scriptUtil import triggerPV
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from java.lang import Thread, Runnable

on_set_1        = display.getWidget("Boolean_Switch_on_set_pneuval1")
on_set_2        = display.getWidget("Boolean_Switch_on_set_pneuval2")

#show the original thresholds, _1 = GAUGE1, _2 = Gauge"
sp1_high_set_1 = display.getWidget("Text_Update_gauge1_sp1_high_set")
sp1_low_set_1  = display.getWidget("Text_Update_gauge1_sp1_low_set")
sp2_high_set_1 = display.getWidget("Text_Update_gauge1_sp1_high_set")
sp2_low_set_1  = display.getWidget("Text_Update_gauge1_sp2_low_set")
sp1_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp1_low_set_2  = display.getWidget("Text_Update_gauge2_sp1_low_set")
sp2_high_set_2 = display.getWidget("Text_Update_gauge2_sp1_high_set")
sp2_low_set_2  = display.getWidget("Text_Update_gauge2_sp2_low_set")

#fields to set new thresholds, first locally
loc_sp1_high_set_1 = display.getWidget("Text_Input_gauge1_sp1_high_set")
loc_sp1_low_set_1  = display.getWidget("Text_Input_gauge1_sp1_low_set")
loc_sp2_high_set_1 = display.getWidget("Text_Input_gauge1_sp2_high_set")
loc_sp2_low_set_1  = display.getWidget("Text_Input_gauge1_sp2_low_set")
loc_sp1_high_set_2 = display.getWidget("Text_Input_gauge2_sp1_high_set")
loc_sp1_low_set_2  = display.getWidget("Text_Input_gauge2_sp1_low_set")
loc_sp2_high_set_2 = display.getWidget("Text_Input_gauge2_sp2_high_set")
loc_sp2_low_set_2  = display.getWidget("Text_Input_gauge2_sp2_low_set")

#fields to set pneuvals on, first locally
loc_on_set_1     = display.getWidget("Boolean_Switch_on_set_pneuval1")
loc_on_set_2     = display.getWidget("Boolean_Switch_on_set_pneuval2")

bar_1  = display.getWidget("Progress_Bar_1")
bar_2  = display.getWidget("Progress_Bar_2")
p_get_1  = display.getWidget("Text_Update_p_get_1")
p_get_2  = display.getWidget("Text_Update_p_get_2")
action = display.getWidget("Action Button")
blink  = display.getWidget("Label_blink")

#fields to set thresholds back to original values
label_sp1_high_low_1 = display.getWidget("Label_gauge1_sp1_high_set_low")
label_sp1_low_low_1  = display.getWidget("Label_gauge1_sp1_low_set_low")
label_sp2_high_low_1 = display.getWidget("Label_gauge1_sp2_high_set_low")
label_sp2_low_low_1  = display.getWidget("Label_gauge1_sp2_low_set_low")
label_sp1_high_low_2 = display.getWidget("Label_gauge2_sp1_high_set_low")
label_sp1_low_low_2  = display.getWidget("Label_gauge2_sp1_low_set_low")
label_sp2_high_low_2 = display.getWidget("Label_gauge2_sp2_high_set_low")
label_sp2_low_low_2  = display.getWidget("Label_gauge2_sp2_low_set_low")
                     
input_sp1_high_low_1 = display.getWidget("Text_Input_gauge1_sp1_high_set_low")
input_sp1_low_low_1  = display.getWidget("Text_Input_gauge1_sp1_low_set_low")
input_sp2_high_low_1 = display.getWidget("Text_Input_gauge1_sp2_high_set_low")
input_sp2_low_low_1  = display.getWidget("Text_Input_gauge1_sp2_low_set_low")
input_sp1_high_low_2 = display.getWidget("Text_Input_gauge2_sp1_high_set_low")
input_sp1_low_low_2  = display.getWidget("Text_Input_gauge2_sp1_low_set_low")
input_sp2_high_low_2 = display.getWidget("Text_Input_gauge2_sp2_high_set_low")
input_sp2_low_low_2  = display.getWidget("Text_Input_gauge2_sp2_low_set_low")

on_set_1PV = on_set_1.getPV()
on_set_2PV = on_set_2.getPV()

sp1_high_set_1PV = sp1_high_set_1.getPV()
sp1_low_set_1PV  = sp1_low_set_1.getPV()
sp2_high_set_1PV = sp2_high_set_1.getPV()
sp2_low_set_2PV  = sp2_low_set_1.getPV()
sp1_high_set_2PV = sp1_high_set_2.getPV()
sp1_low_set_2PV  = sp1_low_set_2.getPV()
sp2_high_set_2PV = sp2_high_set_2.getPV()
sp2_low_set_2PV  = sp2_low_set_2.getPV()

loc_sp1_high_set_1PV = loc_sp1_high_set_1.getPV()
loc_sp1_low_set_1PV  = loc_sp1_low_set_1.getPV()
loc_sp2_high_set_1PV = loc_sp2_high_set_1.getPV()
loc_sp2_low_set_1PV  = loc_sp2_low_set_1.getPV()
loc_sp1_high_set_2PV = loc_sp1_high_set_2.getPV()
loc_sp1_low_set_2PV  = loc_sp1_low_set_2.getPV()
loc_sp2_high_set_2PV = loc_sp2_high_set_2.getPV()
loc_sp2_low_set_2PV  = loc_sp2_low_set_2.getPV()

loc_on_set_1PV = loc_on_set_1.getPV()
loc_on_set_2PV = loc_on_set_2.getPV()
p_get_1PV      = p_get_1.getPV()
p_get_2PV      = p_get_2.getPV()
bar_1PV        = bar_1.getPV()
bar_2PV        = bar_2.getPV()

ConsoleUtil.writeInfo("----_Orig thresholds-----")

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

ConsoleUtil.writeInfo("----_New thresholds-----")
if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())):    
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_high_set_1PV))
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_low_set_1PV))
if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())): 
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_high_set_1PV))
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_low_set_1PV))
if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())):    
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_high_set_2PV))
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp1_low_set_2PV))
if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())): 
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_high_set_2PV))
    ConsoleUtil.writeInfo(PVUtil.getString(loc_sp2_low_set_2PV))

class OpenValve(Runnable):
    def run(self): 
        
        #write new thresholds to PVs
        #if ((loc_sp1_high_set_1.getValue()) and (loc_sp1_low_set_1.getValue())): 
            #sp1_high_set_1PV.setValue(PVUtil.getDouble(loc_sp1_high_set_1PV))
            #sp1_low_setPV_1.setValue(PVUtil.getDouble(loc_sp1_low_set_1PV))
        #if ((loc_sp2_high_set_1.getValue()) and (loc_sp2_low_set_1.getValue())): 
            #sp2_high_setPV_1.setValue(PVUtil.getDouble(loc_sp2_high_set_1PV))
            #sp2_low_setPV_1.setValue(PVUtil.getDouble(loc_sp2_low_set_1PV))
            
        #if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())): 
            #sp1_high_set_2PV.setValue(PVUtil.getDouble(loc_sp1_high_set_2PV))
            #sp1_low_setPV_2.setValue(PVUtil.getDouble(loc_sp1_low_set_2PV))
        #if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())): 
            #sp2_high_setPV_2.setValue(PVUtil.getDouble(loc_sp2_high_set_2PV))
            #sp2_low_setPV_2.setValue(PVUtil.getDouble(loc_sp2_low_set_2PV))
        
        
        on_set_1PV.setValue(PVUtil.getDouble(loc_on_set_1PV))
        on_set_2PV.setValue(PVUtil.getDouble(loc_on_set_2PV))
        bar_1.setVisible(True)
        bar_2.setVisible(True)
        p_get.setVisible(True)
        action.setVisible(False)
        
        # dient nur dazu 20 sec abzuwarten, bevor ich die Werte zurücksetze
        #for i in range(0,1E-8,48E-9):    #range(start, stop[, step])
        #for i in range(0,21,1):    #range(start, stop[, step])
            #barPV.setValue(i)
            #Thread.sleep(1000)     #msec
        bar_1PV.setValue(PVUtil.getDouble(p_getPV))
        bar_2PV.setValue(PVUtil.getDouble(p_getPV))
        #barPV.setValue(8e-10)
        
        blink.setVisible(True)
        
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
        if ((loc_sp1_high_set_2.getValue()) and (loc_sp1_low_set_2.getValue())):
            label_sp1_high_low_2.setVisible(True)
            label_sp1_low_low_2.setVisible(True)
            input_sp1_high_low_2.setVisible(True)
            input_sp1_low_low_2.setVisible(True)
        if ((loc_sp2_high_set_2.getValue()) and (loc_sp2_low_set_2.getValue())):   
            label_sp2_high_low_2.setVisible(True)
            label_sp2_low_low_2.setVisible(True)
            input_sp2_high_low_2.setVisible(True)
            input_sp2_low_low_2.setVisible(True)
        
        #ConsoleUtil.writeInfo("-----------------New Values---------------------")
        #ConsoleUtil.writeInfo(PVUtil.getString(thresholdPV_1))
        #ConsoleUtil.writeInfo(PVUtil.getString(thresholdPV_2))
        #ConsoleUtil.writeInfo(PVUtil.getString(onsetPV))
       
thread = Thread(OpenValve());
thread.start();
