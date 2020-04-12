from loading import classicLoading
from time import sleep
from consolemod import style
l = classicLoading(style.green('loading... '),'#',' ',100)
l.update(0.01)
print(end=style.green('1%'),flush=True)
sleep(1)
l.update(0.15435) # percentage
print(end=style.green('15%'),flush=True)
sleep(1)
l.update(0.5)
print(end=style.green('50%'),flush=True)
sleep(1)
l.update(1.0)
print(end=style.green('100%'),flush=True)
print(style.reset(),flush=True)
sleep(1)
from loading import fullLineLoading
l = fullLineLoading('loading... ','rhs',style.blue(),style.bluebg())
l.update(0.01)
sleep(1)
l.update(0.15435) # percentage
sleep(1)
l.update(0.5)
sleep(1)
l.update(1.0)
print(style.reset(),flush=True)
sleep(1)