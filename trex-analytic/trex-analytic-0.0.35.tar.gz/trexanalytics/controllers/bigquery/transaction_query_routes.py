'''
Created on 3 May 2021

@author: jacklok
'''

from flask import Blueprint
import logging
from trexanalytics.controllers.bigquery.query_base_routes import CategoryAndCountQueryBaseResource,\
    QueryBaseResource
from flask_restful import Api
from trexanalytics.conf import BIGQUERY_GCLOUD_PROJECT_ID, MERCHANT_DATASET
from trexlib.utils.string_util import is_not_empty
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

transaction_analytics_data_bp = Blueprint('transaction_analytics_data_bp', __name__,
                                 template_folder='templates',
                                 static_folder='static',
                                 url_prefix='/analytics/transaction')

logger = logging.getLogger('analytics')

query_transaction_data_api = Api(transaction_analytics_data_bp)

@transaction_analytics_data_bp.route('/index')
def query_transaction_index(): 
    return 'ping', 200


def process_transaction_result_into_fieldname_and_value(job_result_rows):
    row_list = []
    for row in job_result_rows:
        #logger.debug(row)
        column_dict = {}
        column_dict['date_range']           = row.date_range
        column_dict['sumTransactAmount']    = row.sumTransactAmount
        column_dict['transactionCount']     = row.transactionCount
        
        row_list.append(column_dict)
    
    return row_list

def process_transaction_result_without_dange_range_into_fieldname_and_value(job_result_rows):
    row_list = []
    for row in job_result_rows:
        #logger.debug(row)
        column_dict = {}
        column_dict['totalTransactAmount']      = row.totalTransactAmount
        column_dict['transactionCount']         = row.transactionCount
        
        row_list.append(column_dict)
    
    return row_list     

class CustomerTransactionQueryBase(QueryBaseResource):
    def process_query_result(self, job_result_rows):
        return process_transaction_result_into_fieldname_and_value(job_result_rows)
    

