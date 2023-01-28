# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:55:54 2020

@author: prach
"""

#Library
import axelrod as axl
import json
import chart_studio
import chart_studio.plotly as py

#=========================================================================
username = 'why_Uh_No' # your username
api_key = 'PNMuTUCF6mJI3kiy7O0y' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

#==========================================================================


'''
Anuya's json format: text1, text2
temp1=text1 
temp2=text2
round=number of turns
'''
#Hardcoded Values
text1="Cooperator"
text2="Random"

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

tuple1 = (1,1)       
tuple2 = (3,3)       
tuple3 = (0,5)       
tuple4 = (5,0)        

stuple1 = (360000,360000)
stuple2 = (531000,531000)
stuple3 = (70000,814000)
stuple4 = (872000,70000)
        
#checking sales launch matrx values
def checksales(stup):
    if stup == tuple1:
        stup = stuple1
        return stup
    elif stup == tuple2:
        stup = stuple2
        return stup
    elif stup == tuple3:
        stup = stuple3
        return stup
    elif stup == tuple4:
        stup = stuple4    
        return stup
#-------------------------------

#adding both strategies        
simulate(text1)
print("Strategy 1 added")
print(tempt)

simulate(text2)
print("Strategy 2 added")
print(tempt)

#Creation of the final tuple as argument
players = tuple(tempt)

#players=(axl.Grumpy(), axl.Grudger)

#hardcoded value
playerturn = 12
match = axl.Match(players=players, turns=playerturn)
resultplay = (match.play())
matchscore = match.scores()
print(resultplay,matchscore)
#match = axl.Match(players,10)
#print(match.play())
#print(match.scores())

#returning quatity value in tempscore
matchscore_final = []
num = playerturn -1
for i in range(num):
   tempscore =  matchscore[i]
   tempscore = checksales(tempscore)
   print(tempscore)
   matchscore_final.append(tempscore)
   
print("=========")   
print("The final scores are", matchscore_final)
   
finalresult = (match.result)

print(match.sparklines())
matchline = match.sparklines()


# the json file where the output must be stored 
out_file = open("myfile.json", "w") 	
json.dump(matchline, out_file, indent = 6) 	
out_file.close() 

print(match.sparklines(c_symbol='1', d_symbol='0'))

matchfinalscore = (match.final_score())

winner = (match.winner())

coop = (match.cooperation())  # The count of cooperations
playerA_coop= coop[0]
playerB_coop= coop[1]

playerA_defc= playerturn- playerA_coop
playerB_defc= playerturn- playerB_coop

playerA=[playerA_coop, playerA_defc]
playerB=[playerB_coop, playerB_defc]

'''
Data to be sent to frontend:
    matchscore
    matchline
    matchfinalscore
    winner
    coop
'''
### Plotting
#import matplotlib as plt
import matplotlib.pyplot as plt

#Plotly calls
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go


x=0
scorelist=matchscore_final

A_score=[]
B_score=[]
for x in scorelist:
    A_score.append(x[0])
    B_score.append(x[1])


# libraries
import numpy as np

# set width of bar
barWidth = 0.25
  
# Set position of bar on X axis
r1 = np.arange(len(A_score))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, A_score, color='#0859c6', width=barWidth, edgecolor='white', label=text1)
plt.bar(r2, B_score, color='#d30000', width=barWidth, edgecolor='white', label=text2)

r=0
list1=[]
list2 =[]
for r in range(len(A_score)):
    list1.append("M"+ str(r+1))
    list2.append("M"+ str(r+1))
    list2.append("M"+ str(r+1))
    
print(list1)

# Add xticks on the middle of the group bars
plt.xlabel('Matches', fontweight='bold')
plt.ylabel('Match score', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(A_score))], [list1[r] for r in range(0,len(list1))])
 
# Create legend & Show graphic
plt.legend()
plt.savefig('matchscore.jpg')
plt.show()

#=======================================================================================================
#Plotly bar graph
#=======================================================================================================


#=======================================================================================================
'Interactive Pie chart'

types=['Cooperation', 'Defection']
colors = ['rgb(93,129,216)', 'rgb(93,216,181)']

specs = [[{'type':'domain'}, {'type':'domain'}]]
fig1 = make_subplots(rows=1, cols=2, specs=specs)

fig1.add_trace(go.Pie(labels=types, values=playerA, marker_colors=colors), 1, 1)
fig1.add_trace(go.Pie(labels=types, values=playerB, marker_colors=colors), 1, 2)

# Tune layout and hover info
fig1.update_traces(hoverinfo='label+percent', textinfo='none')
fig1.update(layout_title_text='Move count',
           layout_showlegend=True)

fig1 = go.Figure(fig1)
# plot(fig1)

py.plot(fig1, filename = '[Sales] Co-operation Vs. Defection Count', auto_open=False)
#====================================================================================
#old pyplot implementation
#====================================================================================
# fig1 = go.Figure(data=[go.Pie(labels=types, values=playerA)])
# fig1.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
#                   marker=dict(colors=colors, line=dict(color='#000000', width=2)))
# plot(fig1)

# fig2 = go.Figure(data=[go.Pie(labels=types, values=playerB)])
# fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
#                   marker=dict(colors=colors, line=dict(color='#000000', width=2)))
# plot(fig2)
#====================================================================================

#===========================================
# regular pie charts for testing
#===========================================
fig=plt.figure(figsize=(10,7))

plt.pie(playerA, labels=types)
plt.savefig('PlayerA_pie.jpg')
plt.show()

fig=plt.figure(figsize=(10,7))
plt.pie(playerB, labels=types)
plt.savefig('PlayerB_pie.jpg')
plt.show()

#====================================================================================

'Interactive Scatter Plot'
y=0
scorelist=matchscore_final
A_scores=[]
B_scores=[]
for x in scorelist:
    A_scores.append(x[0])
    B_scores.append(x[1])

player_score=[]
playertype= []
for i in range(playerturn-1):
    player_score.append(A_scores[i])
    playertype.append("Player A")
    player_score.append(B_scores[i])
    playertype.append("Player B")
    
print(player_score)
print(playertype)

# scatfig=plt.figure()
# ax=scatfig.add_axes([0,0,1,1])
# ax.scatter(list1, A_scores, color='r')
# ax.scatter(list1, B_scores, color='b')
# ax.set_xlabel('Matches')
# ax.set_ylabel('Scores')
# ax.set_title('Scatter plot for Match Scores')
# plt.savefig('matchscores_scatterplot.jpg')
# plt.show()
#=============================================================================
#Sactter plot 2 [create df]
#=============================================================================
import pandas as pd
import plotly.express as px


dict = {'Match': list2, 'Score': player_score, 'Type': playertype}  
    
df = pd.DataFrame(dict) 

fig = px.scatter(df, x="Match", y="Score", color="Type")

# plot(fig)
py.plot(fig, filename = '[Sales] Scatter Plot: Player Score per Match', auto_open=False)


figb = go.Figure(data=[
    go.Bar(name='Player A', x=list1, y=A_score),
    go.Bar(name='Player B', x=list1, y=B_score)
])
# Change the bar mode
figb.update_layout(barmode='group')
figb = go.Figure(figb)
#plot(figb)

py.plot(figb, filename = '[Sales] Bar Plot: Player Score per Match', auto_open=False)
#================================================================================
# figs = go.Figure()

# figs.add_trace(go.Scatter(
#     x=list1, y=A_scores,
#     name='player A',
#     mode='markers',
#     marker_color='rgb(187,51,45)',
# ))

# figs.add_trace(go.Scatter(
#     x=list1, y=B_scores,
#     name='Player B',
#     marker_color='rgb(40,166,109)'
# ))

# # Set options common to all traces with fig.update_traces
# figs.update_traces(mode='markers', marker_line_width=2, marker_size=10)
# figs.update_layout(title='Styled Scatter',
#                   yaxis_zeroline=False, xaxis_zeroline=False)

# plot(figs)
