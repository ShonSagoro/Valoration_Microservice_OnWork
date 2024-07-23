import httpx
import os

class S3Service:
    def __init__(self):
        self.bucket_name = os.getenv('S3_BUCKET_NAME', 'my-bucket')
        self.folder_name = os.getenv('S3_FOLDER', 'uploads')
    
    async def execute(self, file: bytes, file_name: str, mime_type: str) -> str:
        s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{self.folder_name}/{file_name}"
        
        async with httpx.AsyncClient() as client:
            response = await client.put(
                s3_url,
                content=file,
                headers={
                    'Content-Type': mime_type,
                    'x-amz-acl': 'public-read',
                }
            )
        
        if response.status_code == 200:
            return s3_url
        else:
            raise Exception(f"Failed to upload file to S3: {response.text}")