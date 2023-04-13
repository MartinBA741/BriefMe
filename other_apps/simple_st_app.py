from transformers import pipeline
import streamlit as st

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn",
                      framework='pt', device=-1)  # 0 for gpu and -1 for cpu
# Define the Streamlit app


def app():
    # Add a title to the app
    st.title("Summarizer App")

    # Create a text input field
    input_txt = st.text_input("Enter the text to summarize:")

    # Check if the user has entered any text
    if input_txt:
        # Call the summarization function
        result = summarizer(input_txt, max_length=1024,
                            min_length=30, do_sample=False)

        # Display the summarized text
        st.write("Summary:")
        st.write(result[0]['summary_text'])


# Run the Streamlit app
if __name__ == '__main__':
    app()
