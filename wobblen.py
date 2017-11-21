from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil
from java.lang import Thread, Runnable

check_startwobble = display.getWidget("Action Button_Start_Wobble")   #define a widget_name
iwobble_set       = display.getWidget("Text_Input_iwobble_set")
iwobble_orig      = display.getWidget("Text_Input_iwobble_orig")
iwobblemin_set    = display.getWidget("Text_Input_iwobblemin_set")  
iwobblemax_set    = display.getWidget("Text_Input_iwobblemax_set")

check_startwobblePV = check_startwobble.getPV()  #widget.getPV()
iwobble_setPV       = iwobble_set.getPV()
iwobblemin_setPV    = iwobblemin_set.getPV()   
iwobblemax_setPV    = iwobblemax_set.getPV()

startstop = PVUtil.getLong(check_startwobblePV)

#save original value
iwobble_orig.setValue(PVUtil.getDouble(iwobble_setPV))  #show value in css
orig = PVUtil.getDouble(iwobble_setPV)

ConsoleUtil.writeInfo(str(startstop)) 
ConsoleUtil.writeInfo(PVUtil.getString(iwobblemin_setPV))
ConsoleUtil.writeInfo(PVUtil.getString(iwobblemax_setPV))
ConsoleUtil.writeInfo(PVUtil.getString(iwobble_setPV))
ConsoleUtil.writeInfo(str(orig))

minperc = PVUtil.getDouble(iwobblemin_setPV)
minval  = ((PVUtil.getDouble(iwobble_setPV))/100)*minperc
ConsoleUtil.writeInfo(str(minval))
maxperc = PVUtil.getDouble(iwobblemax_setPV)
maxval  = ((PVUtil.getDouble(iwobble_setPV))/100)*maxperc
ConsoleUtil.writeInfo(str(maxval))

class Wobblen(Runnable):
    def run(self): 
        while startstop == 1 :  # infinite loop
            
            iwobble_setPV.setValue(minval)
            Thread.sleep(400)       #msec
            #ConsoleUtil.writeInfo("-----------------MIN---------------------")
            ConsoleUtil.writeInfo(PVUtil.getString(iwobble_setPV)) 
            
            iwobble_setPV.setValue(maxval)
            Thread.sleep(600)
            #ConsoleUtil.writeInfo("-----------------MAX---------------------")
            ConsoleUtil.writeInfo(PVUtil.getString(iwobble_setPV))
            #Thread.sleep(600)
            if PVUtil.getLong(check_startwobblePV) == 0 :
                ConsoleUtil.writeInfo("-----------------STOP---------------------")
                ConsoleUtil.writeInfo(str(orig))
                iwobble_setPV.setValue(orig)
                break;

thread = Thread(Wobblen());
thread.start();
