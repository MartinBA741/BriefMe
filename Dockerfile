# Use the official PyTorch CPU image from Hugging Face as the base image
FROM huggingface/transformers-pytorch-cpu

# Set the environment variable
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the container
COPY . .

# Set the working directory to where the model.py file is located
WORKDIR .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "--server.port", "80", "app.py"]
