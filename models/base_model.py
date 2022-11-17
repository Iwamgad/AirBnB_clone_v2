#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import uuid
from os import getenv
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, time)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """ models.storage.new(self)"""

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        newDict = self.__dict__.copy()
        if "created_at" in newDict:
            newDict["created_at"] = newDict["created_at"].strftime(time)
        if "updated_at" in newDict:
            newDict["updated_at"] = newDict["updated_at"].strftime(time)
        newDict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in newDict:
            del newDict["_sa_instance_state"]
        return newDict
    def delete(self):
        """Deletes instance from storage"""
        models.storage.delete(self)
