class time:
   def __init__(obj,h,m,s):
      obj.hour = h
      obj.minute = m
      obj.second = s
   def show(obj):
      return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
   def number_of_seconds(obj):
      return obj.hour*3600+obj.minute*60+obj.second
   def ezafe_kardan(obj,hh,mm,ss):
      obj.hour += hh
      obj.minute += mm
      obj.second += ss
   def add(obj,saate_jadid):
      obj.hour += saate_jadid.hour
      obj.minute += saate_jadid.minute
      obj.second += saate_jadid.second
   def __add__(obj,obj2):
      obj.hour += obj2.hour
      obj.minute += obj2.minute
      obj.second += obj2.second


   def __gt__(obj, obj2):
      if obj.minute*60+ obj.hour *3600 + obj.second > obj2.minute*60+obj2.hour*3600+obj2.second:
         return True
      return False

   def __lt__(obj,obj2):
      if obj.minute*60+obj.hour*3600+obj.second < obj2.minute*60+obj2.hour*3600+obj2.second:
         return True
      return False

   def __str__(obj):
      return str(obj.hour)

   def __repr__(obj):
      return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
      
      

      
      
      
      
      
      
      
      
      
   
