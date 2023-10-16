from redis import Redis
from Location import Location
client = Redis(decode_responses=True)
location = Location(client)
location.pin("peter", 113.20996731519699, 23.593675019671288) 
location.pin("jack", 113.22784155607224, 23.125598202060807)  
location.pin("tom", 113.40603142976761, 22.511156445825442)   
location.pin("mary", 113.0398344, 23.6945014)
location.pin("david", 113.0398861, 23.6933749)
print(location.find_nearby("peter", 100000))                       

print(location.get("peter"))
print(location.get("jack"))
print(location.calculate_distance("peter", "jack"))
print(location.calculate_distance("peter", "tom"))
print(location.find_random_nearby("peter", 100000))          # 随机地返回peter附近的一位用户
