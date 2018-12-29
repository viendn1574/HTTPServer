import numpy
import pandas

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.tools.xml import NetworkWriter


seed = 7
numpy.random.seed(seed)

def add_model(dataset):
    ds = ClassificationDataSet(108,1,nb_classes=2)
    dataframe = pandas.read_csv("./train.csv", delimiter=" ",header=None)
    data_train = dataframe.values
    data_train=numpy.concatenate((data_train,dataset))
    input=data_train[:,1:109].astype(float)
    target=data_train[:,0]
    target = numpy.reshape(target, (-1, 1))
    ds.setField('input', input)
    ds.setField('target', target)
    ds._convertToOneOfMany()
    net = buildNetwork(ds.indim, 50, ds.outdim, outclass=SoftmaxLayer)
    def train():
        back=BackpropTrainer(net,ds,learningrate = 0.0001, momentum = 0.1,verbose=True, weightdecay=0.1)
        #back.trainUntilConvergence(verbose=True)
        back.trainEpochs(100)
        NetworkWriter.writeToFile(net, './model.xml')
    train()
