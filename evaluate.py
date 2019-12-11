'''
Created on Apr 15, 2016
Evaluate the performance of Top-K recommendation:
    Protocol: leave-1-out evaluation
    Measures: Hit Ratio and NDCG
    (more details are in: Xiangnan He, et al. Fast Matrix Factorization for Online Recommendation with Implicit Feedback. SIGIR'16)

@author: hexiangnan
'''
import math
import heapq # for retrieval topK
import multiprocessing
import numpy as np
from time import time
#from numba import jit, autojit

# Global variables that are shared across processes
_model = None
_testRatings = None
_testNegatives = None
_testImFeatures = None
_K = None

def evaluate_model(model, testRatings, testNegatives, testImFeatures, K, num_thread):
    """
    Evaluate the performance (Hit_Ratio, NDCG) of top-K recommendation
    Return: score of each test rating.
    """
    global _model
    global _testRatings
    global _testNegatives
    global _testImFeatures
    global _K
    _model = model
    _testRatings = testRatings
    _testNegatives = testNegatives
    _testImFeatures = testImFeatures
    _K = K
        
    hits, ndcgs = [],[]
    if(num_thread > 1): # Multi-thread
        pool = multiprocessing.Pool(processes=num_thread)
        res = pool.map(eval_one_rating, range(len(_testRatings)))
        pool.close()
        pool.join()
        hits = [r[0] for r in res]
        ndcgs = [r[1] for r in res]
        return (hits, ndcgs)
    # Single thread
    for idx in xrange(len(_testRatings)):
        (hr,ndcg) = eval_one_rating(idx)
        hits.append(hr)
        ndcgs.append(ndcg)      
    return (hits, ndcgs)

def eval_one_rating(idx):
    rating = _testRatings[idx]
    # rating = (user, item, rating)
    # need to pass matrix of item features for all imgs in items
    items = _testNegatives[idx]
    # print(items)
    # items = (user, item) [item1, item2, ...]
    # print("item features idx shape = ", np.shape([_testImFeatures[items]]))
    # print("item features shape = ", np.shape(np.array(item_features)))
    u = rating[0]
    gtItem = rating[1]
    items.append(gtItem)
    item_features = list(np.array([_testImFeatures[items]])[0])
    # Get prediction scores
    map_item_score = {}
    users = np.full(len(item_features), u, dtype = 'int32')
    # print "item shape: " + str(np.shape(item_features))
    predictions = _model.predict([users, np.array(item_features)], 
                                 batch_size=100, verbose=0)
    # print("evaluating for " + str(idx))
    # print "prediction length: " + str(predictions.shape)
    for i in xrange(len(items)):
        # item_feat = item_features[i]
        map_item_score[items[i]] = predictions[i]
    item_features.pop()
    
    # Evaluate top rank list
    ranklist = heapq.nlargest(_K, map_item_score, key=map_item_score.get)
    hr = getHitRatio(ranklist, gtItem)
    ndcg = getNDCG(ranklist, gtItem)
    return (hr, ndcg)

def getHitRatio(ranklist, gtItem):
    for item in ranklist:
        if item == gtItem:
            return 1
    return 0

def getNDCG(ranklist, gtItem):
    for i in xrange(len(ranklist)):
        item = ranklist[i]
        if item == gtItem:
            return math.log(2) / math.log(i+2)
    return 0
