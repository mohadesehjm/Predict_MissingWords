# Predict_MissingWords
Masked-Language Modeling With BERT

## What is BERT?

BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based method of learning language representations. It is a bidirectional transformer pre-trained model developed using a combination of two tasks namely: masked language modeling objective and next sentence prediction on a large corpus.

Through Pytorch-transformers we can use Bert’s pre-trained language model for pridicting missing words. We can also finetune Bert’s pre-trained language model to fit our task and then use that model to gain some improvements.

## What is the purpose of this project?

In this project, I recognized verbs in sentences and then other verbs were predicted by Bert, which they could be replaced in that position of sentences. I created 6 levels for prediction and Chose best options for selecting to show in site.

e.g.

![sample](https://user-images.githubusercontent.com/38848389/151368278-3095933e-628f-4d90-bad0-20c960adbc98.jpg)



### Masked-Language Modeling With BERT

Two ways were implemented by Bert and we figure out almost same result for using directly bert model and finetuned language model because our dataset was written in English.

If our data is different than the data used for pretraining, the results would not be that satisfactory. Consider for example if we have a mix of Persian and English language data and we are using a pre-trained model trained on Wikipedia, it would lead to bad results. In that scenario, we need to fine-tune our language model. But, if we have English dataset we do not need finetune our model.
