from google.cloud import storage

client = storage.Client()

# Create a new storage bucket
new_bucket = client.create_bucket("hello-world-2-storage")

# create a blob(file) to be uploaded
new_blob= new_bucket.blob("test-folder/manage.py")

# upload the file
new_blob.upload_from_filename(filename="first_api/manage.py")