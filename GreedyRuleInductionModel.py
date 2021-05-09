


class GreedyRuleInductionModel(LearnedRuleModel):
    
    def __init__(self,maxRules=10, increments=25):
        # call the init function for the super class
        # and inherit all the other methods
        super().__init__(maxRules=maxRules, increments=increments)


        
    def fit( self,train_X,train_y):
      #  Preprocess (trainingset)  
      # store the set of different labels - don't assume theyare 0,12,2 etc
        self.labels = np.unique(train_y)

        # remember how many features there are describing each trainig case
        self.numFeatures= train_X.shape[1]
        
        # preprocess the data to compute the set of thresholds  to be used in rules
        # there are self.numThresholds of these for each feature
        self.CalculatePossibleThresholds(train_X)
        
        numOperators = 3
        score = 0
#         [self.numFeatures , numOperators , threshold_id , CalculatePossibleThresholds(train_X)]
        # now to learn from the data
        
        ###== YOUR CODE HERE====####
            ## I suggest you copy in the pseudocode from the lecture then code to that
            ## some of the lines in that pseudocode have been covered above
            ## and some are covered in the init() method
            
#        WHILE (currentModel.score<trainingsetSize and numRule < maxRules) DO 
        while score < self.numFeatures and self.numRules < self.maxRules:
#            SET bestchild = emptyModel
                bestchild = self.ruleSet.copy()
                bestchildscore = score
#            FOR newRule in (all_possible_rules) 
                for newRule in range(self.numFeatures):
                    print(newRule)
#                SET newModel = COPY(currentModel)
#                     newModel = bestchild.copy()
# # # #                SET newModel = ADDRULE (newModel, newRule)
#                     newModel = np.add(newModel , newRule)
# # #                SET score = SCORE(newModel)
#                     score = self.Score(newModel, newRule, train_X,train_y)
#                     print(score)
# #                IF (newModel.score > bestChild.score)
#                     if score > bestchildscore:
# # #                   SET bestChild= COPY(newModel)
#                         bestchild = newModel.copy()
# # #             IF (bestChild.score > currentModel.score)
#                     if bestchildscore > score:
# # #                SET currentModel=COPY (bestChild)
#                         self.ruleSet = self.ruleSet.copy()
# #                  #SET numRules += 1
#                         self.numRules ++1 
#         return self.ruleSet
#         print(newModel)
#        RETURN currentModel
        

        
    
    def predict(self, examples):
        ypred = np.zeros(examples.shape[0],-999, dtype=np.uint)
 
   
    
        ###== YOUR CODE HERE====####
            ## I suggest you start by setting everything in ypred to a valid default value
            ## i.e. something from the list self.labels
            
            ## then you will find it useful to look at the score() method in the super class
            ## to see how you can try to match rules from your ruleset  for each  test instance in turn
        
        
        # Loop over each example to make predictions about
#         for example in examples:
           # Loop over each rule in model
#             if example
               # Check if example matches rules conditions (HINT: look at score())
                   # Set this example prediction to prediction of rule

       # Set a default prediction e.g. self.labels[0]
       # For each prediction
           #If prediction is default (-1)
               # Set prediction to first class/label e.g. self.labels[0]

        
        return ypred
    


