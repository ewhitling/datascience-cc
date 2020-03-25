# %% codecell
import sqlite3

# connect to the dataset
myDB = './data/cephalopod_RnD.db'
connection = sqlite3.connect(myDB)

# %% codecell
# find out what tables we have
mySQL = "SELECT type, name FROM sqlite_master;"
result = connection.execute(mySQL)
# %% codecell
print(type(result))
# %% codecell
# iterate over the results
for line in result:
    print(line)
# %% codecell
# look at the data_sources table
mySQL = "SELECT * FROM data_sources;"
result = connection.execute(mySQL)

# print only the first line
print(result.fetchone())
# %% codecell
# fetch another row
row = result.fetchone()
print(type(row))
print(row)
# %% codecell
# close the connection
connection.close()

# open the connection and create a row factory
connection = sqlite3.connect(myDB)
connection.row_factory = sqlite3.Row
# %% codecell
# look at the data_sources table
mySQL = "SELECT * FROM data_sources"
result = connection.execute(mySQL)
row = result.fetchone()

# inspect the data type of a row
print(type(row))
print(row)
# %% codecell
# look at the data_sources table
mySQL = "SELECT * FROM spady_defense"
# 'spady_defense_treatments'
result = connection.execute(mySQL)
row = result.fetchall()

for line in row:
    print(line[:])
# %% codecell

# find the column names
print(row.keys())

# print our value
print(row['Table'])

# print by index
print(row[1:3])
# %% codecell
# print our value
print(row['Table'])
# %% codecell
# look at the data_sources table
mySQL = '''
    SELECT Treatment,
        LineCrosses,
        Active,
        TimetoReact,
        ReactionType,
        InkDischarge,
        BodyPattern
    FROM spady_defense;'''
result = connection.execute(mySQL)

for line in result:
    print(line[:])
# %% codecell
# look at the data_sources table
mySQL = '''
    SELECT Treatment,
        LineCrosses,
        Active,
        TimetoReact,
        ReactionType,
        InkDischarge,
        BodyPattern
    FROM spady_defense
    WHERE Treatment = 'Mid';'''
result = connection.execute(mySQL)

print(len(result.fetchall()))
# %% codecell
# look at the data_sources table
mySQL = '''
    SELECT Treatment,
        LineCrosses,
        Active,
        TimetoReact,
        ReactionType,
        InkDischarge,
        BodyPattern
    FROM spady_defense
    WHERE Treatment <> 'Mid' and LineCrosses > 8;'''
result = connection.execute(mySQL)

print(len(result.fetchall()))
# %% codecell
# look at the data_sources table
mySQL = '''
    SELECT Treatment,
        LineCrosses,
        Active,
        TimetoReact,
        ReactionType,
        InkDischarge,
        BodyPattern
    FROM spady_defense
    WHERE Treatment <> 'Mid' and LineCrosses > 8
    ORDER BY LineCrosses;'''
result = connection.execute(mySQL)

for line in result:
    print(line[:])
# %% codecell
# look at the data_sources table
mySQL = '''
    SELECT Treatment,
        Active,
        avg(LineCrosses) as AverageLineCrosses,
        count(LineCrosses) as CountLineCrosses
    FROM spady_defense
    GROUP BY Treatment, Active
        '''
result = connection.execute(mySQL)
for line in result:
    print(line[:])
# %% codecell
mySQL = '''
    SELECT
        sd.Treatment,
        sd.Active,
        sdt.pH,
        avg(sd.LineCrosses) as AverageLineCrosses
    FROM spady_defense sd
        INNER JOIN spady_defense_treatments sdt
            on sd.Treatment = sdt.treatment
    GROUP BY sd.Treatment, sd.Active, sdt.ph
        '''
result = connection.execute(mySQL)
for line in result:
    print(line[:])
# %% codecell
