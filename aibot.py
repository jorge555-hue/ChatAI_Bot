    def response_generator():
        response = ai_ask("Pretend you are a very friendly and helpful person.  Please provide a response given the provided context.  Please provide the response only with no before or after commentary.",
                          data=st.session_state.messages,
                          api_key=st.secrets["apikey"])
        for word in response.split():
            yield word + " "
            time.sleep(0.05)



