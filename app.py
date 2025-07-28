import streamlit as st
import openai
 
# Set your OpenAI API key securely
openai.api_key = "your-api-key-here"
 
st.title("🧪 Code Explanation & Debugger")
code_input = st.text_area("Paste your Python code below:", height=200)
 
# Optional: Ask for debugging help
debug_mode = st.checkbox("Include debugging suggestions")
 
if st.button("Explain Code"):
    if code_input.strip() == "":
        st.warning("Please enter some code to explain.")
    else:
        # Create prompt for GPT
        prompt = (f"Explain what this Python code does in simple terms:\n\n{code_input}\n\n"
    "Also identify potential errors or exceptions this code might throw during execution, "
    "and explain how they can be handled using proper error-handling techniques like try-except blocks. ")
        if debug_mode:
            prompt += "\n\nAlso suggest possible bugs or improvements."
 
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You're a helpful Python expert. You explain code clearly and also provide insights on potential errors, exceptions, and how to improve reliability using good programming practices."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            explanation = response['choices'][0]['message']['content']
            st.subheader("💡 Explanation")
            st.write(explanation)
        except Exception as e:
            st.error(f"Error: {str(e)}")