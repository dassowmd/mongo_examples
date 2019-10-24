from pymongo import MongoClient
import datetime
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

db = client['playground'] # select the database that you would like to use

course = {"author": "Matt",
        "name" : "Pymongo",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow(),
        "isPublished": True}

courses = db.courses

# Insert a document
course_id = courses.insert_one(course).inserted_id
print(course_id)

# Insert Many
new_courses = [{"author": "Mike",
               "name": "Another course!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "tags": "and pretty easy too!".split(' '),
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = courses.insert_many(new_courses)
print(result.inserted_ids)

# Query a document
query_course = courses.find_one({'author': 'Matt'})
pprint(query_course)

# Query many documents
for course in courses.find({"author": "Mike"}):
    pprint(course)

# Count documents
print(courses.count_documents({})) # Count all
print(courses.count_documents({"author": "Mike"})) # with filter

# Delete Documents
courses.delete_many({'title': {'$exists': True}})