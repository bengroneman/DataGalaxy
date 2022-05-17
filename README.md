# Data Engineer Intern Fall 2022 - Shopify Challenge
Welcome to my submission for the Fall 2022 Data Engineer Intern Challenge!
I have created a simple web application that would allow users to add, share and apply filters to images uploaded.

## Client Requirements
- Build an image repository

## Running locally
```bash
git clone https://github.com/bengroneman/DataGalaxy.git
```
```bash
cd DataGalaxy
```
### Client setup
```bash
cd client
```
```bash
npm install
```
```bash
npm run dev
```
### Server setup
```bash
cd ../server
```
*I encourage the use of virtual environments, but feel free to manage your dependencies how you see fit*
```bash
python3 -m venv env
```
```bash
source env/bin/activate 
```
```bash
pip install pytest "fastapi[all]" python-multipart sqlalchemy
```
```bash
pytest
```
```bash
uvicorn main:app --reload
```
