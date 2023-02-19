import random
'''
Creates Random swim training plan
'''
time = 0
warmup = "200m front crawl 5min\n 50m backstroke 2min\n 50m breaststroke 2min\n 1min rest"
lengths = ["25","50","100","150"]
sprints = ["sprint","sprint","sprint","normal"]
strokes = ["front crawl","front crawl","front crawl","front crawl","Legs with float","Arm with float","Arms with bouy"]
plan = []
# these are the random choices

while time < 1260 :
    length = random.choice(lengths)
    #sets a length to do
    stroke = random.choice(strokes)
    #sets the stroke to do
    if stroke == "front crawl":
        sprint = random.choice(sprints)
        # chooses whether its a sprint or not
        if sprint == "sprint":
            if length == "25":
                t = 25
                r = 30
            elif length == "50":
                t = 55
                r = 60
            elif length == "100":
                t = 120
                r = 120
            else:
                t = 150
                r = 150
        else:
            if length == "25":
                t = 35
                r = 5
            elif length == "50":
                t = 70
                r = 5
            elif length == "100":
                t = 145
                r = 10
            else:
                t = 185
                r = 15
    else:
        sprint = "normal"
        if length == "25":
            t = 45
            r = 15
        elif length == "50":
            t = 90
            r = 30
        elif length == "100":
            t = 180
            r = 60
        else:
            t = 270
            r = 60
    #sets times and rest times based around my personal timings
    time = time + t + r
    #adds times
    length = str(length)
    sprint = str(sprint)
    stroke = str(stroke)
    tm = str(t//60)
    ts = str(t%60)
    rm = str(r//60)
    rs = str(r%60)
    activity = length + "m " + sprint + " " + stroke + " " + tm + "min" + ts + "seconds with " + rm + "min " + rs + "s" + "rest"
    plan.append(activity)
    #add this to the pool plan

    
print ("warm up -\n",warmup,"\n")
for count in range(len(plan)):
    print (plan[count])
#outputs the pool plan to pps
