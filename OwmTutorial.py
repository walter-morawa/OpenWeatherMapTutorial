import requests
#Which city and country do we want to request? Create an array
cities = ['New York', 'Denver', 'Atlanta']
#parameters- which type of request are we making
parameter = 'weather'
#normally you should never share an API key: its basically your password!
owm_api_key = 'Your_API_Key' 
#for loops allow us to iterate through the cities easily
for city in cities:
  #here we use Open Weather Map's API to request.get data
  httpLink = 'http://api.openweathermap.org/data/2.5/'+ parameter+'?q=' + city +',us&appid=' + owm_api_key
  #get the data in json format
  r = requests.get(httpLink).json()
  #if statements allow us to execute code under certain circumstances
  if city == 'Denver':
    print('Denver is my favorite city!')
  #create a variable to store it for later
  weather = r['weather']
  description = weather[0]['description']
  #print is what makes stuff spit out to the right
  print('The weather in ' + city + ' is : ' + description)
