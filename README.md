# SE-2025Spring-GitOffMyLawn

Data analysis and visualization of bird flu data provided by the CDC

# Team members:

|      Name      |    Username    |            Email            |
| :------------: | :------------: | :-------------------------: |
| David Stepanov |    jajajava    | ds29123@georgiasouthern.edu |
|  Sydney Boles  |  BlueRogue12   | sb35329@georgiasouthern.edu |
|    Kai Fang    |   Kaifang02    | kf12106@georgiasouthern.edu |
| Michael Aaron  |    MAaron45    | ma17700@georgiasouthern.edu |
| Phillip Mejia  | oscarmejia1776 | om00913@georgiasouthern.edu |

## Getting Started

Before running the project, ensure you have:

Python 3.10+ installed → Check by running:

```bash
  python --version
```

Git installed → Check by running:

```bash
  git --version
```

Node.js & npm (for frontend development) → Check by running:

```bash
  node -v
  npm -v

```

## Setting Up the project

1. **Clone the repository**
   Run this command in whatever directory you want the project

```bash
  git clone https://github.com/GSU-CS-Intro-to-Software-Engineering/SE-2025Spring-GitOffMyLawn.git
```

## Backend Setup

2. **Create and activate a virtual environment**

```bash
python3 -m venv flu_finder_venv
source flu_finder_venv/bin/activate  # For macOS/Linux
flu_finder_venv\Scripts\Activate     # For Windows (PowerShell)
```

3. **Install dependencies**

(Includes Flask, Flask-CORS, and database dependencies)

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a .env file in the root directory and add:

```bash
DATABASE_URL=your_postgres_url_here
DOWNLOAD_PATH=flu_finder_src/data.csv
```

5. **Test the database connection**

```bash
python -c "from db import test_query; test_query()"
```

If successful, you should see:

```bash
Connected to database
Database time: YYYY-MM-DD HH:MM:SS+00:00
```

6. **Fetching the Latest CDC Data**

Before running queries, you need to **fetch the latest data** from the CDC.
The script `data_fetcher.py` downloads and saves the dataset as a local `data.csv` file inside of the `flu_finder_src` folder.

Your data should now be up to date from the CDC.

### **Running the Backend API**

To start the Flask backend, run:

```bash
python flu_finder_src/app.py
```

This will start the backend on:

➡ http://127.0.0.1:5000/

## Frontend Setup (React + Vite)

⚠️ **Make sure the backend is running before testing frontend API calls.**

1. **Navigate to the Frontend Folder**

```bash
cd flu_finder_frontend
```

2. **Install Dependencies**

```bash
npm install
```

3. **Run the Development Server**

```bash
npm run dev
```

This will start the React app, and you can access it at:
➡ http://localhost:5173/

## Additional Notes

This project uses Vite for the frontend, which provides fast hot module replacement (HMR) and optimized builds.
If you need to expand the ESLint configuration, check out:

[@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md)

[@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc/blob/main/README.md)
