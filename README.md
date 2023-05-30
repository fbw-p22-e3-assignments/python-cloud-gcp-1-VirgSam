# Python-Cloud-GCP-1

Below you can find a few task where you will need to use **Cloud Storage** service.

> All tasks assume that you have your **Google Cloud Platform** account ready.

#

## Task 1: Create Cloud Storage bucket

Follow the requirements:
* name it as you want
* objects should be **safe** in case of one **region** being shut down for whatever reason
* elements cannot be **removed** easily (e.g. by mistake)
* objects will be read **frequently**, but they won't be stored for a **long time**

#

## Task 2: Upload a file into your bucket using _GCP Console_

Simply use GCP Console and upload **any type of file** into your newly created bucket.
Also, **create a folder** and **upload any file** into it.

#

## Task 3: Upload a file into your bucket using _gsutil_

Now make the same as in **Task 2**, but using _gsutil_ tool.

> If you don't have _gsutil_ installed, follow the steps [here](https://cloud.google.com/storage/docs/gsutil_install).

#

## Task 4: Remove files and then the bucket

To practice using CLI, use _gsutil_ tool for it.
