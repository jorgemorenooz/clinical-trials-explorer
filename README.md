# 🧪 Clinical Trials Explorer (CTE)

A cloud-native platform for exploring, managing, and analyzing clinical trials data. It combines modern web technologies, healthcare interoperability standards (FHIR), and AI-driven analytics to simulate real-world clinical informatics solutions.

This project was developed as a personal initiative to apply computer science principles in the context of clinical trial regulation and health informatics. It serves as a technical demonstration aligned with trainee roles in research and innovation at the European Medicines Agency.

---

## 🎯 Project Goals

- Develop a full CRUD system for managing simulated clinical trials
- Integrate real data from public registries such as ClinicalTrials.gov
- Provide a RESTful API compatible with the FHIR standard
- Apply machine learning and generative AI for data summarization and insights
- Deploy the system using modern, cloud-based serverless architecture

---

## 🧰 Technologies Used

| Domain                  | Stack / Tools                                |
|-------------------------|----------------------------------------------|
| Backend                 | Python (FastAPI), PostgreSQL                 |
| Frontend                | React, TailwindCSS                           |
| External Data Source    | ClinicalTrials.gov API                       |
| Healthcare Standards    | HL7 FHIR (ResearchStudy resource)            |
| Cloud Infrastructure    | AWS Lambda, API Gateway, DynamoDB / RDS      |
| AI & ML                 | Transformers, Scikit-learn, pandas           |
| CI/CD & DevOps          | GitHub Actions, Terraform                    |

---

## 📁 Project Structure

clinical-trials-explorer/
├── k8s/postgres/ # Kubernetes YAML files for PostgreSQL Service
├── backend/ # FastAPI backend and RESTful logic
├── frontend/ # React application
├── fhir_module/ # FHIR data conversion adapters
├── ml_ai/ # AI/ML analysis and summarization scripts
├── cloud/ # AWS Lambda & infrastructure configuration
├── docs/ # Architecture diagrams and documentation
├── tests/ # Unit and integration tests
└── README.md


---

## 🚧 Project Phases

### ✅ Phase 1: Design & Planning
- [x] GitHub repository setup
- [x] Define tech stack and project scope
- [x] Draft initial architecture diagram
- [x] Prepare README with roadmap and objectives

### ⌛ Phase 2: Backend CRUD API
- [ ] Build a FastAPI app with PostgreSQL
- [ ] Define `ClinicalTrial` model (title, disease, status, location, date, description)
- [ ] Implement full REST endpoints
- [ ] Add unit tests with `pytest`

### ⌛ Phase 3: React Frontend
- [ ] Connect to API and display trials list
- [ ] Add forms for create/edit/delete
- [ ] Style the UI and validate input

### ⌛ Phase 4: External Data Integration
- [ ] Use ClinicalTrials.gov API to fetch real trials
- [ ] Merge with local data
- [ ] Enable filtering and search

### ⌛ Phase 5: AI & ML Analysis
- [ ] Summarize trial descriptions using LLMs
- [ ] Perform basic clustering or classification
- [ ] Generate visual insights (charts)

### ⌛ Phase 6: FHIR API Implementation
- [ ] Map local data to FHIR `ResearchStudy` structure
- [ ] Implement RESTful endpoint `/fhir/researchstudy/{id}`
- [ ] Validate FHIR format with example clients

### ⌛ Phase 7: Cloud Deployment
- [ ] Deploy backend on AWS Lambda + API Gateway
- [ ] Use DynamoDB or RDS in the cloud
- [ ] Host frontend on Vercel or S3 + CloudFront
- [ ] Add custom domain and HTTPS

### ⌛ Phase 8: Documentation & Demo
- [ ] Finalize `README.md` with screenshots
- [ ] Create Mermaid or Draw.io diagrams
- [ ] Record a short demo walkthrough (optional)

---

## 📌 Status

This project is under active development as part of a personal portfolio to demonstrate cloud, software engineering, AI, and health informatics skills in preparation for trainee opportunities in regulated healthcare environments.

---

## 📄 License

MIT License — feel free to use and adapt for educational purposes.

## 1️⃣ Phase 1: Design & Planning

