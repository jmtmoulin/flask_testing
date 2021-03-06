from crypt import methods
from flask import Flask, request, render_template, abort, jsonify
import os
import json
import pytest

STUDENT_DATA = [
    {
        "id": 1,
        "first_name": "Travis",
        "last_name": "Smith",
        "date_of_birth": "2007-03-12",
        "grade": 8,
        "phone": "323-952-2520",
        "email": "tsmith@email.com"
    },
    {
        "id": 2,
        "first_name": "Michael",
        "last_name": "Chau",
        "date_of_birth": "2005-05-13",
        "grade": 10,
        "phone": "206-747-5631",
        "email": "mchau@domain.net"
    },
    {
        "id": 3,
        "first_name": "Agnes",
        "last_name": "Isham",
        "date_of_birth": "2009-12-03",
        "grade": 6,
        "phone": "616-889-9443",
        "email": "agnes@domain.com"
    },
    {
        "id": 4,
        "first_name": "Mary",
        "last_name": "Adkins",
        "date_of_birth": "2007-05-21",
        "grade": 8,
        "phone": "323-952-2520",
        "email": "madkins@domain.com"
    },
    {
        "id": 5,
        "first_name": "Joanna",
        "last_name": "Dubuc",
        "date_of_birth": "2009-10-01",
        "grade": 6,
        "phone": "907-251-1446",
        "email": "jdubuc@domain.net"
    },
    {
        "id": 6,
        "first_name": "Darryl",
        "last_name": "Cook",
        "date_of_birth": "2005-05-13",
        "grade": 10,
        "phone": "513-254-0691",
        "email": "dcook@domain.net"
    },
    {
        "id": 7,
        "first_name": "Robert",
        "last_name": "Tables",
        "date_of_birth": "2006-02-03",
        "grade": None,
        "phone": "270-319-7131",
        "email": "bobbyt@domain.net"
    },
    {
        "id": 8,
        "first_name": "Diana",
        "last_name": "Owens",
        "date_of_birth": "2009-12-21",
        "grade": 6,
        "phone": "425-210-0421",
        "email": "diana@email.com"
    },
    {
        "id": 9,
        "first_name": "Carl",
        "last_name": "Baxter",
        "date_of_birth": "2009-12-21",
        "grade": 6,
        "phone": "425-347-3725",
        "email": "carl.baxter@email.com"
    },
    {
        "id": 10,
        "first_name": "Shawnna",
        "last_name": "Newson",
        "date_of_birth": "2005-11-19",
        "grade": 10,
        "phone": "607-725-8122",
        "email": "shawnna@email.com"
    },
    {
        "id": 11,
        "first_name": "Wilma",
        "last_name": "Bradshaw",
        "date_of_birth": "2005-10-09",
        "grade": 10,
        "phone": "330-998-5125",
        "email": "wilmabradshaw@email.com"
    },
]

@pytest.mark.parametrize("std_id", 1)
def students_id_endpoint(std_id):
    print(str(std_id))
    assert isinstance(int(std_id), int)
    # assert int(std_id) == 1
    found_dict = {}
    print("TESTING")
    for list_dict in STUDENT_DATA:
        if int(std_id) == int(list_dict['id']):
            found_dict = list_dict

    if len(found_dict) == 0:
        print("NOT FOUND")
        #return ("", 404)

    else:
        if request.method == "GET":
            print("FOUND")
            #return jsonify(found_dict)

        elif request.method == "PATCH":
            for key,value in request.get_json().items():
                if key in found_dict.keys():
                    if key != "id":
                        found_dict[key] = value


            #return (jsonify(found_dict), 200)
            
            

