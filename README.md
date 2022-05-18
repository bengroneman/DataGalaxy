# Data Engineer Intern Fall 2022 - Shopify Challenge
[![Netlify Status](https://api.netlify.com/api/v1/badges/de535978-4315-4d5d-99dd-f33db4bb6301/deploy-status)](https://app.netlify.com/sites/elaborate-pastelito-70d2ac/deploys)

Welcome to my submission for the Fall 2022 Data Engineer Intern Challenge!
I have created a simple web application that would allow users to add, share and apply filters to images uploaded.

## Client Requirements
- Build an image repository
- Allow users to upload images
- Images populate the homepage dynamically

## Production build
- Frontend is hosted on Netlify
    - url: [Image Repository Client](https://elaborate-pastelito-70d2ac.netlify.app/)
- Backend is hosted on Digital Ocean
    - url: [API Docs](http://164.90.152.35:4080/docs)

## Getting started
**Note:** You will need to have Node.js >= v16, and Python >= 3.5 to run this project
```bash
git clone https://github.com/bengroneman/DataGalaxy.git
```
```bash
cd DataGalaxy
```
### Server setup
```bash
cd server
```
*I encourage the use of virtual environments, but feel free to manage your dependencies how you see fit*
```bash
python3 -m venv env
```
```bash
source env/bin/activate 
```
```bash
pip install pytest "fastapi[all]" python-multipart sqlalchemy databases aiofiles aiosqlite uvicornt 
```
```bash
uvicorn main:app --reload
```
### Client setup
```bash
cd ../client
```
```bash
npm install
```
**Running locally**
```bash
npm run dev
```
**Building for production**
```bash
npm run test
```
```bash
npm run build && npm run preview
```

## Roadmap
- Add a search feature
- Add a filter feature
- Add a category to the image submission form