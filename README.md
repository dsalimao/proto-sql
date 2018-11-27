# proto-sql

*This is still in dev for first workable version.*

Protobuf is nice for defining data models, and easy to use in Python, but a bit painful to interact with relational databases.
Store the whole proto message in BLOB column is not very useful. We expect a field in proto can be mapped to a column in the db.
And proto message can have nested messages and repeated fields.
Inspired by Django models, we want to implement a developer friendly lib to 
* auto manage tables schemas based on proto structure
* fluent operations with pure Python protobuf, no need to write SQL


