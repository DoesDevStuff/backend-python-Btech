# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:56:30 2020

@author: prach
"""
import matplotlib.pyplot as plt
import axelrod as axl
import json

'''
listvalues = ['Hopeless', 'Desperate', 'TitforTat']
'''

#Hardcoded Values
sample_list=['TitForTat', 'Alternator','Forgiver','Grumpy']

#Array for transfer
tempt =[]

#Switch case for strategies
def simulate(text):
    if text=='Cooperator':
        tempt.append(axl.Cooperator())
    elif text=='TrickyCooperator':
        tempt.append(axl.TrickyCooperator())
    elif text=='Defector':
        tempt.append(axl.Defector())
    elif text=='Doubler':
        tempt.append(axl.Doubler())
    elif text=='Random':
        tempt.append(axl.Random())
    elif text=='Alternator':
        tempt.append(axl.Alternator())
    elif text=='TitForTat':
        tempt.append(axl.TitForTat())
    #Grumpy Threshold Values Displayed
    elif text=='Grumpy':
        tempt.append(axl.Grumpy())
    elif text=='Grudger':
        tempt.append(axl.Grudger())
    elif text=='Forgiver':
        tempt.append(axl.Forgiver())
    elif text=='Hopeless':
        tempt.append(axl.Hopeless())
    elif text=='Desperate':
        tempt.append(axl.Desperate())
    elif text=='EvolvedANN':
        tempt.append(axl.EvolvedANN())
    elif text=='EvolvedANN5':
        tempt.append(axl.EvolvedANN5())
    elif text=='EvolvedANN5noise5':
        tempt.append(axl.EvolvedANNNoise05())
    else:
        print("Strategy not found!")
    

for p in sample_list:
    simulate(p)
    print("Strategy added", p)

print('Tempt array')
print(tempt)

players=tempt
tournament = axl.Tournament(players)
results = tournament.play()
ranks= results.ranked_names

print('Ranks')
print(ranks)

wins=results.wins
print('Wins')
print(wins)

scores= results.scores
print('Scores')
print(scores)

payoffmatrix= results.payoff_matrix
print('Payoff Matrix')
print(payoffmatrix)  

payoffstd = results.payoff_stddevs
print('Payoff Standard Deviation')
print(payoffstd)

coop_count = results.cooperation
print('Co-operation Count')
print(coop_count)

Good_PRating = results.good_partner_rating
print('Good_PRating')
print(Good_PRating)


Good_PMatrix = results.good_partner_matrix
print('Good_PMatrix')
print(Good_PMatrix)


Cooperating_Rating = results.cooperating_rating  
print('Cooperating_Rating') 
print(Cooperating_Rating)

Vengeful_Cooperation = results.vengeful_cooperation
print('Vengeful_Cooperation')
print(Vengeful_Cooperation)

Eigenmoses_Rating = results.eigenmoses_rating
print('Eigenmoses_Rating') 
print(Eigenmoses_Rating)

Eigenjesus_Rating = results.eigenjesus_rating
print('Eigenjesus_Rating')
print(Eigenjesus_Rating)

eco = axl.Ecosystem(results)
rno = 100
eco.reproduce(rno) # Evolve the population over 100 time steps
#we can ask for reproduction iterations

tempt =[]

strategy = axl.WinStayLoseShift
probe = axl.TitForTat
af = axl.AshlockFingerprint(strategy, probe)
data = af.fingerprint(turns=10, repetitions=2, step=0.2)

#he fingerprint method returns a dictionary mapping coordinates of the form (x, y) to the mean score for the corresponding interactions
p = af.plot()
p.savefig('Tournament_Fingerprint Heatmap.jpg',dpi=500)
p.show()

#af.fingerprint(turns=50, repetitions=2, step=0.01)  

#We are also able to specify a matplotlib colour map, interpolation and can remove the colorbar and axis labels:
p = af.plot(cmap='PuOr', interpolation='bicubic', colorbar=False, labels=False) 
p.savefig('Tournament_Fingerprint colour map and interpolation.jpg',dpi=500) 
p.show()

#Transitive Fingerprinting

#The transitive fingerprint represents the cooperation rate of a strategy against a set of opponents over a number of turns.

def fsimulate(text):
    if text=='Cooperator':
        ftempt = axl.Cooperator()
    elif text=='TrickyCooperator':
        ftempt = axl.TrickyCooperator()
    elif text=='Defector':
        ftempt = axl.Defector()
    elif text=='Doubler':
        ftempt = axl.Doubler()
    elif text=='Random':
        ftempt = axl.Random()
    elif text=='Alternator':
        ftempt = axl.Alternator()
    elif text=='TitForTat':
        ftempt = axl.TitForTat()
        return ftempt
    #Grumpy Threshold Values Displayed
    elif text=='Grumpy':
        ftempt = axl.Grumpy()
    elif text=='Grudger':
        ftempt = axl.Grudger()
    elif text=='Forgiver':
        ftempt = axl.Forgiver()
    elif text=='Hopeless':
        ftempt = axl.Hopeless()
    elif text=='Desperate':
        ftempt = axl.Desperate()
    elif text=='EvolvedANN':
        ftempt = axl.EvolvedANN()
    elif text=='EvolvedANN5':
        ftempt = axl.EvolvedANN5()
    elif text=='EvolvedANN5noise5':
        ftempt = axl.EvolvedANNNoise05()
    else:
        print("Strategy not found!")
    
    
#player = axl.TitForTat()
#take strategy from user
userfplayer = 'TitForTat'

player = fsimulate(userfplayer)


tf = axl.TransitiveFingerprint(player)
data = tf.fingerprint(turns=40)
#we can ask for number of rounds
print( data.shape)

p = tf.plot()
p.savefig('Tournament_Fingerprint gradient',dpi=500)
p.show()

#It is also possible to fingerprint against a given set of opponents:
#opponents = [s() for s in axl.demo_strategies]

sample_list_fingerprint =[ 'Alternator','Forgiver','Hopeless', 'Random','Defector']
fno = len(sample_list_fingerprint)
tempt = []

for p in sample_list_fingerprint:
    simulate(p)
    print("Strategy added", p)

#ask for repetitions
tf = axl.TransitiveFingerprint(player, opponents=tempt)
data = tf.fingerprint(turns= (fno-1), repetitions=10)

p = tf.plot(display_names=True)
print('plotted !')
p.savefig('Tournament_Fingerprint Heatmap Turns vs Players.jpg',dpi=500)
p.show()
    
'''
summary = results.summarise()
import pprint
pprint.pprint(summary)
'''

'Plotting'
plot = axl.Plot(results)
p = plot.boxplot()
p.savefig('Tournament_Fingerprint Boxplot.jpg',dpi=500)
p.show()

p = plot.winplot()
p.savefig('Tournament_Fingerprint Winplot.jpg',dpi=500)
p.show()


_, ax = plt.subplots()
title = ax.set_title('Payoff')
xlabel = ax.set_xlabel('Strategies')
p = plot.boxplot(ax=ax)
p.savefig('Tournament_Fingerprint Boxplot Payoff Strategy.jpg',dpi=500)
p.show()

p = plot.payoff()
p.savefig('Tournament_Fingerprint Payoff Heatmap.jpg',dpi=500)
p.show()

plot = axl.Plot(results)
p_stackplot = plot.stackplot(eco)
p.savefig('Tournament_Fingerprint Evolution Stackplot.jpg',dpi=500)
p_stackplot.show()

