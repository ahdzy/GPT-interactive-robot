import openai
import GVF

# Set your OpenAI API key
api_key = "Your Key"
openai.api_key = api_key
start_sequence = "alpha"
restart_sequence = "thank you"

#student.iq
#api_key = "Your API"

def use(input_text):
    GVF.prompt += """\nUser: """ + input_text

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=GVF.prompt,
        temperature=0.8,
        max_tokens=100,
        top_p=0.7,
        frequency_penalty=0.2,
        presence_penalty=0.5
    )
    
    output_text = response.choices[0].text.strip().split(':')
    # Delete the first element
    del output_text[0]

    # Combine the remaining elements into a single string
    result_string = " ".join(output_text)

    print(result_string)
    GVF.prompt += """\nAssistant: """ + result_string
    return result_string



def use_last(input_text):
    #Add a new user message to the conversation

    user_message = {"role": "user", "content": input_text}
    GVF.conversation.append(user_message)
    Responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #assistant=GVF.assistant_id,
        messages=GVF.conversation,
        max_tokens=200,
        temperature=0.7,
        api_key=api_key,
        top_p=0.7,  # Adjusted top_p for a wider range of possibilities
        frequency_penalty=0.2,  # Reduced frequency_penalty for more diverse responses
        presence_penalty=0.5  # Increased presence_penalty for more coherent and context-aware responses
        )
    
    output_text = Responce.choices[0].message["content"].strip()
    print(output_text)

    user_message = {"role": "assistant", "content": output_text}
    GVF.conversation.append(user_message)
    return output_text



