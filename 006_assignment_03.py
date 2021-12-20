Hours1=int(input("Give me the start time hour."))
Minutes1=int(input("Give me the start time minutes."))
DURATION=int(input("Give me the duration in minutes."))
Formula=Hours1*60+Minutes1+DURATION
Hours2=Formula//60
Minutes2=Formula-Hours2*60
print("The Finish time is:",end="")
print(Hours2,Minutes2,sep=":")
