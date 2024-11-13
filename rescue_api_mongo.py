from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel
from typing import List
import json
import datetime
import os
import time

class RescueAPIMongo:
    def __init__(self):
        # Initialize MongoDB connection
        self.client = MongoClient('mongodb+srv://admin:SafeGuardian@cluster0.ropb4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        
        
        # Load JSON template
        with open('configs/victim_json_template_flat.json', 'r') as f:
            self.json_template = json.load(f)

        # Set up database and collection
        self.db = self.client['disaster_rescue']
        self.collection = self.db['rescue_team_dataset']

        # Initialize FastAPI
        self.app = FastAPI()

    def set_key(self, json_data):
        # Insert document and return the ID
        result = self.collection.insert_one(json_data)
        return str(result.inserted_id)

    def update_time_and_status(self, victim_id, time, rescue_status, emergency_status):
        self.collection.update_one(
            {'_id': ObjectId(victim_id)},
            {'$set': {
                'last_updated': time,
                'rescue_status': rescue_status,
                'emergency_status': emergency_status
            }}
        )

    def update_(self, victim_id, json_data):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            # Update document
            self.collection.update_one(
                {'_id': ObjectId(victim_id)},
                {'$set': json_data}
            )
            self.update_time_and_status(
                victim_id, 
                time, 
                json_data.get('rescue_status'), 
                json_data.get('emergency_status')
            )
        except:
            self.update_time_and_status(
                victim_id,
                time,
                'pending',
                'low_priority'
            )

    def post_victim(self, victim: dict):
        try:
            victim_number = self.set_key(self.json_template)
            return victim_number
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_victim_info(self, victim_number: str):
        victim_info = self.collection.find_one({'_id': ObjectId(victim_number)})
        if not victim_info:
            raise HTTPException(status_code=404, detail="Victim not found")
        victim_info['_id'] = str(victim_info['_id'])  # Convert ObjectId to string
        return victim_info

    def get_all_victims(self):
        try:
            victims = list(self.collection.find({}))
            # Convert ObjectIds to strings
            for victim in victims:
                victim['_id'] = str(victim['_id'])
            return victims if victims else {}
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def update_victim(self, victim_id: str, victim_data: dict):
        try:
            self.update_(victim_id, victim_data)
            return {"message": "Victim information updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))