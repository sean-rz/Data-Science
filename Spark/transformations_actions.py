from pyspark import SparkContext, SparkConf

# SparkContext creates the connection to a Spark cluster
conf = SparkConf().setMaster("local").setAppName("BasicExample") # one process/thread
sc = SparkContext(conf=conf)

# Save a reference to the RDD
text_rdd = sc.textFile('example2.txt')

####################################################################################################
#Map vs flatMap
####################################################################################################
# Map a function (or lambda expression) to each line. Then collect the results.
print(text_rdd.map(lambda line: line.split()).collect())
# output: [['first'], ['second', 'line'], ['the', 'third', 'line'], ['then', 'a', 'fourth', 'line']]

# Collect everything as a single flat map
print(text_rdd.flatMap(lambda line: line.split()).collect())
# output: ['first', 'second', 'line', 'the', 'third', 'line', 'then', 'a', 'fourth', 'line']

####################################################################################################
# RDDs and Key Value Pairs
####################################################################################################
services = sc.textFile('services.txt')

print(services.take(2))

# remove # and then split
clean = services.map(lambda x: x[1:] if x[0]=='#' else x).map(lambda x: x.split())
pairs = clean.map(lambda lst: (lst[3],lst[-1]))  # grabbing fields to return state column and amount cloumn
rekey = pairs.reduceByKey(lambda amt1,amt2 : float(amt1) + float(amt2))
print(rekey.collect()) # [('State', 'Amount'), ('NY', 850.0), ('TX', 650.0), ('CA', 700.0)]

# Get rid of ('State','Amount') and then sort them by the amount value
result = rekey.filter(lambda x: not x[0]=='State').sortBy(lambda stateAmount: stateAmount[1], ascending=False)

print(result.collect()) # [('NY', 850.0), ('CA', 700.0), ('TX', 650.0)]