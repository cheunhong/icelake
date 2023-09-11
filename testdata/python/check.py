import argparse
import unittest
from pyspark.sql import SparkSession


def check(args):
    tc = unittest.TestCase()
    spark = SparkSession.builder.remote(args.sparkurl).getOrCreate()

    sql1 = args.sql1
    sql2 = args.sql2
    print(f"Executing sql: {sql1}")
    df1 = spark.sql(sql1).collect()
    print(f"Len of df1: {len(df1)}")
    print(f"Executing sql: {sql2}")
    df2 = spark.sql(sql2).collect()
    print(f"Len of df2: {len(df2)}")

    tc.assertEqual(df1, df2)
    # diff_df = df1.exceptAll(df2).collect()
    # tc.assertEqual(len(diff_df), 0)

    # diff_df = df2.exceptAll(df1).collect()
    # tc.assertEqual(len(diff_df), 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test icelake with spark")
    parser.add_argument("-s", dest="sparkurl", type=str, help="Spark remote url")
    parser.add_argument("-q1", dest="sql1", type=str, help="query sql 1")
    parser.add_argument("-q2", dest="sql2", type=str, help="query sql 2")
    check(parser.parse_args())
