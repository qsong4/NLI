# Attention-Based Convolutional Neural Network for Modeling Sentence Pairs(ABCNN)
> This is a simple version of ABCNN depend on tensorflow.\
> The code is fork from <https://github.com/pengming617/text_matching>, and I just do some simple changes and fix some bugs.

This is the implementation of ABCNN, I use this model to compute the similarity of two sentences. The acc is 93.33% on test set, but the performance is bad on
long sentences, and the result is at below.

acc decrease since length of sentence increase:

| Length | 0-5 | 5-10 | 10-20 | 20-30 | 30-40 | >40 |
| :---: |  :---:  | :---:  |  :---:  |  :---: | :---: | :---: |
| ACC | 0.98 | 0.88 | 0.81 | 0.56 | 0.47 | 0.28 |

I will discuss the reason at the end.

## Data
The train data(TSV) use 4 million sentence pairs, and there are 60% pair tag 1, other tag 0.<br>
There are some tips for build data set 
1. Be careful about data balance, not only the tag1 and tag0, but also on sentence length and the tag balance on each length. This model perform bad on long sentence especially longer than 30 words.
2. Be careful about the quantity of data set, at first I can not train reasonable model no matter how I change the params, this is because the data set has lots of noise. You can use some classification model to 
clean the data set.

## Model
In the paper there are 3 type of model, ABCNN1,2,3. They are different at the place of attention. I use ABCNN3 because it's perform better at different data set.
The implement detail can see the code. The code is not perfect, I will update it in the future. The TODO list is at below:
1. Add pre-trained word embedding.
2. The model right now can only add two CNN layer, I will change it to support more layers.
3. I did not use l2 loss in the original code, because the loss is very big when i add l2 loss. I still not find the reason why.

## params
I did not do many params work, I only try to modify learning rate, batch size, embedding size and kernel number etc.

| lr | batch size | acc | f1 |
| :---: |:---: | :---: | :---: |
|0.08|128|0.90|0.90|
|0.1|64|0.88|0.88|
|0.08|300|0.90|0.90|
|0.008|50|0.89|0.89|

## TIP
1. Some times the loss is nan, this is because tf.sqrt(), you need to add a very small number "+1e-8"
2. Tuning is not that important, data is more important, so how to build reasonable data set is very importent.

## Problem
This model is try to use on a intent classification, but it's perform bad than ESIM. ESIM also perform not that good
at long sentence. I think this is because data set(see data part), and the recall of ES. When sentence longer than 30
words, the ES can only recall small part of sentence with right intent. The ES recall result is at below.<br>
The total number of sentence is 176:

| ES hit num | 0-1 | 1-5 | 5-10 | 10-15 | 15-30 | 30-n |
| :---: |:---:|:---:|:---:|:---:|:---:|:---:|
| recall30 | 35 | 58 | 17 | 15 | 13 | 35 |
| recall10 | 46 | 55 | 75 | 0 | 0 | 0 |

