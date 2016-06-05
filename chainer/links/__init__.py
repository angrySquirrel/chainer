"""Collection of :class:`~chainer.Link` implementations."""

from chainer.links.activation import maxout
from chainer.links.activation import prelu
from chainer.links.architecture import alex
from chainer.links.architecture import big_lstm
from chainer.links.architecture import c3d
from chainer.links.architecture import deepspeech2
from chainer.links.architecture import fc5
from chainer.links.architecture import inception_v3
from chainer.links.architecture import resnet_50
from chainer.links.architecture import small_lstm
from chainer.links.architecture import vgg
from chainer.links.connection import bilinear
from chainer.links.connection import convolution_2d
from chainer.links.connection import deconvolution_2d
from chainer.links.connection import embed_id
from chainer.links.connection import gru
from chainer.links.connection import inception
from chainer.links.connection import inceptionbn
from chainer.links.connection import linear
from chainer.links.connection import lstm
from chainer.links.connection import mlp_convolution_2d
from chainer.links.connection import parameter
from chainer.links.loss import hierarchical_softmax
from chainer.links.loss import negative_sampling
from chainer.links.model import classifier
from chainer.links.normalization import batch_normalization


Maxout = maxout.Maxout
PReLU = prelu.PReLU

Alex = alex.Alex
BigLSTM = big_lstm.BigLSTM
C3D = c3d.C3D
DeepSpeech2 = deepspeech2.DeepSpeech2
FC5 = fc5.FC5
InceptionV3 = inception_v3.InceptionV3
ResNet50 = resnet_50.ResNet50
SmallLSTM = small_lstm.SmallLSTM
VGG = vgg.VGG

Bilinear = bilinear.Bilinear
Convolution2D = convolution_2d.Convolution2D
Deconvolution2D = deconvolution_2d.Deconvolution2D
EmbedID = embed_id.EmbedID
GRU = gru.GRU
StatefulGRU = gru.StatefulGRU
Inception = inception.Inception
InceptionBN = inceptionbn.InceptionBN
Linear = linear.Linear
LSTM = lstm.LSTM
MLPConvolution2D = mlp_convolution_2d.MLPConvolution2D
Parameter = parameter.Parameter

BinaryHierarchicalSoftmax = hierarchical_softmax.BinaryHierarchicalSoftmax
NegativeSampling = negative_sampling.NegativeSampling

Classifier = classifier.Classifier

BatchNormalization = batch_normalization.BatchNormalization
