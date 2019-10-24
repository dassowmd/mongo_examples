from mongoengine import connect, Document, StringField, ReferenceField, ListField
from pprint import pprint

connect('playground'
        , host='localhost'
        , port=27017
        # , username='webapp'
        # , password='pwd123'
        # , authentication_source='admin'
        )

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    meta = {'collection' : 'users'}

class Course(Document):
    name = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))

    meta = {'allow_inheritance': True
            , 'collection': 'courses'}

# Create example
new_user = User(email='ross@example.com', first_name='Ross', last_name='Lawley')
new_user.save()

course1 = Course(name='Fun with MongoEngine', author=new_user)
course1.content = 'Took a look at MongoEngine today, looks pretty cool.'
course1.tags = ['mongodb', 'mongoengine']
course1.save()

course2 = Course(name='MongoEngine Documentation', author=new_user)
course2.content = 'More looking. Getting cooler'
course2.tags = ['mongoengine']
course2.save()

# Read example
# searching all objects
for course in Course.objects:
    print(course.name)

# searching by field on object
for user in User.objects(first_name="Ross"):
    print(user.last_name)

# searching by field on NESTED object - note the '__' # TODO not currently working due to bad data in the database (users not linked to courses)
# for course in Course.objects(author__first_name='Ross'):
#     print(course.name)

# Update example
user = User.objects(first_name="Ross")[0]
user.first_name = "Matt"
user.save()

# Delete example
user = User.objects(first_name="Ross")[0]
user.delete()