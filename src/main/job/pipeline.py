import pyspark.sql.functions as F
import pyspark.sql.types as T
from dateutil import parser
from pyspark.sql import SparkSession, DataFrame

from src.main.base import PySparkJobInterface


class PySparkJob(PySparkJobInterface):

    def __init__(self):
        self.spark = SparkSession \
            .builder \
            .appName("Covid19 Vaccination Progress") \
            .getOrCreate()

    def init_spark_session(self) -> SparkSession:
        pass

    def count_available_vaccines(self, vaccines: DataFrame) -> int:
        pass

    def find_earliest_used_vaccine(self, vaccines: DataFrame) -> str:
        pass

    def total_vaccinations_per_country(self, vaccines: DataFrame) -> DataFrame:
        pass
