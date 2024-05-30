import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_solution(student_prompts):
    prompt = (
        "You are an expert chatbot name - Segabot, in the field of computer science."
        f" Here's the question you asked me: {student_prompts}"
        " Now, let me provide you with a specific and well-formed solution in about 200 words."
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    opt = chat_completion.choices[0].message.content + '\n\n'
    return opt


def main():
    print("Welcome to this AI Chatbot.")
    while True:
        print("Welcome to Chatarea or type 'exit' to close the chat.")
        student_prompts = input("Enter Your Query: ")
        if student_prompts.lower() == 'exit':
            print("Thanks for visiting.")
            break
        answers = get_solution(student_prompts)
        print(f"AI Chatbots Answer : \n {answers}")
        

if __name__ == '__main__':
    main()
        