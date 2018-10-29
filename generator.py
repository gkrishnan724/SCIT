import numpy as np
import matplotlib.pyplot as plt
import os
import random


def plot(dataset,dirname,label):
    data = open(dirname+'data.csv','w')
    data.write(','.join(map(str,dataset)))
    data.close()
    if label == "Normal":
        color = "blue"
    else:
        color = "orange"
    plt.hist(dataset,color=color,label=label)
    plt.ylabel('Frequency')
    plt.savefig(dirname+'graph.png')
    plt.cla()

def plotAverage(normdata,poissdata,dirname,rsize,gsize):
    dataset = []
    normset = []
    poisset = []
    for i in range(rsize):
        index = random.randint(0,gsize-1)
        avg = (normdata[index] + poissdata[index])/float(2)
        dataset.append(avg)
        poisset.append(poissdata[index])
        normset.append(normdata[index])
    data = open(dirname+'data.csv','w')
    data.write(','.join(map(str,dataset)))
    data.close()
    plt.hist(normset,color="blue",label='Normal')
    plt.hist(poisset,color="orange",label='Poission')
    plt.hist(dataset,color="green",label='Averaged')
    plt.ylabel('Frequency')
    plt.savefig(dirname+'combinedgraph.png')
    plt.cla()
    plt.hist(dataset,color="green")
    plt.ylabel('Frequency')
    plt.savefig(dirname+'graph.png')
    plt.cla()
    
data_size = 1000
graphs = 'Graphs/'
if not os.path.exists(graphs):
    os.makedirs(graphs)

for i in range(100):
    poissplots = np.random.poisson(lam=i+1,size=data_size)
    normplots = np.random.normal(loc=i+1,size=data_size)
    expdir = graphs+'Experiment'+str(i+1)+'/'
    ndir = expdir+'Normal/'
    pdir = expdir+'Poission/'
    avgdir = expdir+'Average/'
    if not os.path.exists(expdir):
        os.makedirs(ndir)
        os.makedirs(pdir)
        os.makedirs(avgdir)
    
    plot(normplots,ndir,'Normal')
    plot(poissplots,pdir,'Poisson')
    plotAverage(normplots,poissplots,avgdir,100,1000)
    


