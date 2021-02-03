#We import the module
import pywhatkit as pwk

# the first parameter goes the number (+576689741522)
# the second parameter is the message.
# the third parameter is the time in 24 and then minutes 00.
try:
  pwk.sendwhatmsg("+5368558855", "Hello word send message python", 12,40)
except:
  print("Se produjo un error")