class QueryAllCustomerTransactionByYearMonth(CustomerTransactionQueryBase):
    def prepare_query(self, **kwrgs):
        
        date_range_from   = kwrgs.get('date_range_from')
        date_range_to     = kwrgs.get('date_range_to')
        
        where_condition  = ''
        
        if date_range_from and date_range_to:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' AND '{date_range_to}' AND ".format(date_range_from=date_range_from, 
                                                                                                         date_range_to=date_range_to)
        else:
            where_condition = "WHERE "
            
        query = '''
            SELECT FORMAT_DATETIME('%Y-%m', TransactDateTime) as date_range, sum(TotalTransactAmount) as sumTransactAmount, count(*) as transactionCount
            FROM (
                        SELECT TransactDateTime, SUM(TransactAmount) as TotalTransactAmount
                        FROM (
                            SELECT TransactDateTime, TransactionId, TransactAmount
                            FROM `{project_id}.{dataset_name}.customer_transaction_*`
                            {where_condition}
                            sSalesTransaction=true
                            GROUP BY TransactDateTime, TransactionId, TransactAmount
                        )
                        GROUP BY TransactDateTime
                     
            ) GROUP BY date_range  
            order by date_range          
            '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, where_condition=where_condition)    
            
        logger.debug('QueryAllCustomerTransactionByYearMonth: query=%s', query)
    
        return query 
    
class QueryMerchantCustomerTransactionByYearMonth(CustomerTransactionQueryBase):
    def prepare_query(self, **kwrgs):
        account_code      = kwrgs.get('account_code')
        date_range_from   = kwrgs.get('date_range_from')
        date_range_to     = kwrgs.get('date_range_to')
        
        account_code = account_code.replace('-','')
        
        where_condition  = ''
        
        if date_range_from and date_range_to:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{year_month_from}' and '{year_month_to}' AND".format(date_range_from=date_range_from, 
                                                                                                         date_range_to=date_range_to)
        else:
            where_condition = "WHERE "
            
            
        query = '''
            SELECT FORMAT_DATETIME('%Y-%m', TransactDateTime) as date_range, sum(TotalTransactAmount) as sumTransactAmount, count(*) as transactionCount
            FROM (
                        SELECT TransactDateTime, SUM(TransactAmount) as TotalTransactAmount
                        FROM (
                            SELECT TransactDateTime, TransactionId, TransactAmount
                            FROM `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                            {where_condition}
                            IsSalesTransaction=true
                            GROUP BY TransactDateTime, TransactionId, TransactAmount
                        )
                        GROUP BY TransactDateTime
                     
            ) GROUP BY date_range  
            order by date_range          
            '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, where_condition=where_condition, account_code=account_code)    
            
        logger.debug('QueryMerchantCustomerTransactionByYearMonth: query=%s', query)
    
        return query
    
class QueryMerchantCustomerTransactionByDateRange(CustomerTransactionQueryBase):
    def prepare_query(self, **kwrgs):
        account_code            = kwrgs.get('account_code')
        date_range_from         = kwrgs.get('date_range_from')
        date_range_to           = kwrgs.get('date_range_to')
        
        date_range_by_month     = kwrgs.get('date_range_by_month')
        date_range_by_year      = kwrgs.get('date_range_by_year')
        
        
        if is_not_empty(date_range_by_year) and is_not_empty(date_range_by_month):
            date_range_by_year      = int(date_range_by_year, 10)
            date_range_by_month     = int(date_range_by_month, 10)
            
            first_date_of_month     = date(date_range_by_year, date_range_by_month, 1)
            next_month              = first_date_of_month + relativedelta(months=1)
            last_date_of_month      = next_month - timedelta(days=1)
        
            date_range_from         = first_date_of_month.strftime('%Y%m%d')
            date_range_to           = last_date_of_month.strftime('%Y%m%d')
        
        
        account_code = account_code.replace('-','')
        
        where_condition  = ''
        
        if date_range_from and date_range_to:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' and '{date_range_to}' AND ".format(date_range_from=date_range_from, 
                                                                                                         date_range_to=date_range_to)
        else:
            where_condition = "WHERE "
        
        query = '''
            SELECT FORMAT_DATETIME('%Y-%m-%d', TransactDateTime) as date_range, sum(TotalTransactAmount) as sumTransactAmount, count(*) as transactionCount
            FROM (
            
                SELECT TransactDateTime, SUM(TransactAmount) as TotalTransactAmount
                        FROM (
                            
                            SELECT
                                checking_transaction.TransactDateTime as TransactDateTime, 
                                checking_transaction.TransactionId as TransactionId, 
                                checking_transaction.UpdatedDateTime, 
                                checking_transaction.TransactAmount as TransactAmount, 
                                checking_transaction.Reverted as Reverted
                                
                              FROM
                                (
                                SELECT
                                   TransactionId, MAX(UpdatedDateTime) AS latestUpdatedDateTime
                                 FROM
                                   `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                                    
                                    {where_condition}
                                    IsSalesTransaction=true
                            
                                 GROUP BY
                                   TransactionId
                                   ) 
                                   AS latest_transaction
                              INNER JOIN
                              (
                                SELECT 
                                TransactDateTime, TransactionId, UpdatedDateTime, TransactAmount, Reverted
                                FROM
                                `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                                  
                                  {where_condition}
                                  IsSalesTransaction=true
                            
                              ) as checking_transaction
                            
                            ON
                            
                            checking_transaction.TransactionId = latest_transaction.TransactionId
                            AND
                            checking_transaction.UpdatedDateTime=latest_transaction.latestUpdatedDateTime
                            
                            )
                            WHERE Reverted=False
                            GROUP BY TransactDateTime
            )
            GROUP BY date_range    
            order by date_range        
            '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, where_condition=where_condition, account_code=account_code)    
            
        logger.debug('QueryMerchantCustomerTransactionByYearMonth: query=%s', query)
    
        return query
    
class QueryMerchantCustomerTransactionTotalByDateRange(CustomerTransactionQueryBase):
    def prepare_query(self, **kwrgs):
        account_code      = kwrgs.get('account_code')
        date_range_from   = kwrgs.get('date_range_from')
        date_range_to     = kwrgs.get('date_range_to')
        
        account_code = account_code.replace('-','')
        
        where_condition  = ''
        
        if date_range_from and date_range_to:
            where_condition = "WHERE _TABLE_SUFFIX BETWEEN '{date_range_from}' and '{date_range_to}' AND ".format(date_range_from=date_range_from, 
                                                                                                         date_range_to=date_range_to)
        else:
            where_condition = "WHERE "
        
        query = '''
            
                        SELECT SUM(TransactAmount) as totalTransactAmount, count(*) as transactionCount
                        FROM (
                            
                            SELECT
                                checking_transaction.TransactDateTime as TransactDateTime, 
                                checking_transaction.TransactionId as TransactionId, 
                                checking_transaction.UpdatedDateTime, 
                                checking_transaction.TransactAmount as TransactAmount, 
                                checking_transaction.Reverted as Reverted
                                
                              FROM
                                (
                                SELECT
                                   TransactionId, MAX(UpdatedDateTime) AS latestUpdatedDateTime
                                 FROM
                                   `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                                    
                                    {where_condition}
                                    IsSalesTransaction=true
                            
                                 GROUP BY
                                   TransactionId
                                   ) 
                                   AS latest_transaction
                              INNER JOIN
                              (
                                SELECT 
                                TransactDateTime, TransactionId, UpdatedDateTime, TransactAmount, Reverted
                                FROM
                                `{project_id}.{dataset_name}.customer_transaction_{account_code}_*`
                                  
                                  {where_condition}
                                  IsSalesTransaction=true
                            
                              ) as checking_transaction
                            
                            ON
                            
                            checking_transaction.TransactionId = latest_transaction.TransactionId
                            AND
                            checking_transaction.UpdatedDateTime=latest_transaction.latestUpdatedDateTime
                            
                            
                        )
                        WHERE Reverted=False
                     
                   
            '''.format(project_id=BIGQUERY_GCLOUD_PROJECT_ID, dataset_name=MERCHANT_DATASET, where_condition=where_condition, account_code=account_code)    
            
        logger.debug('QueryMerchantCustomerTransactionByYearMonth: query=%s', query)
    
        return query    
    
    def process_query_result(self, job_result_rows):
        return process_transaction_result_without_dange_range_into_fieldname_and_value(job_result_rows)
    

query_transaction_data_api.add_resource(QueryAllCustomerTransactionByYearMonth,   '/all-transaction-by-year-month')
query_transaction_data_api.add_resource(QueryMerchantCustomerTransactionByYearMonth,   '/merchant-transaction-by-year-month')
query_transaction_data_api.add_resource(QueryMerchantCustomerTransactionByDateRange,   '/merchant-transaction-by-date-range')
query_transaction_data_api.add_resource(QueryMerchantCustomerTransactionTotalByDateRange,   '/merchant-transaction-total-by-date-range')


