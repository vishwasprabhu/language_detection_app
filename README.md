# Deploy ML models using FastAPI, Docker

## Steps:
### 1. Develop, perform EDA and Save the Model [Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)
### 2. Create Docker Container

```bash
# Build the Docker image
docker build -t language_detection_app . 

# Run the Docker container
docker run -p 80:80 language_detection_app
```
### 3. Initialize and convert to a git repository
```bash
# Initialize a new Git repository
git init

# Commit the changes
git commit -m "initial commit"

#Add remote and create main branch
git remote add origin git@github.com:vishwasprabhu/language_detection_app.git
git push --set-upstream origin main 
