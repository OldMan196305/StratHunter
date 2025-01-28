# File to build initial database tables

from readline import set_completion_display_matches_hook
import sqlite3



con = sqlite3.connect("./.App/StratHunter.db")
cur = con.cursor()

#   * UserTable             // User information
#   * CredentialsTable      // Holds Credentials and keys for Users and Brokers
#   * BrokerTable           // Broker information
#   * BrokerAccountTable    // Brokers may allow multiple internal accounts
#   * BrokerFeeTable        // Brokers may have multiple fees associated with different Securities
#   * SecuritiesTable       // Securities held
#   * PriceDataTable        // holds historic data to run backtests with.

# Create Table Template
# cur.execute("CREATE TABLE <name>(
#           _Index INTEGER NOT NULL PRIMARY KEY,
# ")

#   * UserTable         // User information
res01 = cur.execute("CREATE TABLE User(
            User_Index INTEGER NOT NULL PRIMARY KEY,
            User_ID TEXT NOT NULL,      # Application Username
            Cr_ID TEXT NOT NULL,        # Link to Credentials Table
            FirstName TEXT NOT NULL, 
            LastName TEXT NOT NULL)
")

res02 = cur.execute("CREATE TABLE credentials(
            Cr_Index INTEGER NOT NULL PRIMARY KEY,
            Cr_ID TEXT NOT NULL,            # ID used to link to this table
            Cr_Salt TEXT NOT NULL,          # Salt value used to create and verify Cr_hash
            Cr_hash TEXT NOT NULL,          # hash value in HEX
            User_ID TEXT NOT NULL,          # link to User Table
")

res03 = cur.execute("CREATE TABLE securities(
            Sec_Index INTEGER NOT NULL PRIMARY KEY,
            Sec_ticker TEXT NOT NULL,       # Ticker symbol of Security purchased
            Sec_timestamp TEXT NOT NULL,    # DateTime purchased
            Sec_name TEXT NOT NULL,         # Name of Security purchased
            Sec_qty TEXT NOT NULL,          # Quantity Purchased
            Sec_price TEXT NOT NULL,        # Purchase Price
            Sec_notes TEXT NOT NULL,        # notes related to this Security
")

res04 = cur.execute("CREATE TABLE pricedata(
            Pri_Index INTEGER NOT NULL PRIMARY KEY, 
            Pri_timestamp TEXT NOT NULL,    # DateTime of data
            Pri_ticker TEXT NOT NULL,       # Ticker symbol of Security purchased
            Pri_timeseries TEXT NOT NULL,   # Time Series of data i.e. (1min, 5min, 1hour, 1day, etc.)
            Pri_name TEXT NOT NULL,         # Name of Security
            Pri_open TEXT NOT NULL,
            Pri_high TEXT NOT NULL,
            Pri_low TEXT NOT NULL,
            Pri_close TEXT NOT NULL,
            Pri_volume TEXT NOT NULL
")

res05 = cur.execute("CREATE TABLE broker(
          Broker_Index INTEGER NOT NULL PRIMARY KEY, 
          Broker_ID             # Application asigned ID
          Broker_Number         # Account number from Broker
          Broker_Name           # Brokerage Name
          Broker_User_Name      # Username used to login to Brokerage account
          BroAcc_Number         # Link to Account Number table
          Broker_Fees           # Link to Fees table
")

res06 = cur.execute("CREATE TABLE brokerassets(
          BroAcc_Index INTEGER NOT NULL PRIMARY KEY, 
          Broker_ID             # Link to broker table
          BroAcc_Number         # Account number from Broker // possible multiple internal accounts
          BroAcc_Currency       # Currency you use with the Broker
          Sec_ticker            # Link to Securities table
          BroAcc_Quantity       # Quantity of Security in this account
")

res07 = cur.execute("CREATE TABLE brokerfees(
          BroFee_Index INTEGER NOT NULL PRIMARY KEY, 
          BroFee_ID         # ID number for fee
          BroFee_Name       # Name to help you identify different fees
          BroFee_Amount     # Fee based on set price
          BroFee_Percent    # Fee based on Percentage of Purchase Price or Security Quantity
")



con.commit()    # make sure all changes are commited to the Database
