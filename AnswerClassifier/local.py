# coding=utf8
__author__ = 'jiangdapeng'


data_dir = 'data/'

dim = 23

def parse_sample(line):
    row = line.strip().split(" ")
    sample = [0.0 for i in range(dim+1)]
    features = map(lambda f: f.split(":"),row[2:])
    for fea in features:
        sample[int(fea[0])-1] = float(fea[1])
    return (sample,row[1])

def load_dataset():
    data_path = data_dir + 'dataset.txt'

    samples = []
    labels = []
    for line in open(data_path):
        sample = parse_sample(line)
        samples.append(sample[0])
        labels.append(sample[1])

    return (samples,labels)

def train_model(train_data):
    pass

def test_mode(model, test_data):
    pass

def main():
    dataset = load_dataset()
    train_data = dataset[:3500]
    test_data = dataset[3500:]
    model = train_model(train_data)
    result = test_mode(model,test_data)
    print(result)

if __name__ == '__main__':
    main()


