from pyspark import SparkContext, SparkConf

# SparkContext creates the connection to a Spark cluster
conf = SparkConf().setMaster("local").setAppName("BasicExample") # one process/thread
sc = SparkContext(conf=conf)

textFile = sc.textFile('example.txt') # RDD of strings

# Actions
print(textFile.count())
print(textFile.first())

# Transformations
# The transformations won't display an output and won't be run until an action is called.
secfind = textFile.filter(lambda line: 'second' in line) # new RDD

# Perform action on transformation
print(secfind.collect())
# Perform action on transformation
print(secfind.count())
