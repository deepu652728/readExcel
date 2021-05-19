from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Real-Time Data Pipeline Started ...")

spark = SparkSession \
    .builder \
    .appName("Real-Time Data Pipeline Demo") \
    .master("local[*]") \
     .config("spark.jars.packages", "com.crealytics:spark-excel_2.11:0.13.1") \
    .getOrCreate()
    # .config("spark.executor.extraClassPath", "file:///G://jars//spark-excel_2.11-0.8.2.jar") \
    # .config("spark.executor.extraLibrary", "file:///G://jars//spark-excel_2.11-0.8.2.jar") \
    # .config("spark.driver.extraClassPath", "file:///G://jars//spark-excel_2.11-0.8.2.jar") \
   # .getOrCreate()

print("Session Created")

df = spark.read.format("com.crealytics.spark.excel").\
    option("header", "true").load("C:/Users/admin/Desktop/Book1.xlsx")

print(df.show())