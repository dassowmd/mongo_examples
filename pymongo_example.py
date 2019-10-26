from pymongo import MongoClient, ReturnDocument

import datetime
from pprint import pprint

class mongo_obj:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['playground'] # select the database that you would like to use
        self.courses = self.db.courses

    # Insert a course
    def insert_course(self, course):
        course_id = self.courses.insert_one(course).inserted_id
        return course_id


    # Insert Many
    def insert_courses(self, course_list):
        result = self.courses.insert_many(course_list)
        return result

    def update_course(self, id, course):
        res = self.courses.find_one_and_update(
             {'_id': id},
            {'$set' : course},
             return_document=ReturnDocument.AFTER)
        return res

    # Query a course
    def query_course(self, query_params=None):
        if query_params:
            query_course = self.courses.find_one(query_params)
            return query_course
        else:
            query_course = self.courses.find_one(query_params)
            return query_course

    # Query many courses
    def query_many_courses(self, query_params=None):
        courses = []
        if query_params:
            res = self.courses.find(query_params)
        else:
            res = self.courses.find()
        for course in res:
            courses.append(course)
        return courses

    # Count documents
    def get_course_count(self, query_params=None):
        if query_params:
            return self.courses.count_documents(query_params)
        else:
            return self.courses.count_documents({})


    def delete_many(self, query_params):
        # Delete Documents
        return self.courses.delete_many(query_params)

if __name__=='__main__':
    db_obj = mongo_obj()


    course = {"author": "Matt",
            "name" : "Pymongo",
             "tags": ["mongodb", "python", "pymongo"],
             "date": datetime.datetime.utcnow(),
            "isPublished": True}
    c = db_obj.insert_course(course=course)

    new_courses = [{"author": "Mike",
                    "name": "Another course!",
                    "tags": ["bulk", "insert"],
                    "date": datetime.datetime(2009, 11, 12, 11, 14)},
                   {"author": "Eliot",
                    "title": "MongoDB is fun",
                    "tags": "and pretty easy too!".split(' '),
                    "date": datetime.datetime(2009, 11, 10, 10, 45)}]
    courses = db_obj.insert_courses(course_list=new_courses)

    query_params = {"author": "Mike"}
    res = db_obj.query_course(query_params=query_params)
    print(res)

    res = db_obj.query_many_courses(query_params=query_params)
    print(res)

    delete_query_params = {'title': {'$exists': True}}

