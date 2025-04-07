from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 tests=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests

    def execute(self, context):
        postgres = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        for test in self.tests:
            sql = test.get("sql")
            expected_result = test.get("expected_result")
            
            records = postgres.get_records(sql)[0]
            if records[0] == expected_result:
                self.log.info(f"Data quality check passed for query: {sql}")
            else:
                self.log.error(f"Data quality check failed for query: {sql}")
                raise ValueError(f"Data quality check failed for query: {sql}")
        self.log.info("Data quality checks complete!")
        # self.log.info('DataQualityOperator not implemented yet')