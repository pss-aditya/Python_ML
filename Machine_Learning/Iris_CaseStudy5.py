from sklearn.datasets import load_iris

def main():
    print("-"*35)
    print("Iris Classification  Case Study")
    print("-"*35)
    
    Dataset  = load_iris()

    for i in range(len(Dataset.target)):
        print("ID  %d, Features %s, Label %s" %(i,Dataset.data[i],Dataset.target[i]))



if __name__ == "__main__":
    main()