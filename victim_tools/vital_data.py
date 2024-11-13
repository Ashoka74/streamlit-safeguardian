from typing import List, Tuple, Optional, Dict, Any
import streamlit as st
import google.generativeai as genai
import json
import os
import dotenv
from victim_tools.llm_utils import schema
import openai
import dotenv
dotenv.load_dotenv()


with open('configs/victim_json_template_flat.json', 'r') as f:
    structure = json.load(f)

try:
    gemini_api = os.getenv("gemini_api")
except Exception as e:
    print(f"No .env file, looking at secrets.toml")
    gemini_api = st.secrets["gemini_api"]

def update_victim_json(new_infos: Optional[Dict[str, Any]]):
    json_template = st.session_state.get('json_template', {})
    history_infos = st.session_state.get('victim_info', {})

    prompt = f"Update the JSON structure: {schema}\n\n with accurate informations based on history: {history_infos}\n\n and new informations: {new_infos}\n\n. Output should be a JSON file. Fit new information in the main structure of the template [{json_template.keys()}]. Leave blank (e.g.""), when there is no information. Do not overwrite existing information provided, unless it's to update it into something more informative. NEVER replace existing information with blank values! Ask follow-up questions to keep filling the json file, but in a natural way and prioritizing the most importants ones for rescue. Always update emergency_status! Output:"

    openai_api = os.getenv("openai_api")
    openai.api_key = openai_api
    model = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a helpful assistant that updates JSON files."}, {"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    response = model.choices[0].message.content
    print(response)
    
    return response 