### ✅ Step 1: MVP Scope for Clinical Trials Explorer
- Users can create, read, update, and delete simulated clinical trial entries via a REST API.
- The backend provides a RESTful interface, exposing clinical trial data in a structured JSON format.
- The system can fetch and display real clinical trials from ClinicalTrials.gov using their public API.
- The frontend web app (React) allows users to view and filter clinical trials from both local and external sources.
- The backend includes an endpoint that returns clinical trials in FHIR-compatible format (e.g., ResearchStudy resource).
- All components (frontend, backend, data access) are modular, and the system can be deployed locally or to the cloud.

While real-time data is fetched from ClinicalTrials.gov for technical demonstration purposes, this application is conceptually aligned with EMA’s CTIS platform and the EU Clinical Trials Regulation.

---

### ✅ Step 2: Designing the `ClinicalTrial` Data Model

The main data entity in this application is a `ClinicalTrial`, structured to reflect core fields aligned with clinical research standards and compatible with future FHIR transformation.

#### 📄 Fields

- `id` — unique identifier (UUID or numeric)
- `official_title` — full official title of the trial
- `acronym` — short name or abbreviation
- `disease_area` — condition being studied (e.g., Diabetes)
- `trial_phase` — clinical phase (e.g., Phase I, II, III)
- `status` — current status (Ongoing, Completed, etc.)
- `start_date` — trial start date
- `end_date` — trial end date
- `country` — where the trial is conducted
- `sponsor` — sponsoring organization or entity
- `description` — full protocol or study summary

---

### ✅ Step 3: Choosing and Deploying the Database
PostgreSQL was selected over NoSQL solutions due to:

- Structured schema enforcement
- Strong support for complex queries (filtering by status, phase, etc.)
- Easy integration with healthcare data standards like **FHIR**
- Compatibility with both local development and future **cloud migration (Azure/AWS)**

To avoid installing a local PostgreSQL client, the database is deployed **inside a Kubernetes cluster** using **Minikube** and containerized via the official `postgres:15` image.

---

#### 🧰 Tools Used

