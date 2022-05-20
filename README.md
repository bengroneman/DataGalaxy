# Data Engineer Intern Fall 2022 - Shopify Challenge

Welcome to my submission for the Fall 2022 Data Engineer Intern Challenge!
I have created a simple web application that enables users to add images to a repository and dynamically see other submissions.

## Client Requirements
- Build an image repository
- Allow users to upload images
- Images populate the homepage dynamically

## Production build
- Production is being hosted on a Digital Ocean server
    - client: [Image Repository Client](http://164.90.152.35:4081/)
    - server: [API Docs](http://164.90.152.35:4080/docs)

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

**Note:** I am using [virtualenv](https://virtualenv.pypa.io/en/latest/) here coupled with Python 3.8
```bash
python3 -m venv env
```
```bash
source env/bin/activate 
```
```bash
pip install "fastapi[all]" sqlalchemy databases aiofiles aiosqlite uvicorn
```
If you receive the following error just ensure you have wheel installed (```pip install wheel```)
then rerun the command to ensure dependencies are met

> ERROR: Failed building wheel for python-multipart

Otherwise you can get the server up and running with:
```bash
uvicorn main:app --reload
```
### Client setup
**Note:** leave the server running - switch to another terminal to run the client
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
I am using [playwright](https://playwright.dev/) for end-to-end testing (```npx playwright install```)

```bash
npm run test
```
```bash
npm run build && npm run preview
```

## Roadmap
- Add a search feature
- Add a filter feature
- ~~Add a category to the image submission form~~
- Add charts to show a breakdown of size / category
