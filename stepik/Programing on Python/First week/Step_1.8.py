
SleepHours = int(input())
SleepMinutes = int(input())
print(SleepHours*60 + SleepMinutes)

SleepMinutes = int(input())
SleepHours = SleepMinutes // 60
SleepMinutes %= 60
print(SleepHours, '\n', SleepMinutes)

TimeForSleeping = int(input())
StartHours = int(input())
StartMinutes = int(input())
FinishHours = (TimeForSleeping + StartHours*60 +
               StartMinutes)//60
FinishMinutes = (TimeForSleeping + StartHours*60 +
               StartMinutes)%60
print(FinishHours, '\n', FinishMinutes)