- [Minikube](https://minikube.sigs.k8s.io/docs/start/) — local Kubernetes cluster
- [Docker](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64) — used as the container runtime for Minikube
- kubectl — Kubernetes CLI
- PostgreSQL 15 — running as a pod inside Kubernetes
- Kubernetes YAML manifests — to define `Secret`, `PVC`, `Deployment`, and `Service` in `k8s/postgres`

---

#### 🔧 Install Minikube on Windows
Start Minikube with Docker driver:

   ```bash
   minikube start --driver=docker
   ```

Verify the cluster is running:

   ```bash
   kubectl get nodes
   ```

---

#### 🚀 Deploy PostgreSQL to Minikube
Apply the Kubernetes manifests (defined in `k8s/postgres`) to deploy the PostgreSQL database and its supporting resources:

   ```bash
   kubectl apply -f k8s/postgres/
   ```

This will create:

- A Kubernetes Secret with the database credentials
- A PersistentVolumeClaim for PostgreSQL data
- A Deployment running the postgres:15 container
- A Service to expose PostgreSQL within the cluster

In order to verify that PostgreSQL is accessible by launching a temporary pod and connecting to the service:

   ```bash
   kubectl run test-client --rm -it --image=postgres:15 -- bash
   ```
Then inside the container::

   ```bash
   psql -h postgres -U postgres -d clinical_trials
   # password: postgres
   ```

---

#### 📄 View Logs (Optional)

To confirm it started properly and the env vars (from the secret) are working:

   ```bash
   kubectl logs deployment/postgres
   ```

We are looking for log lines like: `PostgreSQL init process complete; ready for start up.`

---

### ✅ Step 4: FastAPI Backend Setup
Setting up a FastAPI application will:
- Connect to our PostgreSQL database
- Define your ClinicalTrial data model
- Expose CRUD endpoints for clinical trials

---

#### Create backend structure

In our project, In order to keep things clean and scalable, database logic (`database.py`), models (`models.py`), schemas (`schemas.py`), and API logic (`main.py`) will be separated
:

   ```bash
   clinical-trials-explorer/
    └── backend/
        ├── app/
        │   ├── main.py
        │   ├── models.py
        │   ├── database.py
        │   ├── crud.py
        │   ├── schemas.py
        │   └── config.py
        └── requirements.txt
   ```

---

#### Install required dependencies

It is recommended to use a virtual environment:

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # or myenv\Scripts\activate on Windows
   ```

Then we can install the dependencies and save them:

   ```bash
   python.exe -m pip install --upgrade pip # Upgrade pip first
   pip install fastapi[all] sqlalchemy psycopg2-binary python-dotenv # Install dependencies
   pip freeze > requirements.txt  # save them
   ```

---

#### Setup Database Connection
Create a `database.py` file that handles:

- Connecting to PostgreSQL
- Creating a SessionLocal object to interact with the DB
- Managing the SQLAlchemy engine and Base

In backend/app/database.py, we will define:

1. DATABASE_URL from environment variable (.env file so app logic and environment-specific settings stay separate)
2. SQLAlchemy engine
3. SessionLocal class (your DB session factory)
4. Base object for your ORM models
5. get_db() function to automatically open and close the DB session

---

#### Define `ClinicalTrial` Model
Create a `models.py` file that will:

- Inherit from Base (defined in `database.py`)
- Map to a database table (e.g., clinical_trials)
- Match the fields defined in [📄 Fields](#-fields)

---

#### Define Schemas
Create a `schemas.py` file to define the **data shape used in the API**, using Pydantic.

This separates:
- Internal database logic (`models.py`)
- External input/output validation (`schemas.py`)

We will define three schemas:

| Schema               | Purpose                              |
|----------------------|--------------------------------------|
| `ClinicalTrialBase`  | Shared fields for creation and output |
| `ClinicalTrialCreate`| Inherits from base, used for POST    |
| `ClinicalTrial`      | Adds `id`, used for GET responses     |

The `ClinicalTrial` schema uses:

It is recommended to use a virtual environment:

   ```python
    class Config:
        orm_mode = True
   ```

---

#### FastAPI entrypoint in `main.py`

# https://www.linkedin.com/pulse/mapping-pydantic-models-sqlalchemy-other-orm-alembic-herman-varzari-fnspf/ For Mapping Pydantic models to SQLAlchemy models

#### Test the API
If not run, start Minikube with Docker driver:

   ```bash
   minikube start --driver=docker
   ```

Verify the cluster is running:

   ```bash
   kubectl get nodes
   ```

Expose the postgres service, connection can be tested running the file `test_conn.py`:

   ```bash
   minikube service postgres --url
   ```

This creates a temporary tunnel from a random high port the host, copy the URL in the `.env` file `DATABASE_URL=postgresql://postgres:postgres@$host:$port/clinical_trials`

Run the FastAPI app:

   ```bash
   uvicorn app.main:app --reload
   ```

We will see `GET /trials` and `POST /trials`, being able to click them and test them.

---

#### ❌❌❌❌Automate minikube tunnel to expose services automatically at startup

---

### ✅ Step 5: API Endpoints (CRUD)

#### `GET /trials`

```http
   GET /trials/
```

Returns a list of all clinical trials in the database.

   ```json
      [
         {
            "id": 1,
            "official_title": "Trial A",
            "acronym": "TA",
            "disease_area": "Diabetes",
            ...
         }
      ]
   ```

---

#### `GET /trials/{id}`

```http
   GET /trials/1
```

Returns a single trial by ID.<br>
**Response**:

   ```json
      {
         "official_title": "Trial A",
         "acronym": "TA",
         "disease_area": "Diabetes",
         "trial_phase": "Phase II",
         "status": "Ongoing",
         "start_date": "2023-05-01",
         "end_date": "2024-05-01",
         "country": "Germany",
         "sponsor": "University X",
         "description": "Study of X in Y population",
         "id": 1
      }
   ```

**Errors**:
- `404 Not Found` if ID does not exist

---

#### `POST /trials`

```http
   POST /trials
```

Creates a new clinical trial.<br>
**Request Body**:

   ```json
      {
         "official_title": "Trial A",
         "acronym": "TA",
         "disease_area": "Diabetes",
         "trial_phase": "Phase II",
         "status": "Ongoing",
         "start_date": "2023-05-01",
         "end_date": "2024-05-01",
         "country": "Germany",
         "sponsor": "University X",
         "description": "Study of X in Y population",
      }
   ```

**Response**: Same as `GET /trials/{id}`

---

#### `PUT /trials/{id}`

```http
   PUT /trials/1
```

Replaces all fields of an existing clinical trial.

**Request Body**: Same as `POST /trials/`

**Response**: Updated trial object

**Errors**:
- `404 Not Found` if ID does not exist

---

#### `DELETE /trials/{id}`

```http
   DELETE /trials/1
```

Deletes a trial by ID.

**Response**:
```json
   {
      "message": "Trial deleted"
   }
```

**Errors**:
- `404 Not Found` if ID does not exist

---
