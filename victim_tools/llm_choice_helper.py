import litellm
import requests
import nexa.general
import nexa.utils
import streamlit as st
import time
st.title("Model Chooser")
st._config.set_option("runner.fastReruns", "false")


# add a radio button for local vs cloud, it should be nice and big
local_vs_cloud = st.radio("", ["Local", "Cloud"], index=0, horizontal=True)

if local_vs_cloud == "Local":
    with st.expander("Local Models", expanded=True):
        col1, col2 = st.columns(2)  
        with col1:
            url = 'https://model-hub-backend.nexa4ai.com/model/get-repo-and-usernames'
            # Get models in one line using list comprehension
            models = [f"{response['username']}/{response['repo_name']}" for response in requests.get(url).json()]
            # Add selectbox directly with models list
            model = st.selectbox("Select a model", models)
        if model:
            with col2:
                tag_url = "https://model-hub-backend.nexa4ai.com/model/quicksearch?query_owner=" + model.split("/")[0] + "&query_repo=" + model.split("/")[1]
                # repo_name / tag_name
                tags = [f"{details['repo_name']}:{details['tag_name']}" for details in requests.get(tag_url).json()]
                time.sleep(1)
                selected_tag = st.selectbox("Select a tag", tags)
        if st.button("Pull Model"):
            with st.spinner("Pulling model..."):
                full_path = model.split("/")[0] + "/" + selected_tag
                print(full_path)
                nexa.general.pull_model(model_path=full_path)


elif local_vs_cloud == "Cloud":
    with st.expander("Cloud Models", expanded=True):
        col1, col2 = st.columns(2)  
        with col1:
            provider = st.selectbox("Select a provider", list(litellm.models_by_provider.keys()))
            models = litellm.models_by_provider[provider]
        with col2:
            model = st.selectbox("Select a model", models)
        model_path = provider + "/" + model

    api = st.text_input(f"Enter your {provider} API key", type="password")
    prompt = st.text_input("Enter your prompt")
    if st.button("Generate Response"):
        st.write(model, ':', litellm.completion(model=model_path, api_key=api, messages=[{"role": "user", "content": prompt}]).choices[0].message.content)
