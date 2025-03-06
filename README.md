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

## Setting Up the project

1. **Clone the repository**
   Run this command in whatever directory you want the project

```bash
  git clone https://github.com/GSU-CS-Intro-to-Software-Engineering/SE-2025Spring-GitOffMyLawn.git
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv flu_finder_venv
source flu_finder_venv/bin/activate  # For macOS/Linux
flu_finder_venv\Scripts\Activate     # For Windows (PowerShell)
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a .env file in the root directory and add:

```bash
DATABASE_URL=your_postgres_url_here
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
The script `data_fetcher.py` downloads and saves the dataset as a local `data.csv` file in the root of the project.

### **How to Run `data_fetcher.py`**

From the root directory run:

```bash
python flu_finder_src/utils/data_fetcher.py
```

Your data should now be up to date from the CDC.
