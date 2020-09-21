import matplotlib.pyplot as plt
import numpy as np
import random



def uniform_dataset(words,weightList):
    size = 1000000
    x=np.random.uniform(30.0273437,60.02734375,size)
    y=np.random.uniform(35.87531083569679,45.87531083569679,size)
    visualization(x,y)
    generate_dataset(words,weightList,x,y,'uniform_dataset.txt')
        

def non_uniform_dataset(words,weightList):

    clusters = 5
    size = 1000000
    
    x_center = [30.02734375,40.02734375,50.02734375,60.02734375,70.02734375]

    y_center = [55.87531083569679,45.87531083569679,35.87531083569679,25.87531083569679,15.87531083569679]

    scales = [0.25,0.8,0.42,0.11,0.55]

    for i in range(clusters):
        if i == 0:
            x = np.random.normal(loc=x_center[i], scale=scales[i], size=size)
            y = np.random.normal(loc=y_center[i], scale=scales[i], size=size)
            continue
        x = np.hstack([x, np.random.normal(loc=x_center[i], scale=scales[i], size=size)])
        y = np.hstack([y, np.random.normal(loc=y_center[i], scale=scales[i], size=size)])
        
    visualization(x,y)
    generate_dataset(words,weightList,x,y,'non_uniform_dataset.txt')


def visualization(x,y):
    
    BBox =(-180, 180,-90,90)
    ruh_m = plt.imread('gen_uni_1.png')

    fig, ax = plt.subplots(figsize = (8,7))
    ax.scatter(x, y, zorder=1, alpha= 0.2, c='b', s=13)
    ax.set_title('Uniform Dataset')
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
    plt.show()


def generate_dataset(words,weightList,x,y,file):

    with open(file, "w") as f:  
      for i in range(len(x)):
        r = int(random.uniform(1, 5))
        keywords=[]
        for j in range(r):
            if not keywords:
                
                keywords.append(','.join(random.choices(words, weights=weightList, k=1)))
            else:
                temp=random.choices(words, weights=weightList, k=1)
                if temp in keywords:
                    j=j-1
                    continue
                else:
                    keywords.append(','.join(temp))         
                                                     
        finalkeywords = ','.join(keywords)
        
        f.write("2|" + str(x[i]) + "|" + str(y[i]) + "|" + finalkeywords + "\n")

def main():
    words=[]
    weightList=[]
    count=1
    file = open("keywords.txt","r",encoding='utf-8')
    for line in file:
        fields = line.split("\n")
        words.append(fields[0])
        if count <=3000:
            weightList.append(10)
        elif count>3000 and count <=6000:
            weightList.append(30)
        else:
            weightList.append(60)
        count=count+1    
    uniform_dataset(words,weightList)
    non_uniform_dataset(words,weightList)
    

if __name__=="__main__":
    main()

