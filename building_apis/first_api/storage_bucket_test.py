from google.cloud import storage

client = storage.Client()

# Create a new storage bucket
new_bucket = client.create_bucket("hello-world-2-storage")

# create