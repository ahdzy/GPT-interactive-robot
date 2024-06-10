import openai

# Set your OpenAI API key
api_key = "your API"
openai.api_key = api_key


start_sequence = "alpha"
restart_sequence = "thank you"


# Function to interact with your assistant
import openai
import GVF


#student.iq
#api_key = "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"

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key


start_sequence = "alpha"
restart_sequence = "thank you"


def use(input_text):
    GVF.prompt += """User: """ + input_text + "\n"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=GVF.prompt,
        temperature=0.8,
        max_tokens=256,
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
    GVF.prompt += """Assistant: """ + result_string + "\n"
    return result_string

use("hello alpha")
print(GVF.prompt